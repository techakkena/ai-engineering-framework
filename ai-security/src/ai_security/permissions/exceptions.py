"""
Exceptions for the permissions module.
"""

from __future__ import annotations


class PermissionError(Exception):
    """Base exception for permission operations."""


class PermissionConfigurationError(PermissionError):
    """Raised when permission configuration is invalid."""


class PermissionDeniedError(PermissionError):
    """Raised when permission is denied."""


class RoleNotFoundError(PermissionError):
    """Raised when a requested role does not exist."""