"""
Unit tests for path utilities.
"""

from __future__ import annotations

from pathlib import Path

from ai_utils.file_utils.paths import (
    ensure_directory,
    get_extension,
    get_filename,
    get_stem,
    resolve_path,
)


def test_ensure_directory(tmp_path: Path) -> None:
    directory = tmp_path / "nested" / "folder"

    result = ensure_directory(directory)

    assert result.exists()
    assert result.is_dir()


def test_resolve_path(tmp_path: Path) -> None:
    result = resolve_path(tmp_path)

    assert result.is_absolute()


def test_get_filename() -> None:
    assert get_filename("data/sample.txt") == "sample.txt"


def test_get_stem() -> None:
    assert get_stem("data/sample.txt") == "sample"


def test_get_extension() -> None:
    assert get_extension("data/sample.txt") == ".txt"
