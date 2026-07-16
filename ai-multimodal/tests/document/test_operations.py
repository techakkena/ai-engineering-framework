"""
Unit tests for ai_multimodal.document.operations.
"""

from __future__ import annotations

import pytest

from ai_multimodal.document.exceptions import (
    DocumentClassificationError,
    DocumentValidationError,
    UnsupportedDocumentFormatError,
    UnsupportedLanguageError,
)
from ai_multimodal.document.operations import (
    DocumentResult,
    classify_document,
    extract_document_data,
    get_document_metadata,
    parse_document,
    summarize_document,
)


def test_parse_document_success() -> None:
    """Document parsing should succeed."""
    result = parse_document("document.pdf")

    assert isinstance(result, DocumentResult)
    assert result.success is True
    assert result.task == "parse"


def test_parse_invalid_format() -> None:
    """Unsupported formats should raise."""
    with pytest.raises(UnsupportedDocumentFormatError):
        parse_document(
            "document.xyz",
            document_format="xyz",
        )


def test_parse_invalid_language() -> None:
    """Unsupported language should raise."""
    with pytest.raises(UnsupportedLanguageError):
        parse_document(
            "document.pdf",
            language="xx",
        )


def test_parse_empty_path() -> None:
    """Empty document path should raise."""
    with pytest.raises(DocumentValidationError):
        parse_document("")


def test_classify_document_success() -> None:
    """Document classification should succeed."""
    result = classify_document("document.pdf")

    assert result.success is True
    assert result.task == "classification"


def test_classify_invalid_threshold() -> None:
    """Invalid confidence threshold should raise."""
    with pytest.raises(DocumentClassificationError):
        classify_document(
            "document.pdf",
            confidence_threshold=2.0,
        )


def test_summarize_document_success() -> None:
    """Document summarization should succeed."""
    result = summarize_document("document.pdf")

    assert result.success is True
    assert result.task == "summarization"


def test_extract_document_data_success() -> None:
    """Document extraction should succeed."""
    result = extract_document_data("document.pdf")

    assert result.success is True
    assert result.task == "extraction"


def test_get_document_metadata_success() -> None:
    """Metadata retrieval should succeed."""
    result = get_document_metadata("document.pdf")

    assert result.success is True
    assert result.task == "metadata"