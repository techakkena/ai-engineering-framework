"""Tests for ai_testing.assertions.exceptions."""

from __future__ import annotations

import pytest

from ai_testing.assertions.exceptions import (
    AssertionErrorBase,
    AssertionExecutionError,
    AssertionValidationError,
    UnsupportedAssertionStatusError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(AssertionValidationError, AssertionErrorBase)
    assert issubclass(AssertionExecutionError, AssertionErrorBase)
    assert issubclass(
        UnsupportedAssertionStatusError,
        AssertionValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (AssertionErrorBase, "base"),
        (AssertionValidationError, "validation"),
        (AssertionExecutionError, "execution"),
        (UnsupportedAssertionStatusError, "status"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)