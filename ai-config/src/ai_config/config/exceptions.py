"""
Custom exceptions for the config module.

Author: TECHAKKENA
"""


class ConfigError(Exception):
    """Base exception for configuration."""


class ConfigNotLoadedError(ConfigError):
    """Raised when configuration has not been loaded."""


class ConfigKeyError(ConfigError):
    """Raised when a configuration key does not exist."""
