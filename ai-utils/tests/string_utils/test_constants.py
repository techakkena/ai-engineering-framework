"""
Unit tests for string utility constants.
"""

from __future__ import annotations

from ai_utils.string_utils import constants


def test_default_truncate_suffix() -> None:
    assert constants.DEFAULT_TRUNCATE_SUFFIX == "..."
