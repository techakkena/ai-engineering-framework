"""Tests for ai_enterprise.permissions.exceptions."""

from __future__ import annotations

import pytest

from ai_enterprise.permissions.exceptions import (
    DuplicatePermissionError,
    PermissionError,
    PermissionNotFoundError,
    PermissionRegistrationError,
    PermissionValidationError,
    UnsupportedPermissionError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        PermissionValidationError,
        PermissionError,
    )
    assert issubclass(
        PermissionRegistrationError,
        PermissionError,
    )
    assert issubclass(
        PermissionNotFoundError,
        PermissionRegistrationError,
    )
    assert issubclass(
        DuplicatePermissionError,
        PermissionRegistrationError,
    )
    assert issubclass(
        UnsupportedPermissionError,
        PermissionValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (PermissionError, "base"),
        (PermissionValidationError, "validation"),
        (PermissionRegistrationError, "registration"),
        (PermissionNotFoundError, "missing"),
        (DuplicatePermissionError, "duplicate"),
        (UnsupportedPermissionError, "permission"),
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