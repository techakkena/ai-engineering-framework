from __future__ import annotations

from pathlib import Path

import pytest

from ai_tools.filesystem.exceptions import (
    FileSystemToolError,
)
from ai_tools.filesystem.operations import (
    FileSystemTool,
)


def test_exists(
    tmp_path: Path,
) -> None:
    tool = FileSystemTool()

    file_path = tmp_path / "test.txt"

    file_path.write_text("hello")

    assert tool.exists(file_path)


def test_write_and_read(
    tmp_path: Path,
) -> None:
    tool = FileSystemTool()

    file_path = tmp_path / "sample.txt"

    tool.write_text(
        file_path,
        "hello",
    )

    assert (
        tool.read_text(
            file_path,
        )
        == "hello"
    )


def test_missing_file() -> None:
    tool = FileSystemTool()

    with pytest.raises(
        FileSystemToolError,
    ):
        tool.read_text(
            "missing_file.txt",
        )
