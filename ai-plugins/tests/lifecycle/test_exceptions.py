"""Tests for ai_plugins.lifecycle.exceptions."""

from __future__ import annotations

import pytest

from ai_plugins.lifecycle.exceptions import (
    DuplicateLifecycleError,
    LifecycleError,
    LifecycleNotFoundError,
    LifecycleRegistrationError,
    LifecycleValidationError,
    UnsupportedLifecyclePhaseError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        LifecycleValidationError,
        LifecycleError,
    )
    assert issubclass(
        LifecycleRegistrationError,
        LifecycleError,
    )
    assert issubclass(
        LifecycleNotFoundError,
        LifecycleRegistrationError,
    )
    assert issubclass(
        DuplicateLifecycleError,
        LifecycleRegistrationError,
    )
    assert issubclass(
        UnsupportedLifecyclePhaseError,
        LifecycleValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (LifecycleError, "base"),
        (LifecycleValidationError, "validation"),
        (LifecycleRegistrationError, "registration"),
        (LifecycleNotFoundError, "missing"),
        (DuplicateLifecycleError, "duplicate"),
        (UnsupportedLifecyclePhaseError, "phase"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)