"""Tests for ai_plugins.validation.exceptions."""

from __future__ import annotations

import pytest

from ai_plugins.validation.exceptions import (
    DuplicateValidationError,
    UnsupportedValidationLevelError,
    ValidationDefinitionError,
    ValidationError,
    ValidationNotFoundError,
    ValidationRegistrationError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        ValidationDefinitionError,
        ValidationError,
    )
    assert issubclass(
        ValidationRegistrationError,
        ValidationError,
    )
    assert issubclass(
        ValidationNotFoundError,
        ValidationRegistrationError,
    )
    assert issubclass(
        DuplicateValidationError,
        ValidationRegistrationError,
    )
    assert issubclass(
        UnsupportedValidationLevelError,
        ValidationDefinitionError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (ValidationError, "base"),
        (ValidationDefinitionError, "validation"),
        (ValidationRegistrationError, "registration"),
        (ValidationNotFoundError, "missing"),
        (DuplicateValidationError, "duplicate"),
        (UnsupportedValidationLevelError, "level"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)