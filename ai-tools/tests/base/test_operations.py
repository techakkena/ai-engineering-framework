import pytest

from ai_agents.tools.operations import (
    ToolInput,
    ToolOutput,
)
from ai_tools.base.constants import (
    ToolCategory,
)
from ai_tools.base.operations import (
    ToolContext,
    ToolImplementation,
    ToolMetadata,
)


def test_metadata() -> None:
    metadata = ToolMetadata(
        name="http",
        description="HTTP Tool",
        category=ToolCategory.HTTP,
    )

    assert metadata.name == "http"
    assert metadata.category is ToolCategory.HTTP


def test_context() -> None:
    context = ToolContext()

    assert context.variables == {}


def test_tool_properties() -> None:
    tool = ToolImplementation(
        ToolMetadata(
            name="http",
            description="HTTP Tool",
            category=ToolCategory.HTTP,
        )
    )

    assert tool.name == "http"
    assert tool.description == "HTTP Tool"
    assert tool.category is ToolCategory.HTTP


@pytest.mark.asyncio
async def test_execute() -> None:
    tool = ToolImplementation(
        ToolMetadata(
            name="http",
            description="HTTP Tool",
            category=ToolCategory.HTTP,
        )
    )

    result = await tool.execute(
        ToolInput(
            arguments={
                "url": "https://example.com",
            }
        )
    )

    assert isinstance(
        result,
        ToolOutput,
    )

    assert result.result["url"] == "https://example.com"
