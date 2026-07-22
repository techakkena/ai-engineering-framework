from llm.schema import ExtractedDocument, Field
from output.to_image import build_image

# Realistic invoice vocabulary with heavy conjuncts/vowel-sign clusters
summary = "ఈ పత్రం ఒక వాణిజ్య సంస్థ జారీ చేసిన కొనుగోలు ఇన్‌వాయిస్ వివరాలను తెలియజేస్తుంది."
vendor = "శ్రీ వేంకటేశ్వర సంస్థ ప్రైవేట్ లిమిటెడ్"
label = "చెల్లింపు నిబంధనలు"
value = "సరఫరా చేసిన వెంటనే చెల్లించవలసి యున్నది."

doc = ExtractedDocument(
    document_type="ఇన్‌వాయిస్",
    summary=summary,
    vendor_name=vendor,
    invoice_number="INV-2026-0042",
    fields=[Field(label=label, value=value)],
)
img = build_image(doc, "Telugu")
with open(".fonttest/telugu_conjuncts.png", "wb") as f:
    f.write(img)
print("built", len(img))
