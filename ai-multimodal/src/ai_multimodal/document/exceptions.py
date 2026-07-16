"""
Exceptions for the ai_multimodal.document package.

This module defines the exception hierarchy for provider-independent
document processing operations.
"""

from __future__ import annotations


class DocumentError(Exception):
    """Base exception for all document-related errors."""


class DocumentValidationError(DocumentError):
    """Raised when document input validation fails."""


class UnsupportedDocumentFormatError(DocumentValidationError):
    """Raised when an unsupported document format is provided."""


class UnsupportedLanguageError(DocumentValidationError):
    """Raised when an unsupported language is specified."""


class DocumentProcessingError(DocumentError):
    """Base exception for document processing failures."""


class DocumentParsingError(DocumentProcessingError):
    """Raised when document parsing fails."""


class DocumentClassificationError(DocumentProcessingError):
    """Raised when document classification fails."""


class DocumentSummarizationError(DocumentProcessingError):
    """Raised when document summarization fails."""


class DocumentExtractionError(DocumentProcessingError):
    """Raised when document information extraction fails."""


class DocumentMetadataError(DocumentProcessingError):
    """Raised when document metadata extraction fails."""


class DocumentProviderError(DocumentError):
    """Raised when an underlying document provider returns an error."""