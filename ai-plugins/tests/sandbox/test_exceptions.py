"""Tests for ai_plugins.sandbox.exceptions."""

from __future__ import annotations

import pytest

from ai_plugins.sandbox.exceptions import (
    DuplicateSandboxError,
    SandboxError,
    SandboxNotFoundError,
    SandboxRegistrationError,
    SandboxValidationError,
    UnsupportedSandboxModeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        SandboxValidationError,
        SandboxError,
    )
    assert issubclass(
        SandboxRegistrationError,
        SandboxError,
    )
    assert issubclass(
        SandboxNotFoundError,
        SandboxRegistrationError,
    )
    assert issubclass(
        DuplicateSandboxError,
        SandboxRegistrationError,
    )
    assert issubclass(
        UnsupportedSandboxModeError,
        SandboxValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (SandboxError, "base"),
        (SandboxValidationError, "validation"),
        (SandboxRegistrationError, "registration"),
        (SandboxNotFoundError, "missing"),
        (DuplicateSandboxError, "duplicate"),
        (UnsupportedSandboxModeError, "mode"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)