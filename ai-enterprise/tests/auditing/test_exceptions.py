"""Tests for ai_enterprise.auditing.exceptions."""

from __future__ import annotations

import pytest

from ai_enterprise.auditing.exceptions import (
    AuditError,
    AuditNotFoundError,
    AuditRegistrationError,
    AuditValidationError,
    DuplicateAuditError,
    UnsupportedAuditLevelError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        AuditValidationError,
        AuditError,
    )
    assert issubclass(
        AuditRegistrationError,
        AuditError,
    )
    assert issubclass(
        AuditNotFoundError,
        AuditRegistrationError,
    )
    assert issubclass(
        DuplicateAuditError,
        AuditRegistrationError,
    )
    assert issubclass(
        UnsupportedAuditLevelError,
        AuditValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (AuditError, "base"),
        (AuditValidationError, "validation"),
        (AuditRegistrationError, "registration"),
        (AuditNotFoundError, "missing"),
        (DuplicateAuditError, "duplicate"),
        (UnsupportedAuditLevelError, "level"),
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