"""Tests for ai_cloud.authentication.exceptions."""

from __future__ import annotations

import pytest

from ai_cloud.authentication.exceptions import (
    AuthenticationError,
    AuthenticationNotFoundError,
    AuthenticationRegistrationError,
    AuthenticationValidationError,
    DuplicateAuthenticationError,
    UnsupportedAuthenticationTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        AuthenticationValidationError,
        AuthenticationError,
    )
    assert issubclass(
        AuthenticationRegistrationError,
        AuthenticationError,
    )
    assert issubclass(
        AuthenticationNotFoundError,
        AuthenticationRegistrationError,
    )
    assert issubclass(
        DuplicateAuthenticationError,
        AuthenticationRegistrationError,
    )
    assert issubclass(
        UnsupportedAuthenticationTypeError,
        AuthenticationValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (AuthenticationError, "base"),
        (
            AuthenticationValidationError,
            "validation",
        ),
        (
            AuthenticationRegistrationError,
            "registration",
        ),
        (
            AuthenticationNotFoundError,
            "missing",
        ),
        (
            DuplicateAuthenticationError,
            "duplicate",
        ),
        (
            UnsupportedAuthenticationTypeError,
            "authentication",
        ),
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