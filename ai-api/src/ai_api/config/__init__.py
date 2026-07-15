"""
ai_api.config

Framework-independent configuration utilities for the AI API package.

This module provides reusable configuration constants, exceptions,
and helper operations for managing API configuration.

The module is intentionally framework-independent and can be
integrated with FastAPI, Starlette, Quart, Litestar, Flask,
Django, or any future API framework.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_api.config.constants import (
    DEFAULT_API_PREFIX,
    DEFAULT_API_VERSION,
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFAULT_TIMEOUT,
    SUPPORTED_ENVIRONMENTS,
)
from ai_api.config.exceptions import (
    ConfigError,
    InvalidConfigurationError,
    InvalidEnvironmentError,
    MissingConfigurationError,
    UnsupportedConfigurationError,
)
from ai_api.config.operations import (
    build_api_url,
    is_supported_environment,
    normalize_environment,
    validate_configuration_key,
    validate_environment,
)

__all__ = [
    # Constants
    "DEFAULT_API_PREFIX",
    "DEFAULT_API_VERSION",
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_TIMEOUT",
    "SUPPORTED_ENVIRONMENTS",
    # Exceptions
    "ConfigError",
    "InvalidConfigurationError",
    "InvalidEnvironmentError",
    "MissingConfigurationError",
    "UnsupportedConfigurationError",
    # Operations
    "build_api_url",
    "is_supported_environment",
    "normalize_environment",
    "validate_configuration_key",
    "validate_environment",
]