"""Exceptions for the ai_cloud.monitoring module."""

from __future__ import annotations


class MonitoringError(Exception):
    """Base exception for monitoring operations."""


class MonitoringValidationError(MonitoringError):
    """Raised when monitoring validation fails."""


class MonitoringRegistrationError(MonitoringError):
    """Raised when monitoring registration fails."""


class MonitoringNotFoundError(
    MonitoringRegistrationError,
):
    """Raised when a monitor cannot be found."""


class DuplicateMonitoringError(
    MonitoringRegistrationError,
):
    """Raised when attempting to register a duplicate monitor."""


class UnsupportedMonitorTypeError(
    MonitoringValidationError,
):
    """Raised when an unsupported monitor type is specified."""


__all__ = [
    "DuplicateMonitoringError",
    "MonitoringError",
    "MonitoringNotFoundError",
    "MonitoringRegistrationError",
    "MonitoringValidationError",
    "UnsupportedMonitorTypeError",
]