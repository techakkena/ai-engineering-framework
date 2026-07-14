from ai_tools.utils.constants import (
    DEFAULT_TOOL_PREFIX,
)


def test_default_tool_prefix() -> None:
    assert DEFAULT_TOOL_PREFIX == "tool"
