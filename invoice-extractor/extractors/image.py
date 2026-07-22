import io

from fastapi import HTTPException
from PIL import Image

SUPPORTED_FORMATS = {"PNG", "JPEG", "WEBP"}


def extract(data: bytes) -> dict:
    try:
        with Image.open(io.BytesIO(data)) as img:
            img.verify()
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid image.") from exc

    return {"kind": "images", "images": [data], "truncated": False}
