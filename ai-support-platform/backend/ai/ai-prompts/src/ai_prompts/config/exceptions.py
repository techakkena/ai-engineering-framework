from __future__ import annotations

"""Configuration exceptions."""


class ConfigError(Exception):
    """Base configuration exception."""


class InvalidConfigurationError(ConfigError):
    """Raised when configuration is invalid."""


class MissingConfigurationError(ConfigError):
    """Raised when configuration is missing."""


__all__ = [
    "ConfigError",
    "InvalidConfigurationError",
    "MissingConfigurationError",
]
