"""
Tests for ai_integrations.anthropic_provider.operations.
"""

import pytest

from ai_integrations.anthropic_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
)
from ai_integrations.anthropic_provider.exceptions import (
    AnthropicConfigurationError,
    AnthropicModelError,
)
from ai_integrations.anthropic_provider.operations import (
    AnthropicProvider,
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatMessage,
)


def test_chat_message() -> None:
    """ChatMessage should retain values."""
    message = ChatMessage(
        role="user",
        content="Hello Claude!",
    )

    assert message.role == "user"
    assert message.content == "Hello Claude!"


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
    assert request.max_tokens == 4096


def test_chat_completion_response() -> None:
    """Response should retain values."""
    response = ChatCompletionResponse(
        model=DEFAULT_MODEL,
        content="Hello!",
        stop_reason="end_turn",
        usage={"input_tokens": 10},
    )

    assert response.model == DEFAULT_MODEL
    assert response.stop_reason == "end_turn"


def test_provider_defaults() -> None:
    """Provider should expose default configuration."""
    provider = AnthropicProvider(
        api_key="test-key",
    )

    assert provider.model == DEFAULT_MODEL
    assert provider.api_base == DEFAULT_API_BASE
    assert provider.timeout == DEFAULT_TIMEOUT
    assert provider.max_retries == DEFAULT_MAX_RETRIES


def test_invalid_api_key() -> None:
    """Empty API keys should fail."""
    with pytest.raises(
        AnthropicConfigurationError,
    ):
        AnthropicProvider(api_key="")


def test_invalid_model() -> None:
    """Unsupported models should fail."""
    with pytest.raises(
        AnthropicModelError,
    ):
        AnthropicProvider(
            api_key="key",
            model="invalid-model",
        )


def test_chat_requires_messages() -> None:
    """Chat requires at least one message."""
    provider = AnthropicProvider(
        api_key="key",
    )

    request = ChatCompletionRequest(
        messages=(),
    )

    with pytest.raises(
        AnthropicConfigurationError,
    ):
        provider.chat(request)


def test_chat_invalid_model() -> None:
    """Invalid models should fail."""
    provider = AnthropicProvider(
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
        AnthropicModelError,
    ):
        provider.chat(request)


def test_health_check() -> None:
    """Health check should expose provider configuration."""
    provider = AnthropicProvider(
        api_key="key",
    )

    health = provider.health_check()

    assert health["provider"] == "anthropic"
    assert health["configured"] is True
    assert health["model"] == DEFAULT_MODEL
    assert health["api_base"] == DEFAULT_API_BASE


def test_provider_custom_configuration() -> None:
    """Custom configuration should be retained."""
    provider = AnthropicProvider(
        api_key="key",
        model="claude-3-5-sonnet-latest",
        api_base="https://example.com",
        timeout=120.0,
        max_retries=5,
    )

    assert provider.model == "claude-3-5-sonnet-latest"
    assert provider.api_base == "https://example.com"
    assert provider.timeout == 120.0
    assert provider.max_retries == 5