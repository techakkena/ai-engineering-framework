"""
Exceptions for the ai_datasets.config package.
"""

from __future__ import annotations


class DatasetConfigError(Exception):
    """Base exception for dataset configuration errors."""


class ConfigValidationError(DatasetConfigError):
    """Raised when configuration validation fails."""


class ConfigNotFoundError(DatasetConfigError):
    """Raised when a configuration cannot be found."""


class ConfigLoadError(DatasetConfigError):
    """Raised when configuration loading fails."""


class ConfigUpdateError(DatasetConfigError):
    """Raised when configuration update fails."""


class ConfigExportError(DatasetConfigError):
    """Raised when configuration export fails."""


class ConfigProviderError(DatasetConfigError):
    """Raised when an underlying configuration provider fails."""