"""
Tests for ai_integrations.github.exceptions.
"""

from ai_integrations.github.exceptions import (
    GitHubAuthenticationError,
    GitHubConfigurationError,
    GitHubConnectionError,
    GitHubError,
    GitHubProviderError,
    GitHubRateLimitError,
    GitHubRequestError,
    GitHubResponseError,
    GitHubTimeoutError,
)


def test_github_error() -> None:
    """GitHubError should derive from Exception."""
    error = GitHubError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    """Configuration error should derive from GitHubError."""
    assert isinstance(
        GitHubConfigurationError("config"),
        GitHubError,
    )


def test_authentication_error() -> None:
    """Authentication error should derive from GitHubError."""
    assert isinstance(
        GitHubAuthenticationError("auth"),
        GitHubError,
    )


def test_rate_limit_error() -> None:
    """Rate limit error should derive from GitHubError."""
    assert isinstance(
        GitHubRateLimitError("rate"),
        GitHubError,
    )


def test_connection_error() -> None:
    """Connection error should derive from GitHubError."""
    assert isinstance(
        GitHubConnectionError("connection"),
        GitHubError,
    )


def test_timeout_error() -> None:
    """Timeout error should derive from GitHubError."""
    assert isinstance(
        GitHubTimeoutError("timeout"),
        GitHubError,
    )


def test_request_error() -> None:
    """Request error should derive from GitHubError."""
    assert isinstance(
        GitHubRequestError("request"),
        GitHubError,
    )


def test_response_error() -> None:
    """Response error should derive from GitHubError."""
    assert isinstance(
        GitHubResponseError("response"),
        GitHubError,
    )


def test_provider_error() -> None:
    """Provider error should derive from GitHubError."""
    assert isinstance(
        GitHubProviderError("provider"),
        GitHubError,
    )