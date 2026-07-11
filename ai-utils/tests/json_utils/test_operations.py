"""
Unit tests for JSON operations.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from ai_utils.json_utils.exceptions import (
    JsonDecodeError,
    JsonReadError,
)
from ai_utils.json_utils.operations import (
    dumps,
    is_valid_json,
    loads,
    read_json,
    write_json,
)


def test_write_and_read_json(tmp_path: Path) -> None:
    """Write JSON to a file and read it back."""

    file_path = tmp_path / "sample.json"

    data = {
        "name": "OpenAI",
        "framework": "AI Engineering",
    }

    write_json(file_path, data)

    assert read_json(file_path) == data


def test_loads() -> None:
    """Deserialize a JSON string."""

    json_string = '{"name":"OpenAI","version":1}'

    data = loads(json_string)

    assert data["name"] == "OpenAI"
    assert data["version"] == 1


def test_dumps() -> None:
    """Serialize a dictionary."""

    data = {
        "framework": "AI",
    }

    json_string = dumps(data)

    assert '"framework"' in json_string
    assert '"AI"' in json_string


def test_is_valid_json_returns_true() -> None:
    """Valid JSON should return True."""

    assert is_valid_json('{"name":"OpenAI"}')


def test_is_valid_json_returns_false() -> None:
    """Invalid JSON should return False."""

    assert not is_valid_json("{invalid json}")


def test_read_missing_json_file(tmp_path: Path) -> None:
    """Reading a missing file should raise JsonReadError."""

    file_path = tmp_path / "missing.json"

    with pytest.raises(JsonReadError):
        read_json(file_path)


def test_invalid_json_file(tmp_path: Path) -> None:
    """Invalid JSON content should raise JsonDecodeError."""

    file_path = tmp_path / "invalid.json"

    file_path.write_text("{invalid json}")

    with pytest.raises(JsonDecodeError):
        read_json(file_path)


def test_invalid_json_string() -> None:
    """Invalid JSON string should raise JsonDecodeError."""

    with pytest.raises(JsonDecodeError):
        loads("{invalid json}")
