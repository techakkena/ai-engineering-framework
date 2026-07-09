import pytest

from ai.providers.base_provider import BaseProvider
from ai.providers.provider_factory import ProviderFactory
from ai.providers.types import (
    ChatRequest,
    ChatResponse,
    EmbeddingResponse,
    HealthResponse,
)


class DummyProvider(BaseProvider):

    async def chat(self, request: ChatRequest) -> ChatResponse:
        return ChatResponse(content="ok", model="dummy")

    async def stream(self, request: ChatRequest):
        yield "ok"

    async def embeddings(self, text: str) -> EmbeddingResponse:
        return EmbeddingResponse(
            embedding=[],
            model="dummy",
            dimensions=0,
        )

    async def health(self) -> HealthResponse:
        return HealthResponse(
            provider="dummy",
            status="healthy",
            latency_ms=0.0,
        )

    async def close(self) -> None:
        return None


def test_provider_factory_register_and_create():
    ProviderFactory.register("dummy", DummyProvider)

    provider = ProviderFactory.create("dummy")

    assert isinstance(provider, DummyProvider)


def test_unknown_provider():
    with pytest.raises(ValueError):
        ProviderFactory.create("unknown")