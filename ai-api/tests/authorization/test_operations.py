"""
Unit tests for ai_api.authorization.operations.
"""

from __future__ import annotations

import pytest

from ai_api.authorization.exceptions import (
    InsufficientPermissionsError,
    InvalidPermissionError,
    InvalidRoleError,
    InvalidScopeError,
)
from ai_api.authorization.operations import (
    has_permission,
    has_role,
    is_supported_permission,
    is_supported_role,
    is_supported_scope,
    normalize_permission,
    normalize_role,
    require_permission,
    validate_permission,
    validate_role,
    validate_scope,
)


# ============================================================================
# normalize_role
# ============================================================================


@pytest.mark.parametrize(
    ("role", "expected"),
    [
        ("Admin", "admin"),
        (" USER ", "user"),
        ("SuperUser", "superuser"),
        ("Guest", "guest"),
        ("System", "system"),
    ],
)
def test_normalize_role(
    role: str,
    expected: str,
) -> None:
    """Test role normalization."""
    assert normalize_role(role) == expected


# ============================================================================
# validate_role
# ============================================================================


@pytest.mark.parametrize(
    "role",
    [
        "user",
        "admin",
        "superuser",
        "guest",
        "system",
    ],
)
def test_validate_role(
    role: str,
) -> None:
    """Test valid roles."""
    assert validate_role(role) == role


@pytest.mark.parametrize(
    "role",
    [
        "",
        "manager",
        "developer",
        "operator",
    ],
)
def test_validate_role_invalid(
    role: str,
) -> None:
    """Invalid roles should raise."""
    with pytest.raises(InvalidRoleError):
        validate_role(role)


# ============================================================================
# normalize_permission
# ============================================================================


@pytest.mark.parametrize(
    ("permission", "expected"),
    [
        ("READ", "read"),
        (" Write ", "write"),
        ("Delete", "delete"),
        ("Execute", "execute"),
    ],
)
def test_normalize_permission(
    permission: str,
    expected: str,
) -> None:
    """Test permission normalization."""
    assert normalize_permission(permission) == expected


# ============================================================================
# validate_permission
# ============================================================================


@pytest.mark.parametrize(
    "permission",
    [
        "read",
        "write",
        "update",
        "delete",
        "execute",
        "admin",
    ],
)
def test_validate_permission(
    permission: str,
) -> None:
    """Test valid permissions."""
    assert validate_permission(permission) == permission


@pytest.mark.parametrize(
    "permission",
    [
        "",
        "publish",
        "approve",
        "manage",
    ],
)
def test_validate_permission_invalid(
    permission: str,
) -> None:
    """Invalid permissions should raise."""
    with pytest.raises(InvalidPermissionError):
        validate_permission(permission)


# ============================================================================
# validate_scope
# ============================================================================


@pytest.mark.parametrize(
    "scope",
    [
        "read",
        "write",
        "update",
        "delete",
        "execute",
        "admin",
    ],
)
def test_validate_scope(
    scope: str,
) -> None:
    """Test valid scopes."""
    assert validate_scope(scope) == scope


@pytest.mark.parametrize(
    "scope",
    [
        "",
        "billing",
        "analytics",
        "custom",
    ],
)
def test_validate_scope_invalid(
    scope: str,
) -> None:
    """Invalid scopes should raise."""
    with pytest.raises(InvalidScopeError):
        validate_scope(scope)


# ============================================================================
# has_role
# ============================================================================


@pytest.mark.parametrize(
    ("assigned", "required", "expected"),
    [
        ("admin", "user", True),
        ("superuser", "admin", True),
        ("system", "guest", True),
        ("guest", "user", False),
        ("user", "admin", False),
    ],
)
def test_has_role(
    assigned: str,
    required: str,
    expected: bool,
) -> None:
    """Test role hierarchy."""
    assert has_role(
        assigned,
        required,
    ) is expected


# ============================================================================
# has_permission
# ============================================================================


@pytest.mark.parametrize(
    ("permissions", "required", "expected"),
    [
        ({"read"}, "read", True),
        ({"read", "write"}, "write", True),
        ({"read"}, "delete", False),
        ({"admin"}, "admin", True),
    ],
)
def test_has_permission(
    permissions: set[str],
    required: str,
    expected: bool,
) -> None:
    """Test permission lookup."""
    assert has_permission(
        permissions,
        required,
    ) is expected


# ============================================================================
# require_permission
# ============================================================================


def test_require_permission_success() -> None:
    """Test successful permission validation."""
    require_permission(
        {"read", "write"},
        "write",
    )


def test_require_permission_failure() -> None:
    """Missing permission should raise."""
    with pytest.raises(
        InsufficientPermissionsError,
    ):
        require_permission(
            {"read"},
            "delete",
        )


# ============================================================================
# is_supported_role
# ============================================================================


@pytest.mark.parametrize(
    ("role", "expected"),
    [
        ("user", True),
        ("admin", True),
        ("system", True),
        ("manager", False),
    ],
)
def test_is_supported_role(
    role: str,
    expected: bool,
) -> None:
    """Test supported role detection."""
    assert (
        is_supported_role(role)
        is expected
    )


# ============================================================================
# is_supported_permission
# ============================================================================


@pytest.mark.parametrize(
    ("permission", "expected"),
    [
        ("read", True),
        ("write", True),
        ("admin", True),
        ("publish", False),
    ],
)
def test_is_supported_permission(
    permission: str,
    expected: bool,
) -> None:
    """Test supported permission detection."""
    assert (
        is_supported_permission(permission)
        is expected
    )


# ============================================================================
# is_supported_scope
# ============================================================================


@pytest.mark.parametrize(
    ("scope", "expected"),
    [
        ("read", True),
        ("write", True),
        ("admin", True),
        ("billing", False),
    ],
)
def test_is_supported_scope(
    scope: str,
    expected: bool,
) -> None:
    """Test supported scope detection."""
    assert (
        is_supported_scope(scope)
        is expected
    )