"""Tests for ai_cloud.secrets.exceptions."""

from __future__ import annotations

import pytest

from ai_cloud.secrets.exceptions import (
    DuplicateSecretError,
    SecretError,
    SecretNotFoundError,
    SecretRegistrationError,
    SecretValidationError,
    UnsupportedSecretTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        SecretValidationError,
        SecretError,
    )
    assert issubclass(
        SecretRegistrationError,
        SecretError,
    )
    assert issubclass(
        SecretNotFoundError,
        SecretRegistrationError,
    )
    assert issubclass(
        DuplicateSecretError,
        SecretRegistrationError,
    )
    assert issubclass(
        UnsupportedSecretTypeError,
        SecretValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (SecretError, "base"),
        (SecretValidationError, "validation"),
        (SecretRegistrationError, "registration"),
        (SecretNotFoundError, "missing"),
        (DuplicateSecretError, "duplicate"),
        (UnsupportedSecretTypeError, "secret"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)