"""Tests for ai_enterprise.policies.exceptions."""

from __future__ import annotations

import pytest

from ai_enterprise.policies.exceptions import (
    DuplicatePolicyError,
    PolicyError,
    PolicyNotFoundError,
    PolicyRegistrationError,
    PolicyValidationError,
    UnsupportedPolicyTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        PolicyValidationError,
        PolicyError,
    )
    assert issubclass(
        PolicyRegistrationError,
        PolicyError,
    )
    assert issubclass(
        PolicyNotFoundError,
        PolicyRegistrationError,
    )
    assert issubclass(
        DuplicatePolicyError,
        PolicyRegistrationError,
    )
    assert issubclass(
        UnsupportedPolicyTypeError,
        PolicyValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (PolicyError, "base"),
        (PolicyValidationError, "validation"),
        (PolicyRegistrationError, "registration"),
        (PolicyNotFoundError, "missing"),
        (DuplicatePolicyError, "duplicate"),
        (UnsupportedPolicyTypeError, "policy"),
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