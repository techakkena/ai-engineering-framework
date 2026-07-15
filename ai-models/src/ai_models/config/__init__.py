"""
ai_models.config

Framework-independent model configuration utilities.

This module provides reusable constants, exceptions, and helper
operations for configuring AI models across multiple providers.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_models.config.constants import (
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL_CONFIG_NAME,
    DEFAULT_TEMPERATURE,
    SUPPORTED_ENVIRONMENTS,
)
from ai_models.config.exceptions import (
    ConfigurationValidationError,
    InvalidEnvironmentError,
    ModelConfigurationError,
    ModelConfigError,
)
from ai_models.config.operations import (
    build_configuration_id,
    is_supported_environment,
    normalize_environment,
    validate_configuration_id,
    validate_environment,
)

__all__ = [
    # Constants
    "DEFAULT_MAX_TOKENS",
    "DEFAULT_MODEL_CONFIG_NAME",
    "DEFAULT_TEMPERATURE",
    "SUPPORTED_ENVIRONMENTS",
    # Exceptions
    "ModelConfigError",
    "InvalidEnvironmentError",
    "ModelConfigurationError",
    "ConfigurationValidationError",
    # Operations
    "build_configuration_id",
    "is_supported_environment",
    "normalize_environment",
    "validate_configuration_id",
    "validate_environment",
]