"""
Unit tests for JSON constants.
"""

from __future__ import annotations

from ai_utils.json_utils import constants


def test_default_encoding() -> None:
    assert constants.DEFAULT_ENCODING == "utf-8"


def test_default_indent() -> None:
    assert constants.DEFAULT_INDENT == 4


def test_default_ensure_ascii() -> None:
    assert constants.DEFAULT_ENSURE_ASCII is False


def test_default_sort_keys() -> None:
    assert constants.DEFAULT_SORT_KEYS is False
