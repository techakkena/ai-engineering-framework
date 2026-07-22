import os

from fastapi import HTTPException

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "webp", "xlsx", "xls", "csv", "txt"}


def validate_upload(filename: str, size_bytes: int) -> None:
    if not filename or "." not in filename:
        raise HTTPException(status_code=400, detail="File has no extension.")

    extension = filename.rsplit(".", 1)[-1].lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: .{extension}")

    max_bytes = int(os.getenv("MAX_UPLOAD_MB", "15")) * 1024 * 1024
    if size_bytes > max_bytes:
        raise HTTPException(status_code=400, detail=f"File exceeds the {max_bytes // (1024 * 1024)}MB limit.")
