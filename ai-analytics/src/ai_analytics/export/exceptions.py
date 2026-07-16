"""Exceptions for the ai_analytics.export module."""

from __future__ import annotations


class ExportError(Exception):
    """Base exception for export operations."""


class ExportValidationError(ExportError):
    """Raised when export validation fails."""


class ExportRegistrationError(ExportError):
    """Raised when export registration fails."""


class ExportNotFoundError(ExportRegistrationError):
    """Raised when an export definition cannot be found."""


class DuplicateExportError(ExportRegistrationError):
    """Raised when attempting to register a duplicate export."""


class UnsupportedExportFormatError(
    ExportValidationError,
):
    """Raised when an unsupported export format is supplied."""


__all__ = [
    "DuplicateExportError",
    "ExportError",
    "ExportNotFoundError",
    "ExportRegistrationError",
    "ExportValidationError",
    "UnsupportedExportFormatError",
]