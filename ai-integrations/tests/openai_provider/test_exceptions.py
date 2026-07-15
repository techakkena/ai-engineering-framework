"""
Tests for ai_integrations.openai_provider.exceptions.
"""

from ai_integrations.openai_provider.exceptions import (
    OpenAIAuthenticationError,
    OpenAIConfigurationError,
    OpenAIConnectionError,
    OpenAIError,
    OpenAIModelError,
    OpenAIProviderError,
    OpenAIRateLimitError,
    OpenAIRequestError,
    OpenAIResponseError,
    OpenAITimeoutError,
)


def test_openai_error() -> None:
    """OpenAIError should derive from Exception."""
    error = OpenAIError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    """OpenAIConfigurationError should derive from OpenAIError."""
    error = OpenAIConfigurationError("configuration")

    assert isinstance(error, OpenAIError)


def test_authentication_error() -> None:
    """OpenAIAuthenticationError should derive from OpenAIError."""
    error = OpenAIAuthenticationError("authentication")

    assert isinstance(error, OpenAIError)


def test_rate_limit_error() -> None:
    """OpenAIRateLimitError should derive from OpenAIError."""
    error = OpenAIRateLimitError("rate limit")

    assert isinstance(error, OpenAIError)


def test_connection_error() -> None:
    """OpenAIConnectionError should derive from OpenAIError."""
    error = OpenAIConnectionError("connection")

    assert isinstance(error, OpenAIError)


def test_timeout_error() -> None:
    """OpenAITimeoutError should derive from OpenAIError."""
    error = OpenAITimeoutError("timeout")

    assert isinstance(error, OpenAIError)


def test_model_error() -> None:
    """OpenAIModelError should derive from OpenAIError."""
    error = OpenAIModelError("model")

    assert isinstance(error, OpenAIError)


def test_request_error() -> None:
    """OpenAIRequestError should derive from OpenAIError."""
    error = OpenAIRequestError("request")

    assert isinstance(error, OpenAIError)


def test_response_error() -> None:
    """OpenAIResponseError should derive from OpenAIError."""
    error = OpenAIResponseError("response")

    assert isinstance(error, OpenAIError)


def test_provider_error() -> None:
    """OpenAIProviderError should derive from OpenAIError."""
    error = OpenAIProviderError("provider")

    assert isinstance(error, OpenAIError)