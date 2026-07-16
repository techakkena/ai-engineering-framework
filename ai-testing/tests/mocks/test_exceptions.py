"""Tests for ai_testing.mocks.exceptions."""

from __future__ import annotations

import pytest

from ai_testing.mocks.exceptions import (
    DuplicateMockError,
    MockError,
    MockNotFoundError,
    MockRegistrationError,
    MockValidationError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(MockValidationError, MockError)
    assert issubclass(MockRegistrationError, MockError)
    assert issubclass(MockNotFoundError, MockRegistrationError)
    assert issubclass(DuplicateMockError, MockRegistrationError)


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (MockError, "base"),
        (MockValidationError, "validation"),
        (MockRegistrationError, "registration"),
        (MockNotFoundError, "missing"),
        (DuplicateMockError, "duplicate"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)