"""
Unit tests for ai_models.tokenizer.exceptions.
"""

from __future__ import annotations

import pytest

from ai_models.tokenizer.exceptions import (
    InvalidTokenizerProviderError,
    TokenizerConfigurationError,
    TokenizerError,
    TokenizerValidationError,
)


def test_tokenizer_error_default_message() -> None:
    """Test TokenizerError default message."""
    error = TokenizerError()

    assert (
        str(error)
        == "A tokenizer error occurred."
    )


def test_tokenizer_error_custom_message() -> None:
    """Test TokenizerError custom message."""
    error = TokenizerError(
        "Custom tokenizer error.",
    )

    assert (
        str(error)
        == "Custom tokenizer error."
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "bedrock",
        "vertex",
    ],
)
def test_invalid_tokenizer_provider_error(
    provider: str,
) -> None:
    """Test InvalidTokenizerProviderError."""
    error = InvalidTokenizerProviderError(
        provider,
    )

    assert isinstance(
        error,
        TokenizerError,
    )

    assert error.provider == provider

    assert (
        str(error)
        == (
            "Invalid tokenizer provider: "
            f"'{provider}'."
        )
    )


def test_tokenizer_configuration_error() -> None:
    """Test TokenizerConfigurationError."""
    configuration = "context_window"

    error = TokenizerConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        TokenizerError,
    )

    assert (
        error.configuration
        == configuration
    )

    assert (
        str(error)
        == (
            "Invalid tokenizer "
            "configuration: "
            f"'{configuration}'."
        )
    )


def test_tokenizer_validation_error() -> None:
    """Test TokenizerValidationError."""
    tokenizer = "cl100k_base"
    reason = "unsupported encoding"

    error = TokenizerValidationError(
        tokenizer,
        reason,
    )

    assert isinstance(
        error,
        TokenizerError,
    )

    assert error.tokenizer == tokenizer
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Tokenizer '{tokenizer}' "
            f"validation failed: "
            f"{reason}."
        )
    )