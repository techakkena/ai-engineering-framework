"""
Tests for ai_integrations.azure_provider.operations.
"""

import pytest

from ai_integrations.azure_provider.constants import (
    DEFAULT_API_VERSION,
    DEFAULT_ENDPOINT,
    DEFAULT_MODEL,
)
from ai_integrations.azure_provider.exceptions import (
    AzureConfigurationError,
    AzureModelError,
)
from ai_integrations.azure_provider.operations import (
    AzureProvider,
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatMessage,
)


def test_chat_message() -> None:
    """ChatMessage should retain values."""
    message = ChatMessage(
        role="user",
        content="Hello Azure!",
    )

    assert message.role == "user"
    assert message.content == "Hello Azure!"


def test_chat_completion_request_defaults() -> None:
    """Request should use default values."""
    request = ChatCompletionRequest(
        messages=(
            ChatMessage(
                role="user",
                content="Hello",
            ),
        ),
    )

    assert request.model == DEFAULT_MODEL


def test_chat_completion_response() -> None:
    """Response should retain values."""
    response = ChatCompletionResponse(
        model=DEFAULT_MODEL,
        content="Hello!",
        finish_reason="stop",
        usage={
            "prompt_tokens": 10,
            "completion_tokens": 5,
            "total_tokens": 15,
        },
    )

    assert response.model == DEFAULT_MODEL
    assert response.finish_reason == "stop"
    assert response.usage["total_tokens"] == 15


def test_provider_defaults() -> None:
    """Provider should expose default configuration."""
    provider = AzureProvider(
        api_key="test-key",
    )

    assert provider.model == DEFAULT_MODEL
    assert provider.endpoint == DEFAULT_ENDPOINT
    assert provider.api_version == DEFAULT_API_VERSION


def test_invalid_api_key() -> None:
    """Empty API keys should fail."""
    with pytest.raises(
        AzureConfigurationError,
    ):
        AzureProvider(api_key="")


def test_invalid_model() -> None:
    """Unsupported models should fail."""
    with pytest.raises(
        AzureModelError,
    ):
        AzureProvider(
            api_key="key",
            model="invalid-model",
        )


def test_chat_requires_messages() -> None:
    """Chat requires at least one message."""
    provider = AzureProvider(
        api_key="key",
    )

    request = ChatCompletionRequest(
        messages=(),
    )

    with pytest.raises(
        AzureConfigurationError,
    ):
        provider.chat(request)


def test_chat_invalid_model() -> None:
    """Invalid request model should fail."""
    provider = AzureProvider(
        api_key="key",
    )

    request = ChatCompletionRequest(
        model="invalid-model",
        messages=(
            ChatMessage(
                role="user",
                content="Hello",
            ),
        ),
    )

    with pytest.raises(
        AzureModelError,
    ):
        provider.chat(request)


def test_health_check() -> None:
    """Health check should expose provider configuration."""
    provider = AzureProvider(
        api_key="key",
    )

    health = provider.health_check()

    assert health["provider"] == "azure"
    assert health["configured"] is True
    assert health["endpoint"] == DEFAULT_ENDPOINT
    assert health["api_version"] == DEFAULT_API_VERSION
    assert health["model"] == DEFAULT_MODEL


def test_provider_custom_configuration() -> None:
    """Custom configuration should be retained."""
    provider = AzureProvider(
        api_key="key",
        endpoint="https://contoso.openai.azure.com",
        api_version="2025-01-01-preview",
        model="gpt-5-mini",
        timeout=120.0,
        max_retries=5,
    )

    assert provider.endpoint == "https://contoso.openai.azure.com"
    assert provider.api_version == "2025-01-01-preview"
    assert provider.model == "gpt-5-mini"

    health = provider.health_check()
    assert health["timeout"] == 120.0
    assert health["max_retries"] == 5