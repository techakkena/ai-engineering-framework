"""
Tests for ai_integrations.google_provider.operations.
"""

import pytest

from ai_integrations.google_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
)
from ai_integrations.google_provider.exceptions import (
    GoogleConfigurationError,
    GoogleModelError,
)
from ai_integrations.google_provider.operations import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatMessage,
    GoogleProvider,
)


def test_chat_message() -> None:
    """ChatMessage should retain values."""
    message = ChatMessage(
        role="user",
        content="Hello Gemini!",
    )

    assert message.role == "user"
    assert message.content == "Hello Gemini!"


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
    assert request.max_tokens == 8192


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
    provider = GoogleProvider(
        api_key="test-key",
    )

    assert provider.model == DEFAULT_MODEL
    assert provider.api_base == DEFAULT_API_BASE
    assert provider.timeout == DEFAULT_TIMEOUT
    assert provider.max_retries == DEFAULT_MAX_RETRIES


def test_invalid_api_key() -> None:
    """Empty API keys should fail."""
    with pytest.raises(GoogleConfigurationError):
        GoogleProvider(api_key="")


def test_invalid_model() -> None:
    """Unsupported models should fail."""
    with pytest.raises(GoogleModelError):
        GoogleProvider(
            api_key="key",
            model="invalid-model",
        )


def test_chat_requires_messages() -> None:
    """Chat requires at least one message."""
    provider = GoogleProvider(
        api_key="key",
    )

    request = ChatCompletionRequest(
        messages=(),
    )

    with pytest.raises(GoogleConfigurationError):
        provider.chat(request)


def test_chat_invalid_model() -> None:
    """Invalid models should fail."""
    provider = GoogleProvider(
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

    with pytest.raises(GoogleModelError):
        provider.chat(request)


def test_health_check() -> None:
    """Health check should expose provider configuration."""
    provider = GoogleProvider(
        api_key="key",
    )

    health = provider.health_check()

    assert health["provider"] == "google"
    assert health["configured"] is True
    assert health["model"] == DEFAULT_MODEL
    assert health["api_base"] == DEFAULT_API_BASE


def test_provider_custom_configuration() -> None:
    """Custom configuration should be retained."""
    provider = GoogleProvider(
        api_key="key",
        model="gemini-2.5-flash",
        api_base="https://example.test",
        timeout=120.0,
        max_retries=5,
    )

    assert provider.model == "gemini-2.5-flash"
    assert provider.api_base == "https://example.test"
    assert provider.timeout == 120.0
    assert provider.max_retries == 5