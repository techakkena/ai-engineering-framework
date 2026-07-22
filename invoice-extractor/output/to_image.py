import io

import pypdfium2 as pdfium

from llm.schema import ExtractedDocument
from output.to_pdf import build_pdf_report

RENDER_SCALE = 2.0


def build_image(data: ExtractedDocument, target_language: str = "English") -> bytes:
    pdf_bytes = build_pdf_report(data, target_language)

    doc = pdfium.PdfDocument(pdf_bytes)
    try:
        # Only page 1 is rendered; longer reports are truncated to a single image.
        page = doc[0]
        bitmap = page.render(scale=RENDER_SCALE)
        buffer = io.BytesIO()
        bitmap.to_pil().save(buffer, format="PNG")
        bitmap.close()
        page.close()
        return buffer.getvalue()
    finally:
        doc.close()
