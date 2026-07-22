"""
Exceptions for the ai_monitoring.telemetry package.
"""

from __future__ import annotations


class TelemetryError(Exception):
    """Base exception for telemetry errors."""


class TelemetryValidationError(TelemetryError):
    """Raised when telemetry validation fails."""


class TelemetryNotFoundError(TelemetryError):
    """Raised when telemetry cannot be found."""


class TelemetryCollectionError(TelemetryError):
    """Raised when telemetry collection fails."""


class TelemetryExportError(TelemetryError):
    """Raised when telemetry export fails."""


class TelemetryConfigurationError(TelemetryError):
    """Raised when telemetry configuration is invalid."""


class TelemetryProviderError(TelemetryError):
    """Raised when an underlying telemetry provider fails."""