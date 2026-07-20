from __future__ import annotations

from ai_tools.utils.operations import (
    build_tool_name,
    validate_tool_name,
)


def test_build_tool_name() -> None:
    assert build_tool_name("GitHub") == "tool_github"


def test_build_tool_name_spaces() -> None:
    assert build_tool_name("File System") == "tool_file_system"


def test_validate_tool_name() -> None:
    assert validate_tool_name("tool_http")


def test_validate_empty_name() -> None:
    assert not validate_tool_name("")


def test_validate_invalid_name() -> None:
    assert not validate_tool_name("tool-http")
