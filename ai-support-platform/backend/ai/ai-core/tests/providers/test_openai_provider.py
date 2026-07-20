from __future__ import annotations

"""
AI Engineering Framework
OpenAI Provider Tests

Author : TECHAKKENA
"""

import pytest

from ai.providers.openai_provider import OpenAIProvider
from ai.providers.types import ProviderConfig


def test_provider_creation():
    provider = OpenAIProvider(
        ProviderConfig(
            api_key="dummy-key",
            model="gpt-5",
        )
    )

    assert provider.client is None


def test_connect():
    provider = OpenAIProvider(
        ProviderConfig(
            api_key="dummy-key",
            model="gpt-5",
        )
    )

    provider.connect()

    assert provider.client is not None


def test_close():
    provider = OpenAIProvider(
        ProviderConfig(
            api_key="dummy-key",
            model="gpt-5",
        )
    )

    provider.connect()

    provider.close()

    assert provider.client is None


def test_chat_not_implemented():
    provider = OpenAIProvider(
        ProviderConfig(
            api_key="dummy-key",
            model="gpt-5",
        )
    )

    with pytest.raises(NotImplementedError):
        provider.chat([])


def test_embeddings_not_implemented():
    provider = OpenAIProvider(
        ProviderConfig(
            api_key="dummy-key",
            model="gpt-5",
        )
    )

    with pytest.raises(NotImplementedError):
        provider.embeddings("Hello")


def test_image_not_implemented():
    provider = OpenAIProvider(
        ProviderConfig(
            api_key="dummy-key",
            model="gpt-5",
        )
    )

    with pytest.raises(NotImplementedError):
        provider.image("Cat")


def test_speech_not_implemented():
    provider = OpenAIProvider(
        ProviderConfig(
            api_key="dummy-key",
            model="gpt-5",
        )
    )

    with pytest.raises(NotImplementedError):
        provider.speech("Hello")
