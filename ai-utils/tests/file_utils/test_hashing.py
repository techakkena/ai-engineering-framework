"""
Unit tests for hashing utilities.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from ai_utils.file_utils.exceptions import FileReadError
from ai_utils.file_utils.hashing import (
    calculate_hash,
    md5,
    sha256,
)


def test_sha256(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"

    content = "AI Engineering Framework"

    file_path.write_text(content)

    expected = hashlib.sha256(content.encode()).hexdigest()

    assert sha256(file_path) == expected


def test_md5(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"

    content = "AI Engineering Framework"

    file_path.write_text(content)

    expected = hashlib.md5(content.encode()).hexdigest()

    assert md5(file_path) == expected


def test_calculate_hash(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"

    content = "OpenAI"

    file_path.write_text(content)

    expected = hashlib.sha256(content.encode()).hexdigest()

    assert calculate_hash(file_path) == expected


def test_missing_file_raises_error(tmp_path: Path) -> None:
    file_path = tmp_path / "missing.txt"

    with pytest.raises(FileReadError):
        sha256(file_path)
