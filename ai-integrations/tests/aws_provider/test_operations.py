"""
Tests for ai_integrations.aws_provider.operations.
"""

import pytest

from ai_integrations.aws_provider.constants import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_REGION,
    DEFAULT_TIMEOUT,
)
from ai_integrations.aws_provider.exceptions import (
    AWSConfigurationError,
    AWSModelError,
)
from ai_integrations.aws_provider.operations import (
    AWSProvider,
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatMessage,
)


def test_chat_message() -> None:
    """ChatMessage should retain values."""
    message = ChatMessage(
        role="user",
        content="Hello Bedrock!",
    )

    assert message.role == "user"
    assert message.content == "Hello Bedrock!"


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
            "input_tokens": 10,
            "output_tokens": 5,
            "total_tokens": 15,
        },
    )

    assert response.model == DEFAULT_MODEL
    assert response.finish_reason == "stop"
    assert response.usage["total_tokens"] == 15


def test_provider_defaults() -> None:
    """Provider should expose default configuration."""
    provider = AWSProvider(
        access_key_id="access-key",
        secret_access_key="secret-key",
    )

    assert provider.model == DEFAULT_MODEL
    assert provider.region == DEFAULT_REGION


def test_invalid_access_key() -> None:
    """Empty access key should fail."""
    with pytest.raises(
        AWSConfigurationError,
    ):
        AWSProvider(
            access_key_id="",
            secret_access_key="secret-key",
        )


def test_invalid_secret_key() -> None:
    """Empty secret key should fail."""
    with pytest.raises(
        AWSConfigurationError,
    ):
        AWSProvider(
            access_key_id="access-key",
            secret_access_key="",
        )


def test_invalid_model() -> None:
    """Unsupported models should fail."""
    with pytest.raises(
        AWSModelError,
    ):
        AWSProvider(
            access_key_id="access-key",
            secret_access_key="secret-key",
            model="invalid-model",
        )


def test_chat_requires_messages() -> None:
    """Chat requires at least one message."""
    provider = AWSProvider(
        access_key_id="access-key",
        secret_access_key="secret-key",
    )

    request = ChatCompletionRequest(
        messages=(),
    )

    with pytest.raises(
        AWSConfigurationError,
    ):
        provider.chat(request)


def test_chat_invalid_model() -> None:
    """Invalid request model should fail."""
    provider = AWSProvider(
        access_key_id="access-key",
        secret_access_key="secret-key",
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
        AWSModelError,
    ):
        provider.chat(request)


def test_health_check() -> None:
    """Health check should expose provider configuration."""
    provider = AWSProvider(
        access_key_id="access-key",
        secret_access_key="secret-key",
    )

    health = provider.health_check()

    assert health["provider"] == "aws"
    assert health["configured"] is True
    assert health["region"] == DEFAULT_REGION
    assert health["model"] == DEFAULT_MODEL
    assert health["timeout"] == DEFAULT_TIMEOUT
    assert health["max_retries"] == DEFAULT_MAX_RETRIES


def test_provider_custom_configuration() -> None:
    """Custom configuration should be retained."""
    provider = AWSProvider(
        access_key_id="access-key",
        secret_access_key="secret-key",
        region="eu-west-1",
        model="amazon.nova-lite-v1:0",
        timeout=120.0,
        max_retries=5,
    )

    assert provider.region == "eu-west-1"
    assert provider.model == "amazon.nova-lite-v1:0"

    health = provider.health_check()

    assert health["timeout"] == 120.0
    assert health["max_retries"] == 5