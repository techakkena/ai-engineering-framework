"""
Tests for ai_integrations.mistral_provider.exceptions.
"""

from ai_integrations.mistral_provider.exceptions import (
    MistralAuthenticationError,
    MistralConfigurationError,
    MistralConnectionError,
    MistralError,
    MistralModelError,
    MistralProviderError,
    MistralRateLimitError,
    MistralRequestError,
    MistralResponseError,
    MistralTimeoutError,
)


def test_mistral_error() -> None:
    """MistralError should derive from Exception."""
    error = MistralError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    """Configuration error should derive from MistralError."""
    assert isinstance(
        MistralConfigurationError("config"),
        MistralError,
    )


def test_authentication_error() -> None:
    """Authentication error should derive from MistralError."""
    assert isinstance(
        MistralAuthenticationError("auth"),
        MistralError,
    )


def test_rate_limit_error() -> None:
    """Rate limit error should derive from MistralError."""
    assert isinstance(
        MistralRateLimitError("rate"),
        MistralError,
    )


def test_connection_error() -> None:
    """Connection error should derive from MistralError."""
    assert isinstance(
        MistralConnectionError("connection"),
        MistralError,
    )


def test_timeout_error() -> None:
    """Timeout error should derive from MistralError."""
    assert isinstance(
        MistralTimeoutError("timeout"),
        MistralError,
    )


def test_model_error() -> None:
    """Model error should derive from MistralError."""
    assert isinstance(
        MistralModelError("model"),
        MistralError,
    )


def test_request_error() -> None:
    """Request error should derive from MistralError."""
    assert isinstance(
        MistralRequestError("request"),
        MistralError,
    )


def test_response_error() -> None:
    """Response error should derive from MistralError."""
    assert isinstance(
        MistralResponseError("response"),
        MistralError,
    )


def test_provider_error() -> None:
    """Provider error should derive from MistralError."""
    assert isinstance(
        MistralProviderError("provider"),
        MistralError,
    )