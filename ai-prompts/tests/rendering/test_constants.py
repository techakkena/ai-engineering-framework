from ai_prompts.rendering.constants import (
    DEFAULT_END_DELIMITER,
    DEFAULT_START_DELIMITER,
)


def test_default_start_delimiter():
    assert DEFAULT_START_DELIMITER == "{{"


def test_default_end_delimiter():
    assert DEFAULT_END_DELIMITER == "}}"
