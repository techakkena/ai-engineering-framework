"""Tests for ai_testing.performance.exceptions."""

from __future__ import annotations

import pytest

from ai_testing.performance.exceptions import (
    InvalidIterationCountError,
    PerformanceError,
    PerformanceValidationError,
    UnsupportedTimeUnitError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(PerformanceValidationError, PerformanceError)
    assert issubclass(
        InvalidIterationCountError,
        PerformanceValidationError,
    )
    assert issubclass(
        UnsupportedTimeUnitError,
        PerformanceValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (PerformanceError, "base"),
        (PerformanceValidationError, "validation"),
        (InvalidIterationCountError, "iterations"),
        (UnsupportedTimeUnitError, "unit"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)