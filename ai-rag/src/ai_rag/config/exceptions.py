"""Exceptions for ai-rag configuration."""


class ConfigError(Exception):
    """Base configuration exception."""


class InvalidConfigError(ConfigError):
    """Raised when configuration is invalid."""


class MissingConfigError(ConfigError):
    """Raised when required configuration is missing."""