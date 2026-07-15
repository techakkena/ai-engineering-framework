"""
Tests for ai_integrations.base.operations.
"""

from abc import ABC

import pytest

from ai_integrations.base.exceptions import (
    ProviderConfigurationError,
)
from ai_integrations.base.operations import (
    BaseProvider,
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatMessage,
    EmbeddingRequest,
    EmbeddingResponse,
    ProviderConfig,
)


class DummyProvider(BaseProvider):
    """Concrete provider for testing."""

    def chat(
        self,
        request: ChatCompletionRequest,
    ) -> ChatCompletionResponse:
        return ChatCompletionResponse(
            model=self.model,
            content="ok",
            finish_reason="stop",
        )

    def embeddings(
        self,
        request: EmbeddingRequest,
    ) -> EmbeddingResponse:
        return EmbeddingResponse(
            model=self.model,
            embeddings=((0.1, 0.2),),
        )

    def health_check(self) -> dict[str, str]:
        return {"status": "ok"}


def create_provider() -> DummyProvider:
    """Create a provider."""
    return DummyProvider(
        ProviderConfig(
            api_key="key",
            model="test-model",
            api_base="https://example.com",
        )
    )


def test_provider_config() -> None:
    provider = create_provider()

    assert provider.model == "test-model"
    assert provider.is_configured()


def test_provider_info() -> None:
    provider = create_provider()

    info = provider.provider_info()

    assert info["model"] == "test-model"
    assert info["provider"] == "DummyProvider"


def test_chat_message() -> None:
    message = ChatMessage(
        role="user",
        content="Hello",
    )

    assert message.role == "user"


def test_invalid_role() -> None:
    with pytest.raises(
        ProviderConfigurationError,
    ):
        ChatMessage(
            role="invalid",
            content="Hello",
        )


def test_empty_content() -> None:
    with pytest.raises(
        ProviderConfigurationError,
    ):
        ChatMessage(
            role="user",
            content="",
        )


def test_chat_request() -> None:
    request = ChatCompletionRequest(
        model="test-model",
        messages=(
            ChatMessage(
                role="user",
                content="Hello",
            ),
        ),
    )

    assert request.max_tokens == 4096


def test_empty_messages() -> None:
    with pytest.raises(
        ProviderConfigurationError,
    ):
        ChatCompletionRequest(
            model="test-model",
            messages=(),
        )


def test_embedding_request() -> None:
    request = EmbeddingRequest(
        model="embedding-model",
        input=("hello",),
    )

    assert request.model == "embedding-model"


def test_empty_embedding_input() -> None:
    with pytest.raises(
        ProviderConfigurationError,
    ):
        EmbeddingRequest(
            model="embedding-model",
            input=(),
        )


def test_chat() -> None:
    provider = create_provider()

    response = provider.chat(
        ChatCompletionRequest(
            model="test-model",
            messages=(
                ChatMessage(
                    role="user",
                    content="Hello",
                ),
            ),
        )
    )

    assert response.content == "ok"


def test_embeddings() -> None:
    provider = create_provider()

    response = provider.embeddings(
        EmbeddingRequest(
            model="embedding-model",
            input=("hello",),
        )
    )

    assert len(response.embeddings) == 1


def test_base_provider_is_abstract() -> None:
    """BaseProvider should be abstract."""
    assert issubclass(BaseProvider, ABC)