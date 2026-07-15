"""
Tests for ai_integrations.slack.exceptions.
"""

from ai_integrations.slack.exceptions import (
    SlackAuthenticationError,
    SlackConfigurationError,
    SlackConnectionError,
    SlackError,
    SlackProviderError,
    SlackRateLimitError,
    SlackRequestError,
    SlackResponseError,
    SlackTimeoutError,
)


def test_slack_error() -> None:
    """SlackError should derive from Exception."""
    error = SlackError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    """Configuration error should derive from SlackError."""
    assert isinstance(
        SlackConfigurationError("config"),
        SlackError,
    )


def test_authentication_error() -> None:
    """Authentication error should derive from SlackError."""
    assert isinstance(
        SlackAuthenticationError("auth"),
        SlackError,
    )


def test_rate_limit_error() -> None:
    """Rate limit error should derive from SlackError."""
    assert isinstance(
        SlackRateLimitError("rate"),
        SlackError,
    )


def test_connection_error() -> None:
    """Connection error should derive from SlackError."""
    assert isinstance(
        SlackConnectionError("connection"),
        SlackError,
    )


def test_timeout_error() -> None:
    """Timeout error should derive from SlackError."""
    assert isinstance(
        SlackTimeoutError("timeout"),
        SlackError,
    )


def test_request_error() -> None:
    """Request error should derive from SlackError."""
    assert isinstance(
        SlackRequestError("request"),
        SlackError,
    )


def test_response_error() -> None:
    """Response error should derive from SlackError."""
    assert isinstance(
        SlackResponseError("response"),
        SlackError,
    )


def test_provider_error() -> None:
    """Provider error should derive from SlackError."""
    assert isinstance(
        SlackProviderError("provider"),
        SlackError,
    )