"""
Unit tests for ai_models.audio.exceptions.
"""

from __future__ import annotations

import pytest

from ai_models.audio.exceptions import (
    AudioConfigurationError,
    AudioError,
    AudioValidationError,
    InvalidAudioProviderError,
)


def test_audio_error_default_message() -> None:
    """Test AudioError."""
    error = AudioError()

    assert str(error) == "An audio error occurred."


def test_audio_error_custom_message() -> None:
    """Test AudioError custom message."""
    error = AudioError(
        "Custom audio error.",
    )

    assert str(error) == "Custom audio error."


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "aws",
        "bedrock",
    ],
)
def test_invalid_audio_provider_error(
    provider: str,
) -> None:
    """Test InvalidAudioProviderError."""
    error = InvalidAudioProviderError(
        provider,
    )

    assert isinstance(
        error,
        AudioError,
    )

    assert error.provider == provider

    assert (
        str(error)
        == (
            f"Invalid audio provider: "
            f"'{provider}'."
        )
    )


def test_audio_configuration_error() -> None:
    """Test AudioConfigurationError."""
    configuration = "sample_rate"

    error = AudioConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        AudioError,
    )

    assert (
        error.configuration
        == configuration
    )

    assert (
        str(error)
        == (
            "Invalid audio configuration: "
            f"'{configuration}'."
        )
    )


def test_audio_validation_error() -> None:
    """Test AudioValidationError."""
    model = "gpt-4o-mini-transcribe"
    reason = "unsupported language"

    error = AudioValidationError(
        model,
        reason,
    )

    assert isinstance(
        error,
        AudioError,
    )

    assert error.model == model
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Audio model '{model}' "
            f"validation failed: {reason}."
        )
    )