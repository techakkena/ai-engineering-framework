"""
Exceptions for ai_monitoring.utils.
"""

from __future__ import annotations


class MonitoringUtilsError(Exception):
    """Base exception for monitoring utility errors."""


class IdentifierValidationError(MonitoringUtilsError):
    """Raised when an identifier is invalid."""


class MetadataBuildError(MonitoringUtilsError):
    """Raised when metadata creation fails."""


class TimestampFormatError(MonitoringUtilsError):
    """Raised when timestamp formatting fails."""


class DurationFormatError(MonitoringUtilsError):
    """Raised when duration formatting fails."""


class MonitoringUtilsConfigurationError(MonitoringUtilsError):
    """Raised when utility configuration is invalid."""