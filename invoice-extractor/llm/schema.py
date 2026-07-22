from pydantic import BaseModel

SUPPORTED_LANGUAGES = ["English", "Telugu", "Hindi", "Tamil", "Malayalam", "Kannada"]


class LanguageDetection(BaseModel):
    detected_language: str
    language_code: str
    is_supported: bool
    confidence: str


class LineItem(BaseModel):
    description: str | None = None
    quantity: float | None = None
    unit_price: float | None = None
    amount: float | None = None


class Field(BaseModel):
    label: str
    value: str


class Table(BaseModel):
    title: str | None = None
    headers: list[str] = []
    rows: list[list[str]] = []


class ExtractedDocument(BaseModel):
    document_type: str | None = None
    summary: str | None = None

    # Invoice/receipt-specific fields — populated when applicable, null otherwise.
    invoice_number: str | None = None
    invoice_date: str | None = None
    due_date: str | None = None
    vendor_name: str | None = None
    vendor_address: str | None = None
    customer_name: str | None = None
    line_items: list[LineItem] = []
    subtotal: float | None = None
    tax: float | None = None
    total: float | None = None
    currency: str | None = None

    # Generic catch-all for anything not covered by the fields above.
    fields: list[Field] = []
    tables: list[Table] = []
