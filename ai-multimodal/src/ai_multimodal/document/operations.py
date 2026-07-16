"""
Enterprise document operations for the ai_multimodal.document package.

This module provides provider-independent abstractions for document parsing,
classification, summarization, information extraction, and metadata retrieval.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_multimodal.document.constants import (
    DEFAULT_CONFIDENCE_THRESHOLD,
    DEFAULT_DOCUMENT_FORMAT,
    DEFAULT_LANGUAGE,
    MAX_DOCUMENT_PAGES,
    SUPPORTED_DOCUMENT_FORMATS,
    SUPPORTED_LANGUAGES,
)
from ai_multimodal.document.exceptions import (
    DocumentClassificationError,
    DocumentValidationError,
    UnsupportedDocumentFormatError,
    UnsupportedLanguageError,
)


@dataclass(slots=True, frozen=True)
class DocumentResult:
    """Represents the result of a document operation."""

    task: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def _validate_document_path(document_path: str) -> None:
    """Validate a document path."""
    if not document_path.strip():
        raise DocumentValidationError(
            "Document path cannot be empty."
        )


def _validate_document_format(document_format: str) -> None:
    """Validate a document format."""
    if document_format.lower() not in SUPPORTED_DOCUMENT_FORMATS:
        raise UnsupportedDocumentFormatError(
            f"Unsupported document format: {document_format!r}."
        )


def parse_document(
    document_path: str,
    *,
    document_format: str = DEFAULT_DOCUMENT_FORMAT,
    language: str = DEFAULT_LANGUAGE,
) -> DocumentResult:
    """
    Parse a document.
    """
    _validate_document_path(document_path)
    _validate_document_format(document_format)

    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageError(
            f"Unsupported language: {language!r}."
        )

    return DocumentResult(
        task="parse",
        success=True,
        data={
            "document_path": document_path,
            "document_format": document_format,
            "language": language,
        },
    )


def classify_document(
    document_path: str,
    *,
    confidence_threshold: float = DEFAULT_CONFIDENCE_THRESHOLD,
) -> DocumentResult:
    """
    Classify a document.
    """
    _validate_document_path(document_path)

    if not 0.0 <= confidence_threshold <= 1.0:
        raise DocumentClassificationError(
            "Confidence threshold must be between 0.0 and 1.0."
        )

    return DocumentResult(
        task="classification",
        success=True,
        data={
            "document_path": document_path,
            "confidence_threshold": confidence_threshold,
        },
    )


def summarize_document(
    document_path: str,
) -> DocumentResult:
    """
    Summarize a document.
    """
    _validate_document_path(document_path)

    return DocumentResult(
        task="summarization",
        success=True,
        data={
            "document_path": document_path,
        },
    )


def extract_document_data(
    document_path: str,
) -> DocumentResult:
    """
    Extract structured information from a document.
    """
    _validate_document_path(document_path)

    return DocumentResult(
        task="extraction",
        success=True,
        data={
            "document_path": document_path,
        },
    )


def get_document_metadata(
    document_path: str,
) -> DocumentResult:
    """
    Retrieve document metadata.
    """
    _validate_document_path(document_path)

    return DocumentResult(
        task="metadata",
        success=True,
        metadata={
            "document_path": document_path,
            "max_pages": MAX_DOCUMENT_PAGES,
        },
    )