"""
AI Engineering Framework
Base Provider Tests

Author : TECHAKKENA
"""

import pytest

from ai.providers.base_provider import BaseProvider
from ai.providers.types import (
    ProviderConfig,
    ProviderMessage,
    ProviderResponse,
)


class DummyProvider(BaseProvider):
    """
    Dummy provider for testing.
    """

    def connect(self) -> None:
        pass

    def chat(
        self,
        messages: list[ProviderMessage],
    ) -> ProviderResponse:
        return ProviderResponse(
            content="Hello",
            model=self.config.model,
        )

    def embeddings(
        self,
        text: str,
    ):
        return [0.1, 0.2, 0.3]

    def image(
        self,
        prompt: str,
    ):
        return "image.png"

    def speech(
        self,
        text: str,
    ):
        return b"audio"

    def close(
        self,
    ) -> None:
        pass


def test_base_provider_is_abstract():
    with pytest.raises(TypeError):
        BaseProvider(
            ProviderConfig(
                model="gpt-5",
            )
        )


def test_provider_creation():
    provider = DummyProvider(
        ProviderConfig(
            model="gpt-5",
        )
    )

    assert provider.config.model == "gpt-5"


def test_connect():
    provider = DummyProvider(
        ProviderConfig(
            model="gpt-5",
        )
    )

    provider.connect()


def test_chat():
    provider = DummyProvider(
        ProviderConfig(
            model="gpt-5",
        )
    )

    response = provider.chat(
        [
            ProviderMessage(
                role="user",
                content="Hello",
            )
        ]
    )

    assert response.content == "Hello"
    assert response.model == "gpt-5"


def test_embeddings():
    provider = DummyProvider(
        ProviderConfig(
            model="gpt-5",
        )
    )

    embeddings = provider.embeddings("Hello")

    assert isinstance(
        embeddings,
        list,
    )


def test_image():
    provider = DummyProvider(
        ProviderConfig(
            model="gpt-5",
        )
    )

    image = provider.image("Cat")

    assert image == "image.png"


def test_speech():
    provider = DummyProvider(
        ProviderConfig(
            model="gpt-5",
        )
    )

    speech = provider.speech("Hello")

    assert isinstance(
        speech,
        bytes,
    )


def test_close():
    provider = DummyProvider(
        ProviderConfig(
            model="gpt-5",
        )
    )

    provider.close()
