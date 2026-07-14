from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class AgentMemory(ABC):
    """Abstract interface for agent memory."""

    @abstractmethod
    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """Store a value."""

    @abstractmethod
    def get(
        self,
        key: str,
    ) -> Any:
        """Retrieve a value."""

    @abstractmethod
    def clear(self) -> None:
        """Clear memory."""


class InMemoryAgentMemory(AgentMemory):
    """Simple in-memory implementation."""

    def __init__(self) -> None:
        self._memory: dict[str, Any] = {}

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        self._memory[key] = value

    def get(
        self,
        key: str,
    ) -> Any:
        return self._memory.get(key)

    def clear(self) -> None:
        self._memory.clear()

    def __len__(self) -> int:
        return len(self._memory)
