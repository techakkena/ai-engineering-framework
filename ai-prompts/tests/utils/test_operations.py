from ai_prompts.utils.operations import (
    count_lines,
    ensure_trailing_newline,
    is_blank,
    normalize_text,
)


def test_normalize_text():
    assert normalize_text("Hello    World") == "Hello World"


def test_is_blank():
    assert is_blank("   ")
    assert not is_blank("Hello")


def test_ensure_trailing_newline():
    assert ensure_trailing_newline("Hello") == "Hello\n"


def test_existing_trailing_newline():
    assert ensure_trailing_newline("Hello\n") == "Hello\n"


def test_count_lines():
    assert count_lines("A\nB\nC") == 3


def test_empty_line_count():
    assert count_lines("") == 0
