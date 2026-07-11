"""
Unit tests for string utility exceptions.
"""

from __future__ import annotations

import pytest

from ai_utils.string_utils.exceptions import StringUtilsError


def test_string_utils_error_is_exception() -> None:
    assert issubclass(StringUtilsError, Exception)


def test_exception_can_be_raised() -> None:
    with pytest.raises(StringUtilsError):
        raise StringUtilsError("Test exception")
