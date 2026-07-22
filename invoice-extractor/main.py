from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Query, UploadFile
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse

from extractors.router import detect_and_extract
from llm.detect_language import detect_language
from llm.schema import SUPPORTED_LANGUAGES
from llm.structure import extract_invoice_fields
from output.to_excel import build_workbook
from output.to_image import build_image
from output.to_pdf import build_pdf_report
from output.to_word import build_word_report
from utils.validation import validate_upload

app = FastAPI(title="Invoice/Document Data Extractor")

FRONTEND_PATH = Path(__file__).parent / "frontend" / "index.html"

DOWNLOAD_BUILDERS = {
    "xlsx": (
        build_workbook,
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "extracted.xlsx",
    ),
    "pdf": (build_pdf_report, "application/pdf", "extracted.pdf"),
    "image": (build_image, "image/png", "extracted.png"),
    "docx": (
        build_word_report,
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "extracted.docx",
    ),
}

# Formats whose builder renders text into embedded glyphs and therefore needs to know
# the target language to pick a Unicode font. xlsx/docx store text natively and don't.
LANGUAGE_AWARE_OUTPUTS = {"pdf", "image"}


@app.get("/")
def index() -> FileResponse:
    return FileResponse(FRONTEND_PATH)


@app.post("/extract")
async def extract(
    file: UploadFile,
    output: str = Query(default="json", pattern="^(json|xlsx|pdf|image|docx)$"),
    target_language: str = Query(default="English", pattern="^(" + "|".join(SUPPORTED_LANGUAGES) + ")$"),
):
    data = await file.read()
    validate_upload(file.filename, len(data))

    content = detect_and_extract(file.filename, data)

    detected_language = "unknown"
    if content["kind"] == "text":
        detected_language = detect_language(content["text"]).detected_language

    extracted = extract_invoice_fields(content, detected_language, target_language)

    if output in DOWNLOAD_BUILDERS:
        builder, media_type, filename = DOWNLOAD_BUILDERS[output]
        payload = (
            builder(extracted, target_language) if output in LANGUAGE_AWARE_OUTPUTS else builder(extracted)
        )
        return StreamingResponse(
            iter([payload]),
            media_type=media_type,
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )

    return JSONResponse(extracted.())
