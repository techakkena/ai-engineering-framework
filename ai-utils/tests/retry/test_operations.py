"""
Unit tests for retry operations.
"""

from __future__ import annotations

import pytest

from ai_utils.retry.exceptions import RetryError
from ai_utils.retry.operations import (
    retry,
    retry_on_exception,
)


def test_retry_success() -> None:
    attempts = 0

    @retry(max_attempts=3, delay=0)
    def succeed() -> str:
        nonlocal attempts
        attempts += 1
        return "success"

    assert succeed() == "success"
    assert attempts == 1


def test_retry_eventual_success() -> None:
    attempts = 0

    @retry(max_attempts=3, delay=0)
    def sometimes_fails() -> str:
        nonlocal attempts
        attempts += 1

        if attempts < 2:
            raise ValueError("Temporary failure")

        return "success"

    assert sometimes_fails() == "success"
    assert attempts == 2


def test_retry_failure() -> None:
    @retry(max_attempts=2, delay=0)
    def always_fails() -> None:
        raise ValueError("Failure")

    with pytest.raises(RetryError):
        always_fails()


def test_retry_on_exception() -> None:
    attempts = 0

    def operation() -> str:
        nonlocal attempts
        attempts += 1

        if attempts < 2:
            raise ValueError("Temporary failure")

        return "done"

    result = retry_on_exception(
        operation,
        max_attempts=3,
        delay=0,
    )

    assert result == "done"
    assert attempts == 2
