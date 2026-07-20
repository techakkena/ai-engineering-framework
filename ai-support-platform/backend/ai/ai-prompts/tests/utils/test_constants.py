from __future__ import annotations

from ai_prompts.utils.constants import (
    DEFAULT_ENCODING,
    DEFAULT_LINE_SEPARATOR,
)


def test_default_encoding():
    assert DEFAULT_ENCODING == "utf-8"


def test_default_line_separator():
    assert DEFAULT_LINE_SEPARATOR == "\n"
