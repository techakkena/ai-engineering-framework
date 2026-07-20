from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ToolInput:
    """Input supplied to a tool."""

    arguments: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ToolOutput:
    """Output returned by a tool."""

    result: Any
    metadata: dict[str, Any] = field(default_factory=dict)


class BaseTool(ABC):
    """Abstract base class for all tools."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the tool name."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Return the tool description."""

    @abstractmethod
    async def execute(
        self,
        tool_input: ToolInput,
    ) -> ToolOutput:
        """Execute the tool."""
