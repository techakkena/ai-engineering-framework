"""
Unit tests for retry constants.
"""

from __future__ import annotations

from ai_utils.retry import constants


def test_default_attempts() -> None:
    assert constants.DEFAULT_MAX_ATTEMPTS == 3


def test_default_delay() -> None:
    assert constants.DEFAULT_DELAY_SECONDS == 1.0
