"""
Unit tests for decorator exceptions.
"""

from __future__ import annotations

import pytest

from ai_utils.decorators.exceptions import DecoratorError


def test_decorator_error_is_exception() -> None:
    assert issubclass(DecoratorError, Exception)


def test_exception_can_be_raised() -> None:
    with pytest.raises(DecoratorError):
        raise DecoratorError("Test")
