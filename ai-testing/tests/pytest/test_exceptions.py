"""Tests for ai_testing.pytest.exceptions."""

from __future__ import annotations

import pytest

from ai_testing.pytest.exceptions import (
    PytestError,
    PytestValidationError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(PytestValidationError, PytestError)


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (PytestError, "base"),
        (PytestValidationError, "validation"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)