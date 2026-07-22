import io
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from llm.schema import ExtractedDocument

FONTS_DIR = Path(__file__).resolve().parent.parent / "assets" / "fonts"

# Languages needing a bundled Unicode font — Helvetica has no glyphs for these scripts.
# All five share one merged Latin+Devanagari+Telugu+Tamil+Malayalam+Kannada font file:
# registering separate per-script fonts (each merged from the same Latin source) causes
# ReportLab's font cache to corrupt glyph rendering once more than one is registered.
UNICODE_LANGUAGES = {"Hindi", "Telugu", "Tamil", "Malayalam", "Kannada"}
FONT_NAME = "NotoSansIndic"
FONT_FILE = "NotoSansIndic-Regular.ttf"

_font_registered = False


def _resolve_font(target_language: str) -> str | None:
    global _font_registered
    if target_language not in UNICODE_LANGUAGES:
        return None
    if not _font_registered:
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONTS_DIR / FONT_FILE)))
        _font_registered = True
    return FONT_NAME


SCALAR_FIELDS = [
    "invoice_number",
    "invoice_date",
    "due_date",
    "vendor_name",
    "vendor_address",
    "customer_name",
    "subtotal",
    "tax",
    "total",
    "currency",
]

LINE_ITEM_HEADERS = ["description", "quantity", "unit_price", "amount"]

TABLE_STYLE = TableStyle(
    [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f2937")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]
)

MIN_COLUMN_WIDTH = 60


def _wrapped_table(rows: list[list], available_width: float, cell_style, header_style) -> Table:
    col_count = max(len(row) for row in rows)
    col_width = max(available_width / col_count, MIN_COLUMN_WIDTH)

    wrapped_rows = [
        [
            Paragraph(str(cell), header_style if r == 0 else cell_style)
            for cell in row + [""] * (col_count - len(row))
        ]
        for r, row in enumerate(rows)
    ]
    return Table(wrapped_rows, colWidths=[col_width] * col_count, style=TABLE_STYLE, hAlign="LEFT")


def build_pdf_report(data: ExtractedDocument, target_language: str = "English") -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    font_name = _resolve_font(target_language)
    title_style = styles["Title"]
    body_style = styles["BodyText"]
    heading_style = styles["Heading2"]
    cell_style = body_style
    if font_name:
        title_style = ParagraphStyle("TitleUnicode", parent=title_style, fontName=font_name)
        body_style = ParagraphStyle("BodyUnicode", parent=body_style, fontName=font_name)
        heading_style = ParagraphStyle("HeadingUnicode", parent=heading_style, fontName=font_name)
        cell_style = body_style
    header_style = ParagraphStyle(
        "TableHeader",
        parent=cell_style,
        textColor=colors.white,
        fontName=font_name or "Helvetica-Bold",
    )

    story = [Paragraph(data.document_type or "Extracted Document", title_style)]

    if data.summary:
        story.append(Spacer(1, 8))
        story.append(Paragraph(data.summary, body_style))

    detail_rows = [
        [field.replace("_", " ").title(), str(getattr(data, field))]
        for field in SCALAR_FIELDS
        if getattr(data, field) is not None
    ]
    for extra in data.fields:
        detail_rows.append([extra.label, extra.value])

    if detail_rows:
        story.append(Spacer(1, 16))
        story.append(Paragraph("Details", heading_style))
        story.append(
            _wrapped_table([["Field", "Value"]] + detail_rows, doc.width, cell_style, header_style)
        )

    if data.line_items:
        story.append(Spacer(1, 16))
        story.append(Paragraph("Line Items", heading_style))
        rows = [LINE_ITEM_HEADERS] + [
            [str(getattr(item, header)) for header in LINE_ITEM_HEADERS] for item in data.line_items
        ]
        story.append(_wrapped_table(rows, doc.width, cell_style, header_style))

    for table in data.tables:
        rows = ([table.headers] if table.headers else []) + table.rows
        if not rows:
            continue
        story.append(Spacer(1, 16))
        story.append(Paragraph(table.title or "Table", heading_style))
        story.append(_wrapped_table(rows, doc.width, cell_style, header_style))

    doc.build(story)
    return buffer.getvalue()
