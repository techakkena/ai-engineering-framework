"""Exceptions for the ai_docs.documentation module."""

from __future__ import annotations


class DocumentationError(Exception):
    """Base exception for documentation operations."""


class DocumentationValidationError(
    DocumentationError,
):
    """Raised when documentation validation fails."""


class DocumentationRegistrationError(
    DocumentationError,
):
    """Raised when documentation registration fails."""


class DocumentationNotFoundError(
    DocumentationRegistrationError,
):
    """Raised when a documentation definition cannot be found."""


class DuplicateDocumentationError(
    DocumentationRegistrationError,
):
    """Raised when attempting to register a duplicate documentation."""


class UnsupportedDocumentationTypeError(
    DocumentationValidationError,
):
    """Raised when an unsupported documentation type is specified."""


__all__ = [
    "DocumentationError",
    "DocumentationValidationError",
    "DocumentationRegistrationError",
    "DocumentationNotFoundError",
    "DuplicateDocumentationError",
    "UnsupportedDocumentationTypeError",
]