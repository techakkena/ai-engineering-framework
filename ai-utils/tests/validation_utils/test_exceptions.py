"""
Unit tests for validation exceptions.
"""

from __future__ import annotations

import pytest

from ai_utils.validation_utils.exceptions import (
    ValidationUtilsError,
)


def test_validation_utils_error_is_exception() -> None:
    assert issubclass(ValidationUtilsError, Exception)


def test_exception_can_be_raised() -> None:
    with pytest.raises(ValidationUtilsError):
        raise ValidationUtilsError("Test")
