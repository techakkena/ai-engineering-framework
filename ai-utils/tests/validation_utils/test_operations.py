"""
Unit tests for validation operations.
"""

from __future__ import annotations

import uuid
from pathlib import Path

from ai_utils.validation_utils.operations import (
    is_email,
    is_file_path,
    is_json,
    is_non_empty,
    is_positive_integer,
    is_url,
    is_uuid,
    is_valid_length,
)


def test_is_email() -> None:
    assert is_email("user@example.com")
    assert not is_email("invalid-email")


def test_is_url() -> None:
    assert is_url("https://openai.com")
    assert is_url("http://example.com")
    assert not is_url("ftp://example.com")
    assert not is_url("invalid-url")


def test_is_uuid() -> None:
    value = str(uuid.uuid4())

    assert is_uuid(value)
    assert not is_uuid("invalid")


def test_is_non_empty() -> None:
    assert is_non_empty("OpenAI")
    assert not is_non_empty("")
    assert not is_non_empty("   ")


def test_is_positive_integer() -> None:
    assert is_positive_integer(1)
    assert is_positive_integer(100)
    assert not is_positive_integer(0)
    assert not is_positive_integer(-1)


def test_is_valid_length() -> None:
    assert is_valid_length("OpenAI", minimum=3)
    assert is_valid_length("OpenAI", minimum=3, maximum=10)
    assert not is_valid_length("AI", minimum=3)
    assert not is_valid_length("OpenAI", maximum=3)


def test_is_json() -> None:
    assert is_json('{"name":"OpenAI"}')
    assert is_json("[1, 2, 3]")
    assert not is_json("{invalid json}")


def test_is_file_path(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"

    file_path.write_text("AI Framework")

    assert is_file_path(file_path)
    assert not is_file_path(tmp_path / "missing.txt")
