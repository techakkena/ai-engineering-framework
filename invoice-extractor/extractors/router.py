from fastapi import HTTPException

from extractors import image, pdf, spreadsheet, text

SPREADSHEET_EXTENSIONS = {"csv", "xlsx", "xls"}
IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}


def detect_and_extract(filename: str, data: bytes) -> dict:
    extension = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""

    if extension == "pdf":
        return pdf.extract(data)
    if extension in IMAGE_EXTENSIONS:
        return image.extract(data)
    if extension in SPREADSHEET_EXTENSIONS:
        return spreadsheet.extract(data, extension)
    if extension == "txt":
        return text.extract(data)

    raise HTTPException(status_code=400, detail=f"Unsupported file type: .{extension or 'unknown'}")
