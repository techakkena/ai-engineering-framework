import io

import pypdfium2 as pdfium
from fastapi import HTTPException

MAX_SCANNED_PAGES = 10
MIN_CHARS_PER_PAGE_FOR_NATIVE_TEXT = 20
RENDER_SCALE = 200 / 72  # ~200 DPI


def extract(data: bytes) -> dict:
    try:
        doc = pdfium.PdfDocument(data)
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Could not open the uploaded PDF.") from exc

    try:
        page_count = len(doc)
        page_texts = []
        for i in range(page_count):
            page = doc[i]
            textpage = page.get_textpage()
            page_texts.append(textpage.get_text_range())
            textpage.close()
            page.close()

        avg_chars = sum(len(t) for t in page_texts) / max(page_count, 1)
        if avg_chars >= MIN_CHARS_PER_PAGE_FOR_NATIVE_TEXT:
            return {"kind": "text", "text": "\n\n".join(page_texts)}

        truncated = page_count > MAX_SCANNED_PAGES
        images = []
        for i in range(min(page_count, MAX_SCANNED_PAGES)):
            page = doc[i]
            bitmap = page.render(scale=RENDER_SCALE)
            buffer = io.BytesIO()
            bitmap.to_pil().save(buffer, format="PNG")
            images.append(buffer.getvalue())
            bitmap.close()
            page.close()

        return {"kind": "images", "images": images, "truncated": truncated}
    finally:
        doc.close()
