from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator

from .types import (
    ChatRequest,
    ChatResponse,
    EmbeddingResponse,
    HealthResponse,
)


class BaseProvider(ABC):
    """
    Abstract base class for AI providers.

    All provider implementations must inherit from this class
    and implement the required methods.
    """

    @abstractmethod
    async def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Execute a chat completion request.
        """
        raise NotImplementedError

    @abstractmethod
    async def stream(
        self,
        request: ChatRequest,
    ) -> AsyncIterator[str]:
        """
        Stream chat completion tokens.
        """
        raise NotImplementedError

    @abstractmethod
    async def embeddings(
        self,
        text: str,
    ) -> EmbeddingResponse:
        """
        Generate embeddings.
        """
        raise NotImplementedError

    @abstractmethod
    async def health(
        self,
    ) -> HealthResponse:
        """
        Check provider health.
        """
        raise NotImplementedError

    @abstractmethod
    async def close(self) -> None:
        """
        Close provider resources.
        """
        raise NotImplementedError