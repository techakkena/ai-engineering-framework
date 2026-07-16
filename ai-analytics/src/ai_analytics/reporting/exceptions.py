"""Exceptions for the ai_analytics.reporting module."""

from __future__ import annotations


class ReportError(Exception):
    """Base exception for reporting operations."""


class ReportValidationError(ReportError):
    """Raised when report validation fails."""


class ReportRegistrationError(ReportError):
    """Raised when report registration fails."""


class ReportNotFoundError(ReportRegistrationError):
    """Raised when a report cannot be found."""


class DuplicateReportError(ReportRegistrationError):
    """Raised when attempting to register a duplicate report."""


class UnsupportedReportFormatError(
    ReportValidationError,
):
    """Raised when an unsupported report format is supplied."""


__all__ = [
    "DuplicateReportError",
    "ReportError",
    "ReportNotFoundError",
    "ReportRegistrationError",
    "ReportValidationError",
    "UnsupportedReportFormatError",
]