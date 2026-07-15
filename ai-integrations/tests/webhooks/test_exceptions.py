"""
Tests for ai_integrations.webhooks.exceptions.
"""

from ai_integrations.webhooks.exceptions import (
    WebhookAuthenticationError,
    WebhookConfigurationError,
    WebhookConnectionError,
    WebhookError,
    WebhookProviderError,
    WebhookRequestError,
    WebhookResponseError,
    WebhookTimeoutError,
)


def test_webhook_error() -> None:
    """WebhookError should derive from Exception."""
    error = WebhookError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    """Configuration error should derive from WebhookError."""
    assert isinstance(
        WebhookConfigurationError("config"),
        WebhookError,
    )


def test_authentication_error() -> None:
    """Authentication error should derive from WebhookError."""
    assert isinstance(
        WebhookAuthenticationError("auth"),
        WebhookError,
    )


def test_connection_error() -> None:
    """Connection error should derive from WebhookError."""
    assert isinstance(
        WebhookConnectionError("connection"),
        WebhookError,
    )


def test_timeout_error() -> None:
    """Timeout error should derive from WebhookError."""
    assert isinstance(
        WebhookTimeoutError("timeout"),
        WebhookError,
    )


def test_request_error() -> None:
    """Request error should derive from WebhookError."""
    assert isinstance(
        WebhookRequestError("request"),
        WebhookError,
    )


def test_response_error() -> None:
    """Response error should derive from WebhookError."""
    assert isinstance(
        WebhookResponseError("response"),
        WebhookError,
    )


def test_provider_error() -> None:
    """Provider error should derive from WebhookError."""
    assert isinstance(
        WebhookProviderError("provider"),
        WebhookError,
    )