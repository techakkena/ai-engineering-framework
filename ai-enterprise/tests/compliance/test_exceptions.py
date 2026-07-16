"""Tests for ai_enterprise.compliance.exceptions."""

from __future__ import annotations

import pytest

from ai_enterprise.compliance.exceptions import (
    ComplianceError,
    ComplianceNotFoundError,
    ComplianceRegistrationError,
    ComplianceValidationError,
    DuplicateComplianceError,
    UnsupportedComplianceStandardError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        ComplianceValidationError,
        ComplianceError,
    )
    assert issubclass(
        ComplianceRegistrationError,
        ComplianceError,
    )
    assert issubclass(
        ComplianceNotFoundError,
        ComplianceRegistrationError,
    )
    assert issubclass(
        DuplicateComplianceError,
        ComplianceRegistrationError,
    )
    assert issubclass(
        UnsupportedComplianceStandardError,
        ComplianceValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (ComplianceError, "base"),
        (ComplianceValidationError, "validation"),
        (ComplianceRegistrationError, "registration"),
        (ComplianceNotFoundError, "missing"),
        (DuplicateComplianceError, "duplicate"),
        (
            UnsupportedComplianceStandardError,
            "standard",
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