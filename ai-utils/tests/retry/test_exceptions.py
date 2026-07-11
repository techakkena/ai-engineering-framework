"""
Unit tests for retry exceptions.
"""

from __future__ import annotations

import pytest

from ai_utils.retry.exceptions import RetryError


def test_retry_error_is_exception() -> None:
    assert issubclass(RetryError, Exception)


def test_exception_can_be_raised() -> None:
    with pytest.raises(RetryError):
        raise RetryError("Retry failed")
