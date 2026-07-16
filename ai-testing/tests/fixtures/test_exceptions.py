"""Tests for ai_testing.fixtures.exceptions."""

from __future__ import annotations

import pytest

from ai_testing.fixtures.exceptions import (
    DuplicateFixtureError,
    FixtureError,
    FixtureNotFoundError,
    FixtureRegistrationError,
    FixtureValidationError,
    UnsupportedFixtureScopeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(FixtureValidationError, FixtureError)
    assert issubclass(FixtureRegistrationError, FixtureError)
    assert issubclass(FixtureNotFoundError, FixtureError)
    assert issubclass(DuplicateFixtureError, FixtureRegistrationError)
    assert issubclass(
        UnsupportedFixtureScopeError,
        FixtureValidationError,
    )


@pytest.mark.parametrize(
    ("exception_cls", "message"),
    [
        (FixtureError, "fixture"),
        (FixtureValidationError, "validation"),
        (FixtureRegistrationError, "registration"),
        (FixtureNotFoundError, "missing"),
        (DuplicateFixtureError, "duplicate"),
        (UnsupportedFixtureScopeError, "scope"),
    ],
)
def test_exception_message(
    exception_cls: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_cls, match=message):
        raise exception_cls(message)