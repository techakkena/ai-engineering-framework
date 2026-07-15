"""
Tests for ai_integrations.anthropic_provider.exceptions.
"""

from ai_integrations.anthropic_provider.exceptions import (
    AnthropicAuthenticationError,
    AnthropicConfigurationError,
    AnthropicConnectionError,
    AnthropicError,
    AnthropicModelError,
    AnthropicProviderError,
    AnthropicRateLimitError,
    AnthropicRequestError,
    AnthropicResponseError,
    AnthropicTimeoutError,
)


def test_anthropic_error() -> None:
    """AnthropicError should derive from Exception."""
    error = AnthropicError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    """Configuration error should derive from AnthropicError."""
    assert isinstance(
        AnthropicConfigurationError("config"),
        AnthropicError,
    )


def test_authentication_error() -> None:
    """Authentication error should derive from AnthropicError."""
    assert isinstance(
        AnthropicAuthenticationError("auth"),
        AnthropicError,
    )


def test_rate_limit_error() -> None:
    """Rate limit error should derive from AnthropicError."""
    assert isinstance(
        AnthropicRateLimitError("rate"),
        AnthropicError,
    )


def test_connection_error() -> None:
    """Connection error should derive from AnthropicError."""
    assert isinstance(
        AnthropicConnectionError("connection"),
        AnthropicError,
    )


def test_timeout_error() -> None:
    """Timeout error should derive from AnthropicError."""
    assert isinstance(
        AnthropicTimeoutError("timeout"),
        AnthropicError,
    )


def test_model_error() -> None:
    """Model error should derive from AnthropicError."""
    assert isinstance(
        AnthropicModelError("model"),
        AnthropicError,
    )


def test_request_error() -> None:
    """Request error should derive from AnthropicError."""
    assert isinstance(
        AnthropicRequestError("request"),
        AnthropicError,
    )


def test_response_error() -> None:
    """Response error should derive from AnthropicError."""
    assert isinstance(
        AnthropicResponseError("response"),
        AnthropicError,
    )


def test_provider_error() -> None:
    """Provider error should derive from AnthropicError."""
    assert isinstance(
        AnthropicProviderError("provider"),
        AnthropicError,
    )