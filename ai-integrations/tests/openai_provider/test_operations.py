"""
Tests for ai_integrations.openai_provider.operations.
"""

from __future__ import annotations

import pytest

from ai_integrations.openai_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
)
from ai_integrations.openai_provider.exceptions import (
    OpenAIConfigurationError,
    OpenAIModelError,
)
from ai_integrations.openai_provider.operations import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatMessage,
    OpenAIProvider,
)


def test_chat_message() -> None:
    """ChatMessage should retain its values."""
    message = ChatMessage(
        role="user",
        content="Hello!",
    )

    assert message.role == "user"
    assert message.content == "Hello!"


def test_chat_completion_request_defaults() -> None:
    """ChatCompletionRequest should use default values."""
    request = ChatCompletionRequest(
        messages=(
            ChatMessage(
                role="user",
                content="Hello",
            ),
        ),
    )

    assert request.model == DEFAULT_MODEL
    assert request.messages[0].content == "Hello"


def test_chat_completion_response() -> None:
    """ChatCompletionResponse should retain its values."""
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
    provider = OpenAIProvider(
        api_key="test-api-key",
    )

    assert provider.model == DEFAULT_MODEL
    assert provider.api_base == DEFAULT_API_BASE
    assert provider.timeout == DEFAULT_TIMEOUT
    assert provider.max_retries == DEFAULT_MAX_RETRIES


def test_invalid_api_key() -> None:
    """Empty API keys should be rejected."""
    with pytest.raises(OpenAIConfigurationError):
        OpenAIProvider(api_key="")


def test_invalid_model() -> None:
    """Unsupported models should be rejected."""
    with pytest.raises(OpenAIModelError):
        OpenAIProvider(
            api_key="test-api-key",
            model="invalid-model",
        )


def test_chat_requires_messages() -> None:
    """A chat request must contain at least one message."""
    provider = OpenAIProvider(
        api_key="test-api-key",
    )

    request = ChatCompletionRequest(
        messages=(),
    )

    with pytest.raises(OpenAIConfigurationError):
        provider.chat(request)


def test_chat_invalid_model() -> None:
    """A request with an unsupported model should fail."""
    provider = OpenAIProvider(
        api_key="test-api-key",
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

    with pytest.raises(OpenAIModelError):
        provider.chat(request)


def test_embeddings_requires_input() -> None:
    """Embedding requests require at least one input."""
    provider = OpenAIProvider(
        api_key="test-api-key",
    )

    with pytest.raises(OpenAIConfigurationError):
        provider.embeddings([])


def test_health_check() -> None:
    """Health check should expose provider configuration."""
    provider = OpenAIProvider(
        api_key="test-api-key",
    )

    result = provider.health_check()

    assert result["provider"] == "openai"
    assert result["configured"] is True
    assert result["model"] == DEFAULT_MODEL
    assert result["api_base"] == DEFAULT_API_BASE
    assert result["timeout"] == DEFAULT_TIMEOUT
    assert result["max_retries"] == DEFAULT_MAX_RETRIES


def test_provider_custom_configuration() -> None:
    """Custom configuration should be retained."""
    provider = OpenAIProvider(
        api_key="test-api-key",
        model="gpt-5-mini",
        api_base="https://example.test/v1",
        timeout=120.0,
        max_retries=5,
    )

    assert provider.model == "gpt-5-mini"
    assert provider.api_base == "https://example.test/v1"
    assert provider.timeout == 120.0
    assert provider.max_retries == 5