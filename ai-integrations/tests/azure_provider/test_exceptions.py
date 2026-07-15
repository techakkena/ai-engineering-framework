"""
Tests for ai_integrations.azure_provider.exceptions.
"""

from ai_integrations.azure_provider.exceptions import (
    AzureAuthenticationError,
    AzureConfigurationError,
    AzureConnectionError,
    AzureError,
    AzureModelError,
    AzureProviderError,
    AzureRateLimitError,
    AzureRequestError,
    AzureResponseError,
    AzureTimeoutError,
)


def test_azure_error() -> None:
    """AzureError should derive from Exception."""
    error = AzureError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    """Configuration error should derive from AzureError."""
    assert isinstance(
        AzureConfigurationError("config"),
        AzureError,
    )


def test_authentication_error() -> None:
    """Authentication error should derive from AzureError."""
    assert isinstance(
        AzureAuthenticationError("auth"),
        AzureError,
    )


def test_rate_limit_error() -> None:
    """Rate limit error should derive from AzureError."""
    assert isinstance(
        AzureRateLimitError("rate"),
        AzureError,
    )


def test_connection_error() -> None:
    """Connection error should derive from AzureError."""
    assert isinstance(
        AzureConnectionError("connection"),
        AzureError,
    )


def test_timeout_error() -> None:
    """Timeout error should derive from AzureError."""
    assert isinstance(
        AzureTimeoutError("timeout"),
        AzureError,
    )


def test_model_error() -> None:
    """Model error should derive from AzureError."""
    assert isinstance(
        AzureModelError("model"),
        AzureError,
    )


def test_request_error() -> None:
    """Request error should derive from AzureError."""
    assert isinstance(
        AzureRequestError("request"),
        AzureError,
    )


def test_response_error() -> None:
    """Response error should derive from AzureError."""
    assert isinstance(
        AzureResponseError("response"),
        AzureError,
    )


def test_provider_error() -> None:
    """Provider error should derive from AzureError."""
    assert isinstance(
        AzureProviderError("provider"),
        AzureError,
    )