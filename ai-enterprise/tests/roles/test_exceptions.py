"""Tests for ai_enterprise.roles.exceptions."""

from __future__ import annotations

import pytest

from ai_enterprise.roles.exceptions import (
    DuplicateRoleError,
    RoleError,
    RoleNotFoundError,
    RoleRegistrationError,
    RoleValidationError,
    UnsupportedRoleError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        RoleValidationError,
        RoleError,
    )
    assert issubclass(
        RoleRegistrationError,
        RoleError,
    )
    assert issubclass(
        RoleNotFoundError,
        RoleRegistrationError,
    )
    assert issubclass(
        DuplicateRoleError,
        RoleRegistrationError,
    )
    assert issubclass(
        UnsupportedRoleError,
        RoleValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (RoleError, "base"),
        (RoleValidationError, "validation"),
        (RoleRegistrationError, "registration"),
        (RoleNotFoundError, "missing"),
        (DuplicateRoleError, "duplicate"),
        (UnsupportedRoleError, "role"),
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