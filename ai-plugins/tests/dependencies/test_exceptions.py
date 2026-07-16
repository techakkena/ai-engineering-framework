"""Tests for ai_plugins.dependencies.exceptions."""

from __future__ import annotations

import pytest

from ai_plugins.dependencies.exceptions import (
    DependencyError,
    DependencyNotFoundError,
    DependencyRegistrationError,
    DependencyValidationError,
    DuplicateDependencyError,
    UnsupportedDependencyTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        DependencyValidationError,
        DependencyError,
    )
    assert issubclass(
        DependencyRegistrationError,
        DependencyError,
    )
    assert issubclass(
        DependencyNotFoundError,
        DependencyRegistrationError,
    )
    assert issubclass(
        DuplicateDependencyError,
        DependencyRegistrationError,
    )
    assert issubclass(
        UnsupportedDependencyTypeError,
        DependencyValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (DependencyError, "base"),
        (DependencyValidationError, "validation"),
        (DependencyRegistrationError, "registration"),
        (DependencyNotFoundError, "missing"),
        (DuplicateDependencyError, "duplicate"),
        (UnsupportedDependencyTypeError, "type"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)