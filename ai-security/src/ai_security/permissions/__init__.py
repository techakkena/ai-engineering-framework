"""
Permission management for the AI Engineering Framework.

This package provides framework-independent permission evaluation,
role-based access control (RBAC), and permission management utilities.
"""

from ai_security.permissions.constants import (
    DEFAULT_ROLE,
    DEFAULT_SEPARATOR,
    WILDCARD_PERMISSION,
)
from ai_security.permissions.exceptions import (
    PermissionConfigurationError,
    PermissionDeniedError,
    PermissionError,
    RoleNotFoundError,
)
from ai_security.permissions.operations import (
    Permission,
    PermissionManager,
    Role,
)

__all__ = [
    "DEFAULT_ROLE",
    "DEFAULT_SEPARATOR",
    "WILDCARD_PERMISSION",
    "PermissionError",
    "PermissionConfigurationError",
    "PermissionDeniedError",
    "RoleNotFoundError",
    "Permission",
    "Role",
    "PermissionManager",
]