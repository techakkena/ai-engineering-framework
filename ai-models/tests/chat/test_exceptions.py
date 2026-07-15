"""
Unit tests for ai_models.chat.exceptions.
"""

from __future__ import annotations

import pytest

from ai_models.chat.exceptions import (
    ChatConfigurationError,
    ChatError,
    ChatValidationError,
    InvalidChatProviderError,
)


def test_chat_error_default_message() -> None:
    """Test ChatError default message."""
    error = ChatError()

    assert str(error) == "A chat error occurred."


def test_chat_error_custom_message() -> None:
    """Test ChatError custom message."""
    error = ChatError(
        "Custom chat error.",
    )

    assert str(error) == "Custom chat error."


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "azure",
        "bedrock",
    ],
)
def test_invalid_chat_provider_error(
    provider: str,
) -> None:
    """Test InvalidChatProviderError."""
    error = InvalidChatProviderError(
        provider,
    )

    assert isinstance(error, ChatError)
    assert error.provider == provider

    assert (
        str(error)
        == f"Invalid chat provider: '{provider}'."
    )


def test_chat_configuration_error() -> None:
    """Test ChatConfigurationError."""
    configuration = "temperature"

    error = ChatConfigurationError(
        configuration,
    )

    assert isinstance(error, ChatError)
    assert error.configuration == configuration

    assert (
        str(error)
        == (
            "Invalid chat configuration: "
            f"'{configuration}'."
        )
    )


def test_chat_validation_error() -> None:
    """Test ChatValidationError."""
    model = "gpt-5"
    reason = "context window exceeded"

    error = ChatValidationError(
        model,
        reason,
    )

    assert isinstance(error, ChatError)
    assert error.model == model
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Chat model '{model}' "
            f"validation failed: {reason}."
        )
    )