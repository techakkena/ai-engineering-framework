"""
Unit tests for ai_models.audio.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_models.audio.exceptions import (
    InvalidAudioProviderError,
)
from ai_models.audio.operations import (
    build_audio_id,
    is_supported_audio_provider,
    normalize_audio_provider,
    validate_audio_id,
    validate_audio_provider,
)


# ============================================================================
# normalize_audio_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("OPENAI", "openai"),
        (" ElevenLabs ", "elevenlabs"),
        ("Google", "google"),
        ("Azure", "azure"),
    ],
)
def test_normalize_audio_provider(
    provider: str,
    expected: str,
) -> None:
    """Test provider normalization."""
    assert (
        normalize_audio_provider(provider)
        == expected
    )


# ============================================================================
# validate_audio_provider
# ============================================================================


@pytest.mark.parametrize(
    "provider",
    [
        "openai",
        "elevenlabs",
        "assemblyai",
        "deepgram",
        "google",
        "azure",
    ],
)
def test_validate_audio_provider(
    provider: str,
) -> None:
    """Test valid providers."""
    assert (
        validate_audio_provider(provider)
        == provider
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "aws",
        "bedrock",
        "vertex",
    ],
)
def test_validate_audio_provider_invalid(
    provider: str,
) -> None:
    """Invalid providers should raise."""
    with pytest.raises(
        InvalidAudioProviderError,
    ):
        validate_audio_provider(provider)


# ============================================================================
# is_supported_audio_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("openai", True),
        ("elevenlabs", True),
        ("assemblyai", True),
        ("deepgram", True),
        ("google", True),
        ("azure", True),
        ("aws", False),
        ("bedrock", False),
    ],
)
def test_is_supported_audio_provider(
    provider: str,
    expected: bool,
) -> None:
    """Test provider support detection."""
    assert (
        is_supported_audio_provider(provider)
        is expected
    )


# ============================================================================
# validate_audio_id
# ============================================================================


@pytest.mark.parametrize(
    "audio_id",
    [
        "audio",
        "audio_01",
        "audio-01",
        "runtime123",
    ],
)
def test_validate_audio_id(
    audio_id: str,
) -> None:
    """Test valid audio identifiers."""
    assert (
        validate_audio_id(audio_id)
        == audio_id.lower()
    )


@pytest.mark.parametrize(
    "audio_id",
    [
        "",
        "123audio",
        "audio name",
        "@audio",
    ],
)
def test_validate_audio_id_invalid(
    audio_id: str,
) -> None:
    """Invalid identifiers should raise."""
    with pytest.raises(ValueError):
        validate_audio_id(audio_id)


# ============================================================================
# build_audio_id
# ============================================================================


def test_build_audio_id() -> None:
    """Test audio ID generation."""
    audio_id = build_audio_id()

    assert audio_id.startswith("audio-")

    pattern = re.compile(
        (
            r"^audio-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(audio_id) is not None