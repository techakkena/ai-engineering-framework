from ai_agents.tools.constants import (
    DEFAULT_TOOL_DESCRIPTION,
    DEFAULT_TOOL_NAME,
)


def test_default_tool_name() -> None:
    assert DEFAULT_TOOL_NAME == "tool"


def test_default_tool_description() -> None:
    assert "Default" in DEFAULT_TOOL_DESCRIPTION
