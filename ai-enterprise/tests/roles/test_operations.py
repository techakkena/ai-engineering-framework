"""Tests for ai_enterprise.roles.operations."""

from __future__ import annotations

import pytest

from ai_enterprise.roles.constants import (
    DEFAULT_ENABLED,
    DEFAULT_ROLE_NAME,
)
from ai_enterprise.roles.exceptions import (
    DuplicateRoleError,
    RoleNotFoundError,
    RoleValidationError,
    UnsupportedRoleError,
)
from ai_enterprise.roles.operations import (
    EnterpriseRole,
    RoleRegistry,
    build_role,
)


def test_role_defaults() -> None:
    role = EnterpriseRole()

    assert role.name == DEFAULT_ROLE_NAME
    assert role.permissions == ()
    assert role.description == ""
    assert role.enabled is DEFAULT_ENABLED


def test_role_trims_name() -> None:
    role = EnterpriseRole(
        name="  admin  ",
    )

    assert role.name == "admin"


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
        RoleValidationError,
    ):
        EnterpriseRole(
            name=name,
        )


def test_invalid_role_name() -> None:
    with pytest.raises(
        UnsupportedRoleError,
    ):
        EnterpriseRole(
            name="developer",
        )


def test_build_role() -> None:
    role = build_role(
        name="manager",
        permissions=(
            "users.read",
            "users.write",
        ),
        description="Manager role",
    )

    assert role.name == "manager"
    assert role.permissions == (
        "users.read",
        "users.write",
    )
    assert role.description == "Manager role"


def test_registry_register_and_get() -> None:
    registry = RoleRegistry()

    role = build_role(
        name="admin",
    )

    registry.register(role)

    assert registry.get("admin") is role
    assert registry.exists("admin")
    assert len(registry) == 1
    assert "admin" in registry


def test_registry_duplicate_registration() -> None:
    registry = RoleRegistry()

    role = build_role(
        name="admin",
    )

    registry.register(role)

    with pytest.raises(
        DuplicateRoleError,
    ):
        registry.register(role)


def test_registry_unregister() -> None:
    registry = RoleRegistry()

    role = build_role(
        name="admin",
    )

    registry.register(role)
    registry.unregister("admin")

    assert len(registry) == 0
    assert not registry.exists("admin")


def test_registry_unregister_missing() -> None:
    registry = RoleRegistry()

    with pytest.raises(
        RoleNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = RoleRegistry()

    with pytest.raises(
        RoleNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = RoleRegistry()

    registry.register(
        build_role(name="admin")
    )
    registry.register(
        build_role(name="viewer")
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = RoleRegistry()

    first = build_role(name="admin")
    second = build_role(name="viewer")

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = RoleRegistry()

    assert 123 not in registry