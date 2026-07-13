"""Exceptions for the ai_memory.config module."""

from __future__ import annotations


class ConfigError(Exception):
    """Base exception for configuration operations."""


class ConfigNotFoundError(ConfigError):
    """Raised when a configuration cannot be found."""


class ConfigValidationError(ConfigError):
    """Raised when configuration validation fails."""


class ConfigFormatError(ConfigError):
    """Raised when an unsupported configuration format is used."""