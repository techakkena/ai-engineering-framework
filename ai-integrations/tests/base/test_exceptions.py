"""
Tests for ai_integrations.base.exceptions.
"""

from ai_integrations.base.exceptions import (
    ProviderAuthenticationError,
    ProviderAuthorizationError,
    ProviderCapabilityError,
    ProviderConfigurationError,
    ProviderConnectionError,
    ProviderEmbeddingError,
    ProviderError,
    ProviderImageGenerationError,
    ProviderModelError,
    ProviderRateLimitError,
    ProviderRequestError,
    ProviderResponseError,
    ProviderStreamingError,
    ProviderTimeoutError,
    ProviderToolCallError,
    ProviderValidationError,
)


def test_provider_error() -> None:
    """ProviderError should derive from Exception."""
    error = ProviderError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    assert isinstance(
        ProviderConfigurationError("config"),
        ProviderError,
    )


def test_authentication_error() -> None:
    assert isinstance(
        ProviderAuthenticationError("auth"),
        ProviderError,
    )


def test_authorization_error() -> None:
    assert isinstance(
        ProviderAuthorizationError("authz"),
        ProviderError,
    )


def test_connection_error() -> None:
    assert isinstance(
        ProviderConnectionError("connection"),
        ProviderError,
    )


def test_timeout_error() -> None:
    assert isinstance(
        ProviderTimeoutError("timeout"),
        ProviderError,
    )


def test_rate_limit_error() -> None:
    assert isinstance(
        ProviderRateLimitError("rate"),
        ProviderError,
    )


def test_request_error() -> None:
    assert isinstance(
        ProviderRequestError("request"),
        ProviderError,
    )


def test_response_error() -> None:
    assert isinstance(
        ProviderResponseError("response"),
        ProviderError,
    )


def test_model_error() -> None:
    assert isinstance(
        ProviderModelError("model"),
        ProviderError,
    )


def test_validation_error() -> None:
    assert isinstance(
        ProviderValidationError("validation"),
        ProviderError,
    )


def test_streaming_error() -> None:
    assert isinstance(
        ProviderStreamingError("stream"),
        ProviderError,
    )


def test_embedding_error() -> None:
    assert isinstance(
        ProviderEmbeddingError("embedding"),
        ProviderError,
    )


def test_image_generation_error() -> None:
    assert isinstance(
        ProviderImageGenerationError("image"),
        ProviderError,
    )


def test_tool_call_error() -> None:
    assert isinstance(
        ProviderToolCallError("tool"),
        ProviderError,
    )


def test_capability_error() -> None:
    assert isinstance(
        ProviderCapabilityError("capability"),
        ProviderError,
    )