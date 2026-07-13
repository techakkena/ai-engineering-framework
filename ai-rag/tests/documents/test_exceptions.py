from ai_rag.documents.exceptions import (
    DocumentError,
    InvalidDocumentError,
    UnsupportedDocumentTypeError,
)


def test_document_error():
    assert issubclass(
        DocumentError,
        Exception,
    )


def test_invalid_document_error():
    assert issubclass(
        InvalidDocumentError,
        DocumentError,
    )


def test_unsupported_document_type_error():
    assert issubclass(
        UnsupportedDocumentTypeError,
        DocumentError,
    )