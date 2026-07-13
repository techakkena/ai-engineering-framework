from ai_rag.documents.constants import (
    DEFAULT_DOCUMENT_ID,
    DEFAULT_DOCUMENT_SOURCE,
    SUPPORTED_DOCUMENT_TYPES,
)


def test_default_document_id():
    assert DEFAULT_DOCUMENT_ID == "document"


def test_default_document_source():
    assert DEFAULT_DOCUMENT_SOURCE == "unknown"


def test_supported_document_types():
    assert "pdf" in SUPPORTED_DOCUMENT_TYPES
    assert "txt" in SUPPORTED_DOCUMENT_TYPES