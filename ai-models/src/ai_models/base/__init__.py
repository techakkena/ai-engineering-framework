"""
ai_models.base

Framework-independent model base utilities.

This module provides reusable constants, exceptions, and helper
operations for AI model abstractions.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_models.base.constants import (
    DEFAULT_MODEL_NAME,
    DEFAULT_MODEL_PROVIDER,
    DEFAULT_MODEL_TYPE,
    SUPPORTED_MODEL_TYPES,
)
from ai_models.base.exceptions import (
    BaseModelError,
    InvalidModelTypeError,
    ModelConfigurationError,
    ModelValidationError,
)
from ai_models.base.operations import (
    build_model_id,
    is_supported_model_type,
    normalize_model_type,
    validate_model_id,
    validate_model_type,
)

__all__ = [
    # Constants
    "DEFAULT_MODEL_NAME",
    "DEFAULT_MODEL_PROVIDER",
    "DEFAULT_MODEL_TYPE",
    "SUPPORTED_MODEL_TYPES",
    # Exceptions
    "BaseModelError",
    "InvalidModelTypeError",
    "ModelConfigurationError",
    "ModelValidationError",
    # Operations
    "build_model_id",
    "is_supported_model_type",
    "normalize_model_type",
    "validate_model_id",
    "validate_model_type",
]