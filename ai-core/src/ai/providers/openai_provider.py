"""
OpenAI provider implementation.

This module adapts the OpenAI SDK to the ai-core
provider interface.
"""

from __future__ import annotations

from collections.abc import AsyncIterator

from openai import AsyncOpenAI

from .base_provider import BaseProvider
from .types import (
    ChatRequest,
    ChatResponse,
    EmbeddingResponse,
    HealthResponse,
)


class OpenAIProvider(BaseProvider):
    """
    OpenAI provider implementation.
    """

    def __init__(
        self,
        api_key: str,
        timeout: float = 60.0,
    ):
       self.client: AsyncOpenAI = AsyncOpenAI(
        api_key=api_key,
        timeout=timeout,
    )

    async def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:

        response = await self.client.chat.completions.create(
            model=request.model,
            messages=[
                {
                    "role": m.role,
                    "content": m.content,
                }
                for m in request.messages
            ],
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )

        return ChatResponse(
            content=response.choices[0].message.content or "",
            model=response.model,
            usage=response.usage.model_dump(),
            raw=response,
        )

    async def stream(
        self,
        request: ChatRequest,
    ) -> AsyncIterator[str]:

        stream = await self.client.chat.completions.create(
            model=request.model,
            messages=[
                {
                    "role": m.role,
                    "content": m.content,
                }
                for m in request.messages
            ],
            stream=True,
        )

        async for chunk in stream:
            delta = chunk.choices[0].delta.content

            if delta:
                yield delta

    async def embeddings(
        self,
        text: str,
    ) -> EmbeddingResponse:

        response = await self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text,
        )

        embedding = response.data[0].embedding

        return EmbeddingResponse(
            embedding=embedding,
            model=response.model,
            dimensions=len(embedding),
        )

    async def health(
        self,
    ) -> HealthResponse:

        return HealthResponse(
            provider="openai",
            status="healthy",
            latency_ms=0.0,
        )

    async def close(self) -> None:
        await self.client.close()

        __all__ = [
        "OpenAIProvider",
    ]