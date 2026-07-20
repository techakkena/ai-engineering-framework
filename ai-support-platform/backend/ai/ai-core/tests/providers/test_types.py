from __future__ import annotations

"""
AI Engineering Framework
Provider Types Tests

Author : TECHAKKENA
"""

from ai.providers.types import (
    ProviderConfig,
    ProviderMessage,
    ProviderResponse,
    ProviderUsage,
)


def test_provider_config_defaults():
    config = ProviderConfig(
        model="gpt-5",
    )

    assert config.model == "gpt-5"
    assert config.temperature == 0.2
    assert config.max_tokens == 4096
    assert config.timeout == 60
    assert config.stream is False


def test_provider_config_custom():
    config = ProviderConfig(
        api_key="key",
        model="gpt-5-mini",
        temperature=0.7,
        max_tokens=2000,
        timeout=120,
        stream=True,
    )

    assert config.api_key == "key"
    assert config.temperature == 0.7
    assert config.max_tokens == 2000
    assert config.timeout == 120
    assert config.stream is True


def test_provider_message():
    message = ProviderMessage(
        role="user",
        content="Hello",
    )

    assert message.role == "user"
    assert message.content == "Hello"


def test_provider_usage():
    usage = ProviderUsage(
        prompt_tokens=10,
        completion_tokens=20,
        total_tokens=30,
    )

    assert usage.prompt_tokens == 10
    assert usage.completion_tokens == 20
    assert usage.total_tokens == 30


def test_provider_response():
    response = ProviderResponse(
        content="Hi",
        model="gpt-5",
    )

    assert response.content == "Hi"
    assert response.model == "gpt-5"
    assert response.finish_reason == "stop"


def test_provider_response_usage():
    usage = ProviderUsage(
        prompt_tokens=1,
        completion_tokens=2,
        total_tokens=3,
    )

    response = ProviderResponse(
        content="Hi",
        model="gpt-5",
        usage=usage,
    )

    assert response.usage.total_tokens == 3
