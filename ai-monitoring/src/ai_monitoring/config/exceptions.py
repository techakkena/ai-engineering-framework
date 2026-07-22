"""
Exceptions for ai_monitoring.config.
"""

from __future__ import annotations


class MonitoringConfigError(Exception):
    """Base exception for monitoring configuration errors."""


class ConfigValidationError(MonitoringConfigError):
    """Raised when configuration validation fails."""


class ConfigNotFoundError(MonitoringConfigError):
    """Raised when a configuration cannot be found."""


class ConfigLoadError(MonitoringConfigError):
    """Raised when loading configuration fails."""


class ConfigUpdateError(MonitoringConfigError):
    """Raised when updating configuration fails."""


class ConfigExportError(MonitoringConfigError):
    """Raised when exporting configuration fails."""


class ConfigProviderError(MonitoringConfigError):
    """Raised when a configuration provider fails."""