"""Tests for ai_enterprise.organizations.exceptions."""

from __future__ import annotations

import pytest

from ai_enterprise.organizations.exceptions import (
    DuplicateOrganizationError,
    OrganizationError,
    OrganizationNotFoundError,
    OrganizationRegistrationError,
    OrganizationValidationError,
    UnsupportedOrganizationTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        OrganizationValidationError,
        OrganizationError,
    )
    assert issubclass(
        OrganizationRegistrationError,
        OrganizationError,
    )
    assert issubclass(
        OrganizationNotFoundError,
        OrganizationRegistrationError,
    )
    assert issubclass(
        DuplicateOrganizationError,
        OrganizationRegistrationError,
    )
    assert issubclass(
        UnsupportedOrganizationTypeError,
        OrganizationValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (OrganizationError, "base"),
        (OrganizationValidationError, "validation"),
        (OrganizationRegistrationError, "registration"),
        (OrganizationNotFoundError, "missing"),
        (DuplicateOrganizationError, "duplicate"),
        (UnsupportedOrganizationTypeError, "type"),
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