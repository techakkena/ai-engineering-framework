"""
Exceptions for the ai_security.config module.
"""

from __future__ import annotations


class ConfigurationError(Exception):
    """Base exception for configuration operations."""


class ConfigurationValidationError(ConfigurationError):
    """Raised when configuration validation fails."""


class MissingConfigurationError(ConfigurationError):
    """Raised when a required configuration value is missing."""