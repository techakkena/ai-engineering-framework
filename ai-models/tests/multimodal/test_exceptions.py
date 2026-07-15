"""
Unit tests for ai_models.multimodal.exceptions.
"""

from __future__ import annotations

import pytest

from ai_models.multimodal.exceptions import (
    InvalidMultimodalProviderError,
    MultimodalConfigurationError,
    MultimodalError,
    MultimodalValidationError,
)


def test_multimodal_error_default_message() -> None:
    """Test MultimodalError default message."""
    error = MultimodalError()

    assert (
        str(error)
        == "A multimodal error occurred."
    )


def test_multimodal_error_custom_message() -> None:
    """Test MultimodalError custom message."""
    error = MultimodalError(
        "Custom multimodal error.",
    )

    assert (
        str(error)
        == "Custom multimodal error."
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "bedrock",
        "vertex",
    ],
)
def test_invalid_multimodal_provider_error(
    provider: str,
) -> None:
    """Test InvalidMultimodalProviderError."""
    error = InvalidMultimodalProviderError(
        provider,
    )

    assert isinstance(
        error,
        MultimodalError,
    )

    assert error.provider == provider

    assert (
        str(error)
        == (
            "Invalid multimodal provider: "
            f"'{provider}'."
        )
    )


def test_multimodal_configuration_error() -> None:
    """Test MultimodalConfigurationError."""
    configuration = "max_modalities"

    error = MultimodalConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        MultimodalError,
    )

    assert (
        error.configuration
        == configuration
    )

    assert (
        str(error)
        == (
            "Invalid multimodal "
            "configuration: "
            f"'{configuration}'."
        )
    )


def test_multimodal_validation_error() -> None:
    """Test MultimodalValidationError."""
    model = "gpt-5"
    reason = (
        "unsupported input modality"
    )

    error = MultimodalValidationError(
        model,
        reason,
    )

    assert isinstance(
        error,
        MultimodalError,
    )

    assert error.model == model
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Multimodal model '{model}' "
            f"validation failed: "
            f"{reason}."
        )
    )