"""
Unit tests for ai_models.vision.exceptions.
"""

from __future__ import annotations

import pytest

from ai_models.vision.exceptions import (
    InvalidVisionProviderError,
    VisionConfigurationError,
    VisionError,
    VisionValidationError,
)


def test_vision_error_default_message() -> None:
    """Test VisionError."""
    error = VisionError()

    assert str(error) == "A vision error occurred."


def test_vision_error_custom_message() -> None:
    """Test VisionError custom message."""
    error = VisionError(
        "Custom vision error.",
    )

    assert str(error) == "Custom vision error."


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "azure",
        "bedrock",
    ],
)
def test_invalid_vision_provider_error(
    provider: str,
) -> None:
    """Test InvalidVisionProviderError."""
    error = InvalidVisionProviderError(
        provider,
    )

    assert isinstance(
        error,
        VisionError,
    )

    assert error.provider == provider

    assert (
        str(error)
        == f"Invalid vision provider: '{provider}'."
    )


def test_vision_configuration_error() -> None:
    """Test VisionConfigurationError."""
    configuration = "image_detail"

    error = VisionConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        VisionError,
    )

    assert error.configuration == configuration

    assert (
        str(error)
        == (
            "Invalid vision configuration: "
            f"'{configuration}'."
        )
    )


def test_vision_validation_error() -> None:
    """Test VisionValidationError."""
    model = "gpt-5-vision"
    reason = "unsupported image format"

    error = VisionValidationError(
        model,
        reason,
    )

    assert isinstance(
        error,
        VisionError,
    )

    assert error.model == model
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Vision model '{model}' "
            f"validation failed: {reason}."
        )
    )