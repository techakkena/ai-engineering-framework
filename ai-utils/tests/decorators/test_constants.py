"""
Unit tests for decorator constants.
"""

from __future__ import annotations

from ai_utils.decorators import constants


def test_default_deprecation_message() -> None:
    assert constants.DEFAULT_DEPRECATION_MESSAGE
