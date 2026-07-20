from __future__ import annotations

from ai_rag.utils.operations import (
    is_empty,
    join_lines,
    normalize_text,
    unique_strings,
)


def test_is_empty():
    assert is_empty("")


def test_is_not_empty():
    assert not is_empty("hello")


def test_normalize_text():
    assert normalize_text("hello    world") == "hello world"


def test_join_lines():
    assert join_lines(
        ["a", "b", "c"]
    ) == "a\nb\nc"


def test_unique_strings():
    assert unique_strings(
        ["a", "b", "a", "c"]
    ) == ["a", "b", "c"]
