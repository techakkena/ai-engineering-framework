"""Tests for ai_optimization.profiling.exceptions."""

from __future__ import annotations

import pytest

from ai_optimization.profiling.exceptions import (
    DuplicateProfileError,
    ProfileError,
    ProfileNotFoundError,
    ProfileRegistrationError,
    ProfileValidationError,
    UnsupportedProfileTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(ProfileValidationError, ProfileError)
    assert issubclass(
        ProfileRegistrationError,
        ProfileError,
    )
    assert issubclass(
        ProfileNotFoundError,
        ProfileRegistrationError,
    )
    assert issubclass(
        DuplicateProfileError,
        ProfileRegistrationError,
    )
    assert issubclass(
        UnsupportedProfileTypeError,
        ProfileValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (ProfileError, "base"),
        (ProfileValidationError, "validation"),
        (ProfileRegistrationError, "registration"),
        (ProfileNotFoundError, "missing"),
        (DuplicateProfileError, "duplicate"),
        (UnsupportedProfileTypeError, "type"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)