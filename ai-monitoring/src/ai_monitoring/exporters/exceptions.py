"""
Exceptions for the ai_monitoring.exporters package.
"""

from __future__ import annotations


class ExporterError(Exception):
    """Base exception for exporter errors."""


class ExporterValidationError(ExporterError):
    """Raised when exporter validation fails."""


class ExporterNotFoundError(ExporterError):
    """Raised when an exporter cannot be found."""


class ExportOperationError(ExporterError):
    """Raised when exporting fails."""


class ExporterConfigurationError(ExporterError):
    """Raised when exporter configuration is invalid."""


class ExporterProviderError(ExporterError):
    """Raised when an exporter provider fails."""