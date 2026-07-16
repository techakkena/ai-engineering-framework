"""Tests for ai_enterprise.policies.operations."""

from __future__ import annotations

import pytest

from ai_enterprise.policies.constants import (
    DEFAULT_ENABLED,
    DEFAULT_POLICY_TYPE,
)
from ai_enterprise.policies.exceptions import (
    DuplicatePolicyError,
    PolicyNotFoundError,
    PolicyValidationError,
    UnsupportedPolicyTypeError,
)
from ai_enterprise.policies.operations import (
    EnterprisePolicy,
    PolicyRegistry,
    build_policy,
)


def test_policy_defaults() -> None:
    policy = EnterprisePolicy(
        name="default",
    )

    assert policy.name == "default"
    assert policy.policy_type == DEFAULT_POLICY_TYPE
    assert policy.rules == ()
    assert policy.description == ""
    assert policy.enabled is DEFAULT_ENABLED


def test_policy_trims_name() -> None:
    policy = EnterprisePolicy(
        name="  default  ",
    )

    assert policy.name == "default"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "  ",
        "ab",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        PolicyValidationError,
    ):
        EnterprisePolicy(
            name=name,
        )


def test_invalid_policy_type() -> None:
    with pytest.raises(
        UnsupportedPolicyTypeError,
    ):
        EnterprisePolicy(
            name="default",
            policy_type="privacy",
        )


def test_build_policy() -> None:
    policy = build_policy(
        name="security",
        policy_type="security",
        rules=(
            "mfa_required",
            "password_rotation",
        ),
        description="Security policy",
    )

    assert policy.name == "security"
    assert policy.policy_type == "security"
    assert policy.rules == (
        "mfa_required",
        "password_rotation",
    )
    assert policy.description == "Security policy"


def test_registry_register_and_get() -> None:
    registry = PolicyRegistry()

    policy = build_policy(
        name="default",
    )

    registry.register(policy)

    assert registry.get("default") is policy
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = PolicyRegistry()

    policy = build_policy(
        name="default",
    )

    registry.register(policy)

    with pytest.raises(
        DuplicatePolicyError,
    ):
        registry.register(policy)


def test_registry_unregister() -> None:
    registry = PolicyRegistry()

    policy = build_policy(
        name="default",
    )

    registry.register(policy)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = PolicyRegistry()

    with pytest.raises(
        PolicyNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = PolicyRegistry()

    with pytest.raises(
        PolicyNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = PolicyRegistry()

    registry.register(
        build_policy(
            name="default",
        )
    )
    registry.register(
        build_policy(
            name="security",
            policy_type="security",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = PolicyRegistry()

    first = build_policy(
        name="default",
    )
    second = build_policy(
        name="security",
        policy_type="security",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = PolicyRegistry()

    assert 123 not in registry