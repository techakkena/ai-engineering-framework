"""Exceptions for the ai_docs.exporters module."""

from __future__ import annotations


class ExportError(Exception):
    """Base exception for exporter operations."""


class ExportValidationError(ExportError):
    """Raised when exporter validation fails."""


class ExportRegistrationError(ExportError):
    """Raised when exporter registration fails."""


class ExportNotFoundError(
    ExportRegistrationError,
):
    """Raised when an exporter cannot be found."""


class DuplicateExportError(
    ExportRegistrationError,
):
    """Raised when attempting to register a duplicate exporter."""


class UnsupportedExportFormatError(
    ExportValidationError,
):
    """Raised when an unsupported export format is specified."""


__all__ = [
    "DuplicateExportError",
    "ExportError",
    "ExportNotFoundError",
    "ExportRegistrationError",
    "ExportValidationError",
    "UnsupportedExportFormatError",
]