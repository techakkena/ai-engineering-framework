"""
Exceptions for the ai_monitoring.reporting package.
"""

from __future__ import annotations


class ReportingError(Exception):
    """Base exception for reporting errors."""


class ReportValidationError(ReportingError):
    """Raised when report validation fails."""


class ReportNotFoundError(ReportingError):
    """Raised when a report cannot be found."""


class ReportGenerationError(ReportingError):
    """Raised when report generation fails."""


class ReportingConfigurationError(ReportingError):
    """Raised when reporting configuration is invalid."""


class ReportingProviderError(ReportingError):
    """Raised when an underlying reporting provider fails."""