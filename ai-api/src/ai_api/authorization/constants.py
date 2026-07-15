"""
Constants for the ai_api.authorization module.

This module defines immutable constants used throughout the
authorization components of the AI API package.

The constants are framework-independent and provide sensible defaults
for roles, permissions, scopes, and authorization policies.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Default Roles
# ============================================================================

DEFAULT_ROLE: Final[str] = "user"

ADMIN_ROLE: Final[str] = "admin"

SUPERUSER_ROLE: Final[str] = "superuser"

GUEST_ROLE: Final[str] = "guest"

SYSTEM_ROLE: Final[str] = "system"

# ============================================================================
# Supported Roles
# ============================================================================

SUPPORTED_ROLES: Final[frozenset[str]] = frozenset(
    {
        DEFAULT_ROLE,
        ADMIN_ROLE,
        SUPERUSER_ROLE,
        GUEST_ROLE,
        SYSTEM_ROLE,
    }
)

# ============================================================================
# Default Scope
# ============================================================================

DEFAULT_SCOPE: Final[str] = "read"

# ============================================================================
# OAuth2 / JWT Scopes
# ============================================================================

SUPPORTED_SCOPES: Final[frozenset[str]] = frozenset(
    {
        "read",
        "write",
        "update",
        "delete",
        "execute",
        "admin",
    }
)

# ============================================================================
# Permissions
# ============================================================================

READ_PERMISSION: Final[str] = "read"

WRITE_PERMISSION: Final[str] = "write"

UPDATE_PERMISSION: Final[str] = "update"

DELETE_PERMISSION: Final[str] = "delete"

EXECUTE_PERMISSION: Final[str] = "execute"

ADMIN_PERMISSION: Final[str] = "admin"

SUPPORTED_PERMISSIONS: Final[frozenset[str]] = frozenset(
    {
        READ_PERMISSION,
        WRITE_PERMISSION,
        UPDATE_PERMISSION,
        DELETE_PERMISSION,
        EXECUTE_PERMISSION,
        ADMIN_PERMISSION,
    }
)

# ============================================================================
# Resource Wildcards
# ============================================================================

ANY_RESOURCE: Final[str] = "*"

ALL_PERMISSIONS: Final[str] = "*"

# ============================================================================
# Policy Defaults
# ============================================================================

DEFAULT_POLICY: Final[str] = "deny"

ALLOW_POLICY: Final[str] = "allow"

DENY_POLICY: Final[str] = "deny"

# ============================================================================
# Role Hierarchy
# ============================================================================

ROLE_HIERARCHY: Final[dict[str, int]] = {
    GUEST_ROLE: 0,
    DEFAULT_ROLE: 1,
    ADMIN_ROLE: 2,
    SUPERUSER_ROLE: 3,
    SYSTEM_ROLE: 4,
}

# ============================================================================
# Miscellaneous
# ============================================================================

ROLE_SEPARATOR: Final[str] = ":"

PERMISSION_SEPARATOR: Final[str] = "."