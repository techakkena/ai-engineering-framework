from fastapi import HTTPException

from llm.openai_client import get_client, get_model
from llm.schema import LanguageDetection

MAX_DETECTION_CHARS = 6000

DETECT_LANGUAGE_PROMPT = """Identify the primary language of the text below.

Supported languages (ONLY these six are valid):
English, Telugu, Hindi, Tamil, Malayalam, Kannada

Document text:
\"\"\"
{text}
\"\"\"

Rules:
- Judge the language from descriptive/textual content only. Ignore numbers, dates,
  currency symbols, and proper nouns/brand names when deciding — they don't indicate language.
- If the document mixes languages, choose whichever has the most textual content.
- Do not guess from script alone. Hindi, Marathi, and Sanskrit all use Devanagari script —
  distinguish using vocabulary and grammar, not script.
- If the dominant language is not one of the six supported languages, set is_supported to false
  and detected_language to the actual language name you identified (do not force-fit it).
- If the text is too short or unclear to judge confidently, set confidence to "low" rather
  than guessing "high"."""


def detect_language(text: str) -> LanguageDetection:
    client = get_client()
    prompt = DETECT_LANGUAGE_PROMPT.format(text=text[:MAX_DETECTION_CHARS])

    try:
        response = client.responses.parse(
            model=get_model(),
            input=[{"role": "user", "content": prompt}],
            text_format=LanguageDetection,
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Language detection failed: {exc}") from exc

    return response.output_parsed
