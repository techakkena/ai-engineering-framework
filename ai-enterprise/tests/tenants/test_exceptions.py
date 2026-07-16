"""Tests for ai_enterprise.tenants.exceptions."""

from __future__ import annotations

import pytest

from ai_enterprise.tenants.exceptions import (
    DuplicateTenantError,
    TenantError,
    TenantNotFoundError,
    TenantRegistrationError,
    TenantValidationError,
    UnsupportedTenantPlanError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        TenantValidationError,
        TenantError,
    )
    assert issubclass(
        TenantRegistrationError,
        TenantError,
    )
    assert issubclass(
        TenantNotFoundError,
        TenantRegistrationError,
    )
    assert issubclass(
        DuplicateTenantError,
        TenantRegistrationError,
    )
    assert issubclass(
        UnsupportedTenantPlanError,
        TenantValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (TenantError, "base"),
        (TenantValidationError, "validation"),
        (TenantRegistrationError, "registration"),
        (TenantNotFoundError, "missing"),
        (DuplicateTenantError, "duplicate"),
        (UnsupportedTenantPlanError, "plan"),
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