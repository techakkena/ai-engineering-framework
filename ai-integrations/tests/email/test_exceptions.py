"""
Tests for ai_integrations.email.exceptions.
"""

from ai_integrations.email.exceptions import (
    EmailAuthenticationError,
    EmailConfigurationError,
    EmailConnectionError,
    EmailError,
    EmailProviderError,
    EmailRequestError,
    EmailResponseError,
    EmailTimeoutError,
)


def test_email_error() -> None:
    """EmailError should derive from Exception."""
    error = EmailError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    """Configuration error should derive from EmailError."""
    assert isinstance(
        EmailConfigurationError("config"),
        EmailError,
    )


def test_authentication_error() -> None:
    """Authentication error should derive from EmailError."""
    assert isinstance(
        EmailAuthenticationError("auth"),
        EmailError,
    )


def test_connection_error() -> None:
    """Connection error should derive from EmailError."""
    assert isinstance(
        EmailConnectionError("connection"),
        EmailError,
    )


def test_timeout_error() -> None:
    """Timeout error should derive from EmailError."""
    assert isinstance(
        EmailTimeoutError("timeout"),
        EmailError,
    )


def test_request_error() -> None:
    """Request error should derive from EmailError."""
    assert isinstance(
        EmailRequestError("request"),
        EmailError,
    )


def test_response_error() -> None:
    """Response error should derive from EmailError."""
    assert isinstance(
        EmailResponseError("response"),
        EmailError,
    )


def test_provider_error() -> None:
    """Provider error should derive from EmailError."""
    assert isinstance(
        EmailProviderError("provider"),
        EmailError,
    )