"""
Tests for ai_security.permissions.operations.
"""

import pytest

from ai_security.permissions.exceptions import (
    PermissionDeniedError,
    RoleNotFoundError,
)
from ai_security.permissions.operations import (
    Permission,
    PermissionManager,
    Role,
)


def test_add_and_get_role() -> None:
    """A role should be registered and retrieved."""
    manager = PermissionManager()
    role = Role(name="admin")

    manager.add_role(role)

    retrieved = manager.get_role("admin")

    assert retrieved is role
    assert manager.role_count == 1


def test_get_missing_role() -> None:
    """Retrieving a missing role should raise an exception."""
    manager = PermissionManager()

    with pytest.raises(RoleNotFoundError):
        manager.get_role("missing")


def test_grant_permission() -> None:
    """Granting a permission should update the role."""
    manager = PermissionManager()
    role = Role(name="editor")

    manager.add_role(role)
    manager.grant_permission("editor", "document:write")

    assert "document:write" in role.permissions


def test_revoke_permission() -> None:
    """Revoking a permission should remove it."""
    manager = PermissionManager()
    role = Role(
        name="editor",
        permissions={"document:write"},
    )

    manager.add_role(role)
    manager.revoke_permission(
        "editor",
        "document:write",
    )

    assert "document:write" not in role.permissions


def test_has_permission_success() -> None:
    """Permission lookup should succeed."""
    manager = PermissionManager()
    role = Role(
        name="admin",
        permissions={"users:create"},
    )

    manager.add_role(role)

    assert manager.has_permission(
        "admin",
        "users:create",
    )


def test_has_permission_denied() -> None:
    """Missing permission should raise an exception."""
    manager = PermissionManager()
    role = Role(name="viewer")

    manager.add_role(role)

    with pytest.raises(PermissionDeniedError):
        manager.has_permission(
            "viewer",
            "users:delete",
        )


def test_wildcard_permission() -> None:
    """Wildcard permission should authorize everything."""
    manager = PermissionManager()
    role = Role(
        name="super-admin",
        permissions={"*"},
    )

    manager.add_role(role)

    assert manager.has_permission(
        "super-admin",
        "anything",
    )


def test_permission_dataclass() -> None:
    """Permission dataclass should retain its name."""
    permission = Permission(
        name="reports:read",
    )

    assert permission.name == "reports:read"


def test_default_role() -> None:
    """Role should default to the configured default role."""
    role = Role()

    assert role.name == "user"
    assert role.permissions == set()


def test_multiple_roles() -> None:
    """Multiple roles should be tracked."""
    manager = PermissionManager()

    manager.add_role(Role(name="admin"))
    manager.add_role(Role(name="editor"))
    manager.add_role(Role(name="viewer"))

    assert manager.role_count == 3