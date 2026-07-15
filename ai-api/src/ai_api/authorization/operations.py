"""
Utility operations for the ai_api.authorization module.

This module provides framework-independent helper functions for
role, permission, and scope validation.

All functions are deterministic, side-effect free, and easily testable.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from ai_api.authorization.constants import (
    ROLE_HIERARCHY,
    SUPPORTED_PERMISSIONS,
    SUPPORTED_ROLES,
    SUPPORTED_SCOPES,
)
from ai_api.authorization.exceptions import (
    InsufficientPermissionsError,
    InvalidPermissionError,
    InvalidRoleError,
    InvalidScopeError,
)


def normalize_role(role: str) -> str:
    """
    Normalize a role.

    Args:
        role: Role name.

    Returns:
        Normalized role.
    """
    return role.strip().lower()


def validate_role(role: str) -> str:
    """
    Validate a role.

    Args:
        role: Role name.

    Returns:
        Validated role.

    Raises:
        InvalidRoleError:
            If the role is unsupported.
    """
    normalized = normalize_role(role)

    if normalized not in SUPPORTED_ROLES:
        raise InvalidRoleError(role)

    return normalized


def normalize_permission(permission: str) -> str:
    """
    Normalize a permission.

    Args:
        permission: Permission name.

    Returns:
        Normalized permission.
    """
    return permission.strip().lower()


def validate_permission(permission: str) -> str:
    """
    Validate a permission.

    Args:
        permission: Permission name.

    Returns:
        Validated permission.

    Raises:
        InvalidPermissionError:
            If the permission is unsupported.
    """
    normalized = normalize_permission(permission)

    if normalized not in SUPPORTED_PERMISSIONS:
        raise InvalidPermissionError(permission)

    return normalized


def validate_scope(scope: str) -> str:
    """
    Validate an authorization scope.

    Args:
        scope: Scope name.

    Returns:
        Validated scope.

    Raises:
        InvalidScopeError:
            If the scope is unsupported.
    """
    normalized = scope.strip().lower()

    if normalized not in SUPPORTED_SCOPES:
        raise InvalidScopeError(scope)

    return normalized


def has_role(
    assigned_role: str,
    required_role: str,
) -> bool:
    """
    Determine whether the assigned role satisfies the required role.

    Args:
        assigned_role: User role.
        required_role: Required role.

    Returns:
        True if the assigned role is sufficient.
    """
    assigned = validate_role(assigned_role)
    required = validate_role(required_role)

    return (
        ROLE_HIERARCHY[assigned]
        >= ROLE_HIERARCHY[required]
    )


def has_permission(
    permissions: set[str],
    required_permission: str,
) -> bool:
    """
    Determine whether a permission exists.

    Args:
        permissions: Assigned permissions.
        required_permission: Required permission.

    Returns:
        True if permission exists.
    """
    required = validate_permission(required_permission)

    normalized_permissions = {
        normalize_permission(permission)
        for permission in permissions
    }

    return required in normalized_permissions


def require_permission(
    permissions: set[str],
    required_permission: str,
) -> None:
    """
    Require a permission.

    Args:
        permissions: Assigned permissions.
        required_permission: Required permission.

    Raises:
        InsufficientPermissionsError:
            If the permission is missing.
    """
    if not has_permission(
        permissions,
        required_permission,
    ):
        raise InsufficientPermissionsError(
            required_permission,
        )


def is_supported_role(role: str) -> bool:
    """
    Determine whether a role is supported.

    Args:
        role: Role name.

    Returns:
        True if supported.
    """
    return normalize_role(role) in SUPPORTED_ROLES


def is_supported_permission(
    permission: str,
) -> bool:
    """
    Determine whether a permission is supported.

    Args:
        permission: Permission name.

    Returns:
        True if supported.
    """
    return (
        normalize_permission(permission)
        in SUPPORTED_PERMISSIONS
    )


def is_supported_scope(scope: str) -> bool:
    """
    Determine whether a scope is supported.

    Args:
        scope: Scope name.

    Returns:
        True if supported.
    """
    return scope.strip().lower() in SUPPORTED_SCOPES