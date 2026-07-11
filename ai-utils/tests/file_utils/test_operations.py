"""
Unit tests for file operations.
"""

from __future__ import annotations

from pathlib import Path
from typing import cast

import pytest

from ai_utils.file_utils.exceptions import (
    FileReadError,
    FileWriteError,
)
from ai_utils.file_utils.operations import (
    append_text,
    file_exists,
    read_bytes,
    read_text,
    write_bytes,
    write_text,
)


def test_write_and_read_text(tmp_path: Path) -> None:
    """Write and read a text file."""

    file_path = tmp_path / "sample.txt"

    write_text(file_path, "Hello AI Framework")

    assert read_text(file_path) == "Hello AI Framework"


def test_append_text(tmp_path: Path) -> None:
    """Append text to an existing file."""

    file_path = tmp_path / "append.txt"

    write_text(file_path, "Hello")
    append_text(file_path, " World")

    assert read_text(file_path) == "Hello World"


def test_write_and_read_bytes(tmp_path: Path) -> None:
    """Write and read binary data."""

    file_path = tmp_path / "binary.bin"

    data = b"\x00\x01\x02\x03"

    write_bytes(file_path, data)

    assert read_bytes(file_path) == data


def test_file_exists_returns_true(tmp_path: Path) -> None:
    """file_exists should return True for existing files."""

    file_path = tmp_path / "exists.txt"

    write_text(file_path, "exists")

    assert file_exists(file_path) is True


def test_file_exists_returns_false(tmp_path: Path) -> None:
    """file_exists should return False for missing files."""

    file_path = tmp_path / "missing.txt"

    assert file_exists(file_path) is False


def test_read_missing_file_raises_error(tmp_path: Path) -> None:
    """Reading a missing file should raise FileReadError."""

    file_path = tmp_path / "missing.txt"

    with pytest.raises(FileReadError):
        read_text(file_path)


def test_write_creates_parent_directory(tmp_path: Path) -> None:
    """write_text should automatically create parent directories."""

    file_path = tmp_path / "level1" / "level2" / "sample.txt"

    write_text(file_path, "Directory created")

    assert file_path.exists()
    assert read_text(file_path) == "Directory created"


def test_write_bytes_creates_parent_directory(tmp_path: Path) -> None:
    """write_bytes should automatically create parent directories."""

    file_path = tmp_path / "binary" / "data.bin"

    data = b"framework"

    write_bytes(file_path, data)

    assert file_path.exists()
    assert read_bytes(file_path) == data


def test_append_creates_parent_directory(tmp_path: Path) -> None:
    """append_text should create missing parent directories."""

    file_path = tmp_path / "logs" / "app.log"

    append_text(file_path, "First line")

    assert read_text(file_path) == "First line"


def test_write_text_invalid_path_raises_error() -> None:
    """Invalid path should raise FileWriteError."""

    invalid_path = cast(str, None)

    with pytest.raises(FileWriteError):
        write_text(invalid_path, "invalid")


def test_read_text_invalid_path_raises_error() -> None:
    """Invalid path should raise FileReadError."""

    invalid_path = cast(str, None)

    with pytest.raises(FileReadError):
        read_text(invalid_path)
