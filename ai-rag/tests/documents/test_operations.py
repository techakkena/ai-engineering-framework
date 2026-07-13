from ai_rag.documents.operations import (
    default_document_id,
    default_document_source,
    document_type,
    supported_document_type,
)


def test_default_document_id():
    assert default_document_id() == "document"


def test_default_document_source():
    assert default_document_source() == "unknown"


def test_document_type():
    assert document_type("report.pdf") == "pdf"


def test_supported_document_type():
    assert supported_document_type("pdf")


def test_unsupported_document_type():
    assert not supported_document_type("exe")