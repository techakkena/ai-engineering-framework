"""
Tests for ai_integrations.mistral_provider.operations.
"""

import pytest

from ai_integrations.mistral_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
)
from ai_integrations.mistral_provider.exceptions import (
    MistralConfigurationError,
    MistralModelError,
)
from ai_integrations.mistral_provider.operations import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatMessage,
    MistralProvider,
)


def test_chat_message() -> None:
    """ChatMessage should retain values."""
    message = ChatMessage(
        role="user",
        content="Hello Mistral!",
    )

    assert message.role == "user"
    assert message.content == "Hello Mistral!"


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
            "prompt_tokens": 20,
            "completion_tokens": 15,
            "total_tokens": 35,
        },
    )

    assert response.model == DEFAULT_MODEL
    assert response.finish_reason == "stop"
    assert response.usage["total_tokens"] == 35


def test_provider_defaults() -> None:
    """Provider should expose default configuration."""
    provider = MistralProvider(
        api_key="test-key",
    )

    health = provider.health_check()

    assert health["provider"] == "mistral"
    assert health["configured"] is True
    assert health["model"] == DEFAULT_MODEL
    assert health["api_base"] == DEFAULT_API_BASE
    assert health["timeout"] == DEFAULT_TIMEOUT
    assert health["max_retries"] == DEFAULT_MAX_RETRIES


def test_invalid_api_key() -> None:
    """Empty API key should fail."""
    with pytest.raises(
        MistralConfigurationError,
    ):
        MistralProvider(api_key="")


def test_invalid_model() -> None:
    """Unsupported model should fail."""
    with pytest.raises(
        MistralModelError,
    ):
        MistralProvider(
            api_key="key",
            model="invalid-model",
        )


def test_chat_requires_messages() -> None:
    """Chat requires at least one message."""
    provider = MistralProvider(
        api_key="key",
    )

    request = ChatCompletionRequest(
        messages=(),
    )

    with pytest.raises(
        MistralConfigurationError,
    ):
        provider.chat(request)


def test_custom_configuration() -> None:
    """Custom configuration should be retained."""
    provider = MistralProvider(
        api_key="key",
        model="mistral-medium-latest",
        api_base="https://example.test",
        timeout=120.0,
        max_retries=5,
    )

    health = provider.health_check()

    assert health["model"] == "mistral-medium-latest"
    assert health["api_base"] == "https://example.test"
    assert health["timeout"] == 120.0
    assert health["max_retries"] == 5