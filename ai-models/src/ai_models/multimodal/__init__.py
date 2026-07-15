"""
ai_models.multimodal

Framework-independent multimodal model utilities.

This module provides reusable constants, exceptions, and helper
operations for multimodal AI models.

Multimodal models combine multiple input and output modalities such
as text, images, audio, video, and documents through a unified
interface.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_models.multimodal.constants import (
    DEFAULT_MAX_MODALITIES,
    DEFAULT_MULTIMODAL_MODEL,
    DEFAULT_MULTIMODAL_PROVIDER,
    DEFAULT_PRIMARY_MODALITY,
    SUPPORTED_INPUT_MODALITIES,
    SUPPORTED_MULTIMODAL_PROVIDERS,
    SUPPORTED_OUTPUT_MODALITIES,
)
from ai_models.multimodal.exceptions import (
    InvalidMultimodalProviderError,
    MultimodalConfigurationError,
    MultimodalError,
    MultimodalValidationError,
)
from ai_models.multimodal.operations import (
    build_multimodal_id,
    is_supported_multimodal_provider,
    normalize_multimodal_provider,
    validate_multimodal_id,
    validate_multimodal_provider,
)

__all__ = [
    # Constants
    "DEFAULT_MAX_MODALITIES",
    "DEFAULT_MULTIMODAL_MODEL",
    "DEFAULT_MULTIMODAL_PROVIDER",
    "DEFAULT_PRIMARY_MODALITY",
    "SUPPORTED_INPUT_MODALITIES",
    "SUPPORTED_MULTIMODAL_PROVIDERS",
    "SUPPORTED_OUTPUT_MODALITIES",
    # Exceptions
    "MultimodalError",
    "InvalidMultimodalProviderError",
    "MultimodalConfigurationError",
    "MultimodalValidationError",
    # Operations
    "build_multimodal_id",
    "is_supported_multimodal_provider",
    "normalize_multimodal_provider",
    "validate_multimodal_id",
    "validate_multimodal_provider",
]