"""Tests for ai_enterprise.permissions.operations."""

from __future__ import annotations

import pytest

from ai_enterprise.permissions.constants import (
    DEFAULT_ENABLED,
    DEFAULT_PERMISSION_NAME,
    DEFAULT_RESOURCE,
)
from ai_enterprise.permissions.exceptions import (
    DuplicatePermissionError,
    PermissionNotFoundError,
    PermissionValidationError,
    UnsupportedPermissionError,
)
from ai_enterprise.permissions.operations import (
    EnterprisePermission,
    PermissionRegistry,
    build_permission,
)


def test_permission_defaults() -> None:
    permission = EnterprisePermission()

    assert permission.name == DEFAULT_PERMISSION_NAME
    assert permission.resource == DEFAULT_RESOURCE
    assert permission.description == ""
    assert permission.enabled is DEFAULT_ENABLED


def test_permission_trims_values() -> None:
    permission = EnterprisePermission(
        name="  read  ",
        resource="  users  ",
    )

    assert permission.name == "read"
    assert permission.resource == "users"


@pytest.mark.parametrize(
    "name",
    [
        "",
        " ",
        "abc",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        PermissionValidationError,
    ):
        EnterprisePermission(
            name=name,
            resource="users",
        )


@pytest.mark.parametrize(
    "resource",
    [
        "",
        "   ",
    ],
)
def test_invalid_resource(
    resource: str,
) -> None:
    with pytest.raises(
        PermissionValidationError,
    ):
        EnterprisePermission(
            name="read",
            resource=resource,
        )


def test_invalid_permission() -> None:
    with pytest.raises(
        UnsupportedPermissionError,
    ):
        EnterprisePermission(
            name="execute",
            resource="users",
        )


def test_build_permission() -> None:
    permission = build_permission(
        name="write",
        resource="documents",
        description="Write documents",
    )

    assert permission.name == "write"
    assert permission.resource == "documents"
    assert permission.description == "Write documents"


def test_registry_register_and_get() -> None:
    registry = PermissionRegistry()

    permission = build_permission(
        name="read",
        resource="users",
    )

    registry.register(permission)

    assert registry.get("read") is permission
    assert registry.exists("read")
    assert len(registry) == 1
    assert "read" in registry


def test_registry_duplicate_registration() -> None:
    registry = PermissionRegistry()

    permission = build_permission(
        name="read",
        resource="users",
    )

    registry.register(permission)

    with pytest.raises(
        DuplicatePermissionError,
    ):
        registry.register(permission)


def test_registry_unregister() -> None:
    registry = PermissionRegistry()

    permission = build_permission(
        name="read",
        resource="users",
    )

    registry.register(permission)
    registry.unregister("read")

    assert len(registry) == 0
    assert not registry.exists("read")


def test_registry_unregister_missing() -> None:
    registry = PermissionRegistry()

    with pytest.raises(
        PermissionNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = PermissionRegistry()

    with pytest.raises(
        PermissionNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = PermissionRegistry()

    registry.register(
        build_permission(
            name="read",
            resource="users",
        )
    )
    registry.register(
        build_permission(
            name="write",
            resource="users",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = PermissionRegistry()

    first = build_permission(
        name="read",
        resource="users",
    )
    second = build_permission(
        name="write",
        resource="users",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = PermissionRegistry()

    assert 123 not in registry