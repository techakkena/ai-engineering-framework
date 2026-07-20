from __future__ import annotations

from ai_rag.utils.constants import (
    DEFAULT_ENCODING,
    DEFAULT_INDENT,
    DEFAULT_SEPARATOR,
)


def test_default_encoding():
    assert DEFAULT_ENCODING == "utf-8"


def test_default_separator():
    assert DEFAULT_SEPARATOR == "\n"


def test_default_indent():
    assert DEFAULT_INDENT == 4
