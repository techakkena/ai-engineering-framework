"""
Tests for ai_integrations.aws_provider.exceptions.
"""

from ai_integrations.aws_provider.exceptions import (
    AWSAuthenticationError,
    AWSConfigurationError,
    AWSConnectionError,
    AWSError,
    AWSModelError,
    AWSProviderError,
    AWSRateLimitError,
    AWSRequestError,
    AWSResponseError,
    AWSTimeoutError,
)


def test_aws_error() -> None:
    """AWSError should derive from Exception."""
    error = AWSError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    """Configuration error should derive from AWSError."""
    assert isinstance(
        AWSConfigurationError("config"),
        AWSError,
    )


def test_authentication_error() -> None:
    """Authentication error should derive from AWSError."""
    assert isinstance(
        AWSAuthenticationError("auth"),
        AWSError,
    )


def test_rate_limit_error() -> None:
    """Rate limit error should derive from AWSError."""
    assert isinstance(
        AWSRateLimitError("rate"),
        AWSError,
    )


def test_connection_error() -> None:
    """Connection error should derive from AWSError."""
    assert isinstance(
        AWSConnectionError("connection"),
        AWSError,
    )


def test_timeout_error() -> None:
    """Timeout error should derive from AWSError."""
    assert isinstance(
        AWSTimeoutError("timeout"),
        AWSError,
    )


def test_model_error() -> None:
    """Model error should derive from AWSError."""
    assert isinstance(
        AWSModelError("model"),
        AWSError,
    )


def test_request_error() -> None:
    """Request error should derive from AWSError."""
    assert isinstance(
        AWSRequestError("request"),
        AWSError,
    )


def test_response_error() -> None:
    """Response error should derive from AWSError."""
    assert isinstance(
        AWSResponseError("response"),
        AWSError,
    )


def test_provider_error() -> None:
    """Provider error should derive from AWSError."""
    assert isinstance(
        AWSProviderError("provider"),
        AWSError,
    )