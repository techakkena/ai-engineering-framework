"""
Unit tests for ai_multimodal.document.exceptions.
"""

from __future__ import annotations

import pytest

from ai_multimodal.document.exceptions import (
    DocumentClassificationError,
    DocumentError,
    DocumentExtractionError,
    DocumentMetadataError,
    DocumentParsingError,
    DocumentProcessingError,
    DocumentProviderError,
    DocumentSummarizationError,
    DocumentValidationError,
    UnsupportedDocumentFormatError,
    UnsupportedLanguageError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        DocumentValidationError,
        UnsupportedDocumentFormatError,
        UnsupportedLanguageError,
        DocumentProcessingError,
        DocumentParsingError,
        DocumentClassificationError,
        DocumentSummarizationError,
        DocumentExtractionError,
        DocumentMetadataError,
        DocumentProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DocumentError],
) -> None:
    """Every custom exception should inherit from DocumentError."""
    assert issubclass(exception_class, DocumentError)


def test_exception_message() -> None:
    """Exception message should be preserved."""
    with pytest.raises(DocumentError, match="document failure"):
        raise DocumentError("document failure")