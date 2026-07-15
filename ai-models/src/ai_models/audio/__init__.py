"""
ai_models.audio

Framework-independent audio model utilities.

This module provides reusable constants, exceptions, and helper
operations for speech and audio models.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_models.audio.constants import (
    DEFAULT_AUDIO_MODEL,
    DEFAULT_AUDIO_PROVIDER,
    DEFAULT_AUDIO_RESPONSE_FORMAT,
    SUPPORTED_AUDIO_PROVIDERS,
)
from ai_models.audio.exceptions import (
    AudioConfigurationError,
    AudioError,
    AudioValidationError,
    InvalidAudioProviderError,
)
from ai_models.audio.operations import (
    build_audio_id,
    is_supported_audio_provider,
    normalize_audio_provider,
    validate_audio_id,
    validate_audio_provider,
)

__all__ = [
    "DEFAULT_AUDIO_MODEL",
    "DEFAULT_AUDIO_PROVIDER",
    "DEFAULT_AUDIO_RESPONSE_FORMAT",
    "SUPPORTED_AUDIO_PROVIDERS",
    "AudioError",
    "InvalidAudioProviderError",
    "AudioConfigurationError",
    "AudioValidationError",
    "build_audio_id",
    "is_supported_audio_provider",
    "normalize_audio_provider",
    "validate_audio_id",
    "validate_audio_provider",
]