"""Tests for ai_enterprise.users.exceptions."""

from __future__ import annotations

import pytest

from ai_enterprise.users.exceptions import (
    DuplicateUserError,
    UnsupportedUserRoleError,
    UserError,
    UserNotFoundError,
    UserRegistrationError,
    UserValidationError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(UserValidationError, UserError)
    assert issubclass(UserRegistrationError, UserError)
    assert issubclass(
        UserNotFoundError,
        UserRegistrationError,
    )
    assert issubclass(
        DuplicateUserError,
        UserRegistrationError,
    )
    assert issubclass(
        UnsupportedUserRoleError,
        UserValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (UserError, "base"),
        (UserValidationError, "validation"),
        (UserRegistrationError, "registration"),
        (UserNotFoundError, "missing"),
        (DuplicateUserError, "duplicate"),
        (UnsupportedUserRoleError, "role"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(
        exception_class,
        match=message,
    ):
        raise exception_class(message)