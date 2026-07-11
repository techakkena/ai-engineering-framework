"""
Unit tests for string utility operations.
"""

from __future__ import annotations

from ai_utils.string_utils.operations import (
    capitalize_words,
    is_blank,
    normalize_whitespace,
    remove_whitespace,
    reverse,
    to_camel_case,
    to_pascal_case,
    to_snake_case,
    truncate,
)


def test_is_blank() -> None:
    assert is_blank("")
    assert is_blank("   ")
    assert not is_blank("OpenAI")


def test_to_snake_case() -> None:
    assert to_snake_case("Hello World") == "hello_world"
    assert to_snake_case("helloWorld") == "hello_world"


def test_to_pascal_case() -> None:
    assert to_pascal_case("hello_world") == "HelloWorld"


def test_to_camel_case() -> None:
    assert to_camel_case("hello_world") == "helloWorld"


def test_truncate() -> None:
    assert truncate("Hello World", 5) == "Hello..."
    assert truncate("Hello", 10) == "Hello"


def test_remove_whitespace() -> None:
    assert remove_whitespace(" A B C ") == "ABC"


def test_normalize_whitespace() -> None:
    assert normalize_whitespace("A   B\tC") == "A B C"


def test_reverse() -> None:
    assert reverse("OpenAI") == "IAnepO"


def test_capitalize_words() -> None:
    assert capitalize_words("hello world") == "Hello World"
