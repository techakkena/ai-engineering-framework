"""
ai_models.vision

Framework-independent vision model utilities.

This module provides reusable constants, exceptions, and helper
operations for vision models.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_models.vision.constants import (
    DEFAULT_IMAGE_DETAIL,
    DEFAULT_VISION_MODEL,
    DEFAULT_VISION_PROVIDER,
    SUPPORTED_VISION_PROVIDERS,
)
from ai_models.vision.exceptions import (
    InvalidVisionProviderError,
    VisionConfigurationError,
    VisionError,
    VisionValidationError,
)
from ai_models.vision.operations import (
    build_vision_id,
    is_supported_vision_provider,
    normalize_vision_provider,
    validate_vision_id,
    validate_vision_provider,
)

__all__ = [
    "DEFAULT_IMAGE_DETAIL",
    "DEFAULT_VISION_MODEL",
    "DEFAULT_VISION_PROVIDER",
    "SUPPORTED_VISION_PROVIDERS",
    "VisionError",
    "InvalidVisionProviderError",
    "VisionConfigurationError",
    "VisionValidationError",
    "build_vision_id",
    "is_supported_vision_provider",
    "normalize_vision_provider",
    "validate_vision_id",
    "validate_vision_provider",
]