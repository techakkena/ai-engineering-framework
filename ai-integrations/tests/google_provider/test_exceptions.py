"""
Tests for ai_integrations.google_provider.exceptions.
"""

from ai_integrations.google_provider.exceptions import (
    GoogleAuthenticationError,
    GoogleConfigurationError,
    GoogleConnectionError,
    GoogleError,
    GoogleModelError,
    GoogleProviderError,
    GoogleRateLimitError,
    GoogleRequestError,
    GoogleResponseError,
    GoogleTimeoutError,
)


def test_google_error() -> None:
    """GoogleError should derive from Exception."""
    error = GoogleError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    """Configuration error should derive from GoogleError."""
    assert isinstance(
        GoogleConfigurationError("config"),
        GoogleError,
    )


def test_authentication_error() -> None:
    """Authentication error should derive from GoogleError."""
    assert isinstance(
        GoogleAuthenticationError("auth"),
        GoogleError,
    )


def test_rate_limit_error() -> None:
    """Rate limit error should derive from GoogleError."""
    assert isinstance(
        GoogleRateLimitError("rate"),
        GoogleError,
    )


def test_connection_error() -> None:
    """Connection error should derive from GoogleError."""
    assert isinstance(
        GoogleConnectionError("connection"),
        GoogleError,
    )


def test_timeout_error() -> None:
    """Timeout error should derive from GoogleError."""
    assert isinstance(
        GoogleTimeoutError("timeout"),
        GoogleError,
    )


def test_model_error() -> None:
    """Model error should derive from GoogleError."""
    assert isinstance(
        GoogleModelError("model"),
        GoogleError,
    )


def test_request_error() -> None:
    """Request error should derive from GoogleError."""
    assert isinstance(
        GoogleRequestError("request"),
        GoogleError,
    )


def test_response_error() -> None:
    """Response error should derive from GoogleError."""
    assert isinstance(
        GoogleResponseError("response"),
        GoogleError,
    )


def test_provider_error() -> None:
    """Provider error should derive from GoogleError."""
    assert isinstance(
        GoogleProviderError("provider"),
        GoogleError,
    )