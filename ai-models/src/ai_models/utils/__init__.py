"""
ai_models.utils

Framework-independent utility functions for AI models.

This module provides reusable constants, exceptions, and helper
operations shared across all AI model components.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_models.utils.constants import (
    DEFAULT_ENCODING,
    DEFAULT_UUID_PREFIX,
    DEFAULT_VERSION,
    SUPPORTED_ENCODINGS,
)
from ai_models.utils.exceptions import (
    InvalidEncodingError,
    UtilityConfigurationError,
    UtilityError,
    UtilityValidationError,
)
from ai_models.utils.operations import (
    build_model_uuid,
    is_supported_encoding,
    normalize_encoding,
    validate_encoding,
    validate_model_name,
)

__all__ = [
    # Constants
    "DEFAULT_ENCODING",
    "DEFAULT_UUID_PREFIX",
    "DEFAULT_VERSION",
    "SUPPORTED_ENCODINGS",
    # Exceptions
    "UtilityError",
    "InvalidEncodingError",
    "UtilityConfigurationError",
    "UtilityValidationError",
    # Operations
    "build_model_uuid",
    "is_supported_encoding",
    "normalize_encoding",
    "validate_encoding",
    "validate_model_name",
]