"""
Operations for ai_models.audio.
"""

from __future__ import annotations

import re
import uuid

from ai_models.audio.constants import (
    SUPPORTED_AUDIO_PROVIDERS,
)
from ai_models.audio.exceptions import (
    InvalidAudioProviderError,
)


def normalize_audio_provider(
    provider: str,
) -> str:
    """
    Normalize an audio provider.
    """
    return provider.strip().lower()


def validate_audio_provider(
    provider: str,
) -> str:
    """
    Validate an audio provider.
    """
    normalized = normalize_audio_provider(
        provider,
    )

    if (
        normalized
        not in SUPPORTED_AUDIO_PROVIDERS
    ):
        raise InvalidAudioProviderError(
            provider,
        )

    return normalized


def is_supported_audio_provider(
    provider: str,
) -> bool:
    """
    Determine whether an audio provider is supported.
    """
    return (
        normalize_audio_provider(
            provider,
        )
        in SUPPORTED_AUDIO_PROVIDERS
    )


def validate_audio_id(
    audio_id: str,
) -> str:
    """
    Validate an audio identifier.
    """
    normalized = audio_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid audio identifier: '{audio_id}'."
        )

    return normalized


def build_audio_id() -> str:
    """
    Build a unique audio identifier.
    """
    return f"audio-{uuid.uuid4()}"