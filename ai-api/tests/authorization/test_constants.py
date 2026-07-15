"""
Unit tests for ai_api.authorization.constants.
"""

from __future__ import annotations

from ai_api.authorization.constants import (
    ADMIN_PERMISSION,
    ADMIN_ROLE,
    ALL_PERMISSIONS,
    ALLOW_POLICY,
    ANY_RESOURCE,
    DEFAULT_POLICY,
    DEFAULT_ROLE,
    DEFAULT_SCOPE,
    DELETE_PERMISSION,
    DENY_POLICY,
    EXECUTE_PERMISSION,
    GUEST_ROLE,
    PERMISSION_SEPARATOR,
    READ_PERMISSION,
    ROLE_HIERARCHY,
    ROLE_SEPARATOR,
    SUPERUSER_ROLE,
    SUPPORTED_PERMISSIONS,
    SUPPORTED_ROLES,
    SUPPORTED_SCOPES,
    SYSTEM_ROLE,
    UPDATE_PERMISSION,
    WRITE_PERMISSION,
)


def test_default_roles() -> None:
    """Test default role constants."""
    assert DEFAULT_ROLE == "user"
    assert ADMIN_ROLE == "admin"
    assert SUPERUSER_ROLE == "superuser"
    assert GUEST_ROLE == "guest"
    assert SYSTEM_ROLE == "system"


def test_supported_roles() -> None:
    """Test supported roles."""
    expected = {
        "user",
        "admin",
        "superuser",
        "guest",
        "system",
    }

    assert SUPPORTED_ROLES == expected


def test_supported_roles_are_immutable() -> None:
    """Supported roles should be immutable."""
    assert isinstance(
        SUPPORTED_ROLES,
        frozenset,
    )


def test_default_scope() -> None:
    """Test default scope."""
    assert DEFAULT_SCOPE == "read"


def test_supported_scopes() -> None:
    """Test supported scopes."""
    expected = {
        "read",
        "write",
        "update",
        "delete",
        "execute",
        "admin",
    }

    assert SUPPORTED_SCOPES == expected


def test_supported_scopes_are_immutable() -> None:
    """Supported scopes should be immutable."""
    assert isinstance(
        SUPPORTED_SCOPES,
        frozenset,
    )


def test_permission_constants() -> None:
    """Test permission constants."""
    assert READ_PERMISSION == "read"
    assert WRITE_PERMISSION == "write"
    assert UPDATE_PERMISSION == "update"
    assert DELETE_PERMISSION == "delete"
    assert EXECUTE_PERMISSION == "execute"
    assert ADMIN_PERMISSION == "admin"


def test_supported_permissions() -> None:
    """Test supported permissions."""
    expected = {
        "read",
        "write",
        "update",
        "delete",
        "execute",
        "admin",
    }

    assert SUPPORTED_PERMISSIONS == expected


def test_supported_permissions_are_immutable() -> None:
    """Supported permissions should be immutable."""
    assert isinstance(
        SUPPORTED_PERMISSIONS,
        frozenset,
    )


def test_resource_constants() -> None:
    """Test wildcard constants."""
    assert ANY_RESOURCE == "*"
    assert ALL_PERMISSIONS == "*"


def test_policy_constants() -> None:
    """Test policy constants."""
    assert DEFAULT_POLICY == "deny"
    assert ALLOW_POLICY == "allow"
    assert DENY_POLICY == "deny"


def test_role_hierarchy() -> None:
    """Test role hierarchy."""
    assert ROLE_HIERARCHY["guest"] == 0
    assert ROLE_HIERARCHY["user"] == 1
    assert ROLE_HIERARCHY["admin"] == 2
    assert ROLE_HIERARCHY["superuser"] == 3
    assert ROLE_HIERARCHY["system"] == 4


def test_separators() -> None:
    """Test separator constants."""
    assert ROLE_SEPARATOR == ":"
    assert PERMISSION_SEPARATOR == "."