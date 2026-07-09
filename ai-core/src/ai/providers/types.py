from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ChatMessage:
    """
    Represents a single chat message.
    """

    role: str
    content: str


@dataclass(slots=True)
class ChatRequest:
    """
    Standard chat request for all providers.
    """

    messages: list[ChatMessage]
    model: str
    temperature: float = 0.7
    max_tokens: int | None = None


@dataclass(slots=True)
class ChatResponse:
    """
    Standard chat response.
    """

    content: str
    model: str
    usage: dict[str, Any] = field(default_factory=dict)
    raw: Any = None


@dataclass(slots=True)
class EmbeddingResponse:
    """
    Standard embedding response.
    """

    embedding: list[float]
    model: str
    dimensions: int


@dataclass(slots=True)
class HealthResponse:
    """
    Health check result.
    """

    provider: str
    status: str
    latency_ms: float