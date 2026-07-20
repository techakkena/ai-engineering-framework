from __future__ import annotations

import pytest

from ai_agents.tools.operations import (
    BaseTool,
    ToolInput,
    ToolOutput,
)


class EchoTool(BaseTool):
    @property
    def name(self) -> str:
        return "echo"

    @property
    def description(self) -> str:
        return "Echo tool"

    async def execute(
        self,
        tool_input: ToolInput,
    ) -> ToolOutput:
        return ToolOutput(
            result=tool_input.arguments,
        )


def test_tool_input() -> None:
    tool_input = ToolInput()

    assert tool_input.arguments == {}


def test_tool_output() -> None:
    output = ToolOutput(result="hello")

    assert output.result == "hello"
    assert output.metadata == {}


def test_tool_properties() -> None:
    tool = EchoTool()

    assert tool.name == "echo"
    assert tool.description == "Echo tool"


@pytest.mark.asyncio
async def test_tool_execution() -> None:
    tool = EchoTool()

    output = await tool.execute(
        ToolInput(
            arguments={"message": "hello"},
        )
    )

    assert output.result["message"] == "hello"
