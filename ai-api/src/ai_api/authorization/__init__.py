"""
ai_api.authorization

Framework-independent authorization utilities for the AI API package.

This module provides reusable authorization constants, exceptions,
and helper operations for role-based access control (RBAC),
attribute-based access control (ABAC), permission validation,
and scope management.

The module is intentionally framework-independent and can be
integrated with FastAPI, Starlette, Quart, Litestar, Flask,
Django, or any future API framework.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_api.authorization.constants import (
    ADMIN_ROLE,
    DEFAULT_ROLE,
    DEFAULT_SCOPE,
    SUPERUSER_ROLE,
    SUPPORTED_PERMISSIONS,
    SUPPORTED_ROLES,
)
from ai_api.authorization.exceptions import (
    AuthorizationError,
    InsufficientPermissionsError,
    InvalidPermissionError,
    InvalidRoleError,
    UnauthorizedAccessError,
)
from ai_api.authorization.operations import (
    has_permission,
    has_role,
    normalize_permission,
    normalize_role,
    validate_permission,
    validate_role,
)

__all__ = [
    # Constants
    "ADMIN_ROLE",
    "DEFAULT_ROLE",
    "DEFAULT_SCOPE",
    "SUPERUSER_ROLE",
    "SUPPORTED_PERMISSIONS",
    "SUPPORTED_ROLES",
    # Exceptions
    "AuthorizationError",
    "InsufficientPermissionsError",
    "InvalidPermissionError",
    "InvalidRoleError",
    "UnauthorizedAccessError",
    # Operations
    "has_permission",
    "has_role",
    "normalize_permission",
    "normalize_role",
    "validate_permission",
    "validate_role",
]