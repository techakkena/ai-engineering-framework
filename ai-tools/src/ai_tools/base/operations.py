from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_agents.tools.operations import (
    BaseTool,
    ToolInput,
    ToolOutput,
)

from .constants import ToolCategory


@dataclass(slots=True)
class ToolMetadata:
    """Metadata describing a tool."""

    name: str
    description: str
    category: ToolCategory


@dataclass(slots=True)
class ToolContext:
    """Runtime context for a tool."""

    variables: dict[str, Any] = field(
        default_factory=dict,
    )


class ToolImplementation(BaseTool):
    """Default tool implementation."""

    def __init__(
        self,
        metadata: ToolMetadata,
    ) -> None:
        self._metadata = metadata

    @property
    def name(self) -> str:
        return self._metadata.name

    @property
    def description(self) -> str:
        return self._metadata.description

    @property
    def category(self) -> ToolCategory:
        return self._metadata.category

    async def execute(
        self,
        tool_input: ToolInput,
    ) -> ToolOutput:
        return ToolOutput(
            result=tool_input.arguments,
        )
