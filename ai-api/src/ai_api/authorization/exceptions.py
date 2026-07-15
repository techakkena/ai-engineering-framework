"""
Custom exceptions for the ai_api.authorization module.

This module defines the exception hierarchy used throughout the
authorization components of the AI API package.

All authorization-related exceptions inherit from
``AuthorizationError`` to provide consistent error handling.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations


class AuthorizationError(Exception):
    """
    Base exception for all authorization-related errors.
    """

    def __init__(
        self,
        message: str = "An authorization error occurred.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class UnauthorizedAccessError(AuthorizationError):
    """
    Raised when access to a resource is denied.
    """

    def __init__(
        self,
        resource: str = "",
    ) -> None:
        """
        Initialize the exception.

        Args:
            resource: Protected resource.
        """
        self.resource = resource

        message = (
            f"Unauthorized access to resource '{resource}'."
            if resource
            else "Unauthorized access."
        )

        super().__init__(message)


class InvalidRoleError(AuthorizationError):
    """
    Raised when an invalid role is supplied.
    """

    def __init__(
        self,
        role: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            role: Invalid role.
        """
        self.role = role

        super().__init__(
            f"Invalid role: '{role}'."
        )


class InvalidPermissionError(AuthorizationError):
    """
    Raised when an invalid permission is supplied.
    """

    def __init__(
        self,
        permission: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            permission: Invalid permission.
        """
        self.permission = permission

        super().__init__(
            f"Invalid permission: '{permission}'."
        )


class InvalidScopeError(AuthorizationError):
    """
    Raised when an invalid authorization scope is supplied.
    """

    def __init__(
        self,
        scope: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            scope: Invalid scope.
        """
        self.scope = scope

        super().__init__(
            f"Invalid scope: '{scope}'."
        )


class InsufficientPermissionsError(AuthorizationError):
    """
    Raised when a user lacks the required permission.
    """

    def __init__(
        self,
        permission: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            permission: Required permission.
        """
        self.permission = permission

        super().__init__(
            f"Insufficient permissions: '{permission}' required."
        )


class RoleHierarchyError(AuthorizationError):
    """
    Raised when an invalid role hierarchy is encountered.
    """

    def __init__(
        self,
        role: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            role: Role causing the hierarchy violation.
        """
        self.role = role

        super().__init__(
            f"Invalid role hierarchy for '{role}'."
        )


class AuthorizationConfigurationError(
    AuthorizationError,
):
    """
    Raised when authorization configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            configuration: Invalid configuration.
        """
        self.configuration = configuration

        super().__init__(
            f"Invalid authorization configuration: '{configuration}'."
        )