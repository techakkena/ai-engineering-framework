"""
Custom exceptions for the ai_api.middleware module.

This module defines the exception hierarchy used by the middleware
components of the AI API package.

All middleware-related exceptions inherit from ``MiddlewareError``
to provide consistent and predictable error handling.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations


class MiddlewareError(Exception):
    """
    Base exception for all middleware-related errors.
    """

    def __init__(
        self,
        message: str = "A middleware error occurred.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class InvalidMiddlewareConfigurationError(MiddlewareError):
    """
    Raised when middleware configuration is invalid.
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
            f"Invalid middleware configuration: '{configuration}'."
        )


class InvalidMiddlewareTypeError(MiddlewareError):
    """
    Raised when an unsupported middleware type is specified.
    """

    def __init__(
        self,
        middleware_type: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            middleware_type: Invalid middleware type.
        """
        self.middleware_type = middleware_type

        super().__init__(
            f"Unsupported middleware type: '{middleware_type}'."
        )


class DuplicateMiddlewareError(MiddlewareError):
    """
    Raised when a middleware is registered more than once.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            name: Duplicate middleware name.
        """
        self.name = name

        super().__init__(
            f"Middleware '{name}' is already registered."
        )


class MiddlewareNotFoundError(MiddlewareError):
    """
    Raised when a requested middleware cannot be found.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            name: Middleware name.
        """
        self.name = name

        super().__init__(
            f"Middleware '{name}' was not found."
        )


class MiddlewareExecutionError(MiddlewareError):
    """
    Raised when middleware execution fails.
    """

    def __init__(
        self,
        name: str,
        reason: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            name: Middleware name.
            reason: Failure reason.
        """
        self.name = name
        self.reason = reason

        super().__init__(
            f"Middleware '{name}' execution failed: {reason}."
        )


class MiddlewarePriorityError(MiddlewareError):
    """
    Raised when an invalid middleware priority is detected.
    """

    def __init__(
        self,
        priority: int,
    ) -> None:
        """
        Initialize the exception.

        Args:
            priority: Invalid priority.
        """
        self.priority = priority

        super().__init__(
            f"Invalid middleware priority: {priority}."
        )