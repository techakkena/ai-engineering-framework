"""
Unit tests for validators constants.

Author: TECHAKKENA
"""

from ai_config.validators.constants import (
    DEFAULT_MAX_LENGTH,
    DEFAULT_MAX_VALUE,
    DEFAULT_MIN_LENGTH,
    DEFAULT_MIN_VALUE,
)


def test_default_min_length() -> None:
    """Test minimum length."""
    assert DEFAULT_MIN_LENGTH == 0


def test_default_max_length() -> None:
    """Test maximum length."""
    assert DEFAULT_MAX_LENGTH > DEFAULT_MIN_LENGTH


def test_default_min_value() -> None:
    """Test minimum value."""
    assert DEFAULT_MIN_VALUE == float("-inf")


def test_default_max_value() -> None:
    """Test maximum value."""
    assert DEFAULT_MAX_VALUE == float("inf")
