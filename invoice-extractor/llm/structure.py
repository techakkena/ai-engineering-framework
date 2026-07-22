import base64

from fastapi import HTTPException

from llm.openai_client import get_client, get_model
from llm.schema import ExtractedDocument

BASE_SYSTEM_PROMPT = (
    "You extract structured data from the provided document, which could be an "
    "invoice, receipt, report, form, or any other kind of document or image.\n"
    "- First identify the document type.\n"
    "- If it is an invoice or receipt, fill invoice_number, invoice_date, due_date, "
    "vendor_name, vendor_address, customer_name, line_items, subtotal, tax, total, "
    "and currency. Leave these null if the document is not an invoice/receipt.\n"
    "- Always write a short 1-2 sentence summary of the document.\n"
    "- Always also capture any other notable facts as label/value pairs in `fields`, "
    "and any other tabular or grouped content (stats, comparisons, timelines, etc.) "
    "as entries in `tables`.\n"
    "Leave a field null/empty only if it is genuinely not present. Amounts must be "
    "plain numbers (no currency symbols or thousands separators)."
)

TRANSLATION_PROMPT = (
    "\n\n"
    "Source document language: {detected_language}\n"
    "Target output language for text values: {target_language}\n\n"
    "Translation rules:\n"
    "1. Every field KEY in the output stays exactly as defined above (e.g. "
    "vendor_name, line_items, fields, tables) regardless of the target language. "
    "Only field VALUES get translated.\n"
    "2. Translate only descriptive text values — summary, vendor_name, "
    "vendor_address, customer_name, line_items descriptions, and the labels/values "
    "inside `fields` and `tables` — into {target_language}.\n"
    "3. NEVER translate, convert, or alter: numbers, dates, invoice/reference "
    "numbers, currency symbols, tax IDs, phone numbers, email addresses, URLs, "
    "percentages, or alphanumeric codes. Copy these exactly, character for "
    "character, as they appear in the source.\n"
    "4. Preserve the source numeral system exactly (e.g. do not convert Latin "
    "digits to any other numeral system, and do not convert non-Latin numerals to "
    "Latin, unless the source already uses Latin digits).\n"
    "5. Keep proper nouns (company names, brand names, person names) in their "
    "original form unless a well-established localized equivalent exists (e.g. a "
    "country name).\n"
    "6. If the target language equals the source document language, copy text "
    "values as-is — do not re-translate or paraphrase text that's already in the "
    "target language.\n"
    "7. If the target language is English, translate all descriptive text values "
    "to English regardless of the source document language.\n"
    "8. If the source document language is unknown, infer it from the document "
    "content itself before applying the rules above.\n"
    "9. Use natural, contemporary {target_language} vocabulary and grammar — not "
    "Sanskrit. {target_language} shares script and many loanwords with Sanskrit "
    "(and, for Devanagari, with Hindi/Marathi), but do not substitute pure Sanskrit "
    "words, inflections, or sentence structure for everyday {target_language} "
    "usage. Prefer the word a native {target_language} speaker would actually use "
    "in this context, even when a more Sanskrit-derived synonym exists."
)


def _build_system_prompt(detected_language: str, target_language: str) -> str:
    return BASE_SYSTEM_PROMPT + TRANSLATION_PROMPT.format(
        detected_language=detected_language, target_language=target_language
    )


def extract_invoice_fields(
    content: dict,
    detected_language: str = "unknown",
    target_language: str = "English",
) -> ExtractedDocument:
    model = get_model()
    client = get_client()
    system_prompt = _build_system_prompt(detected_language, target_language)

    if content["kind"] == "text":
        user_content = [{"type": "input_text", "text": content["text"]}]
    else:
        user_content = [
            {"type": "input_text", "text": "Extract the structured data from these page image(s)."}
        ]
        for image_bytes in content["images"]:
            b64 = base64.b64encode(image_bytes).decode("ascii")
            user_content.append(
                {"type": "input_image", "image_url": f"data:image/png;base64,{b64}"}
            )

    try:
        response = client.responses.parse(
            model=model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            text_format=ExtractedDocument,
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"LLM extraction failed: {exc}") from exc

    return response.output_parsed
