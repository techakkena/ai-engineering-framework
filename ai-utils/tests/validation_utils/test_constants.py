"""
Unit tests for validation constants.
"""

from __future__ import annotations

from ai_utils.validation_utils import constants


def test_email_pattern() -> None:
    assert constants.EMAIL_PATTERN


def test_url_pattern() -> None:
    assert constants.URL_PATTERN
