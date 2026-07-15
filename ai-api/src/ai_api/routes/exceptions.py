"""
Custom exceptions for the ai_api.routes module.

This module defines the exception hierarchy used by the routing
components of the AI API package.

All routing exceptions inherit from ``RouteError`` to provide
consistent and predictable error handling.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations


class RouteError(Exception):
    """
    Base exception for all route-related errors.
    """

    def __init__(
        self,
        message: str = "A route error occurred.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class InvalidRouteNameError(RouteError):
    """
    Raised when a route name is invalid.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the exception.

        Args:
            name: Invalid route name.
        """
        self.name = name

        super().__init__(
            f"Invalid route name: '{name}'."
        )


class DuplicateRouteNameError(RouteError):
    """
    Raised when a duplicate route name is detected.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the exception.

        Args:
            name: Duplicate route name.
        """
        self.name = name

        super().__init__(
            f"Route name already exists: '{name}'."
        )


class DuplicateRoutePathError(RouteError):
    """
    Raised when a duplicate route path is detected.
    """

    def __init__(self, path: str) -> None:
        """
        Initialize the exception.

        Args:
            path: Duplicate route path.
        """
        self.path = path

        super().__init__(
            f"Route path already exists: '{path}'."
        )


class InvalidRouteParameterError(RouteError):
    """
    Raised when a route parameter is invalid.
    """

    def __init__(self, parameter: str) -> None:
        """
        Initialize the exception.

        Args:
            parameter: Invalid route parameter.
        """
        self.parameter = parameter

        super().__init__(
            f"Invalid route parameter: '{parameter}'."
        )


class InvalidRoutePathError(RouteError):
    """
    Raised when a route path is invalid.
    """

    def __init__(self, path: str) -> None:
        """
        Initialize the exception.

        Args:
            path: Invalid route path.
        """
        self.path = path

        super().__init__(
            f"Invalid route path: '{path}'."
        )


class ReservedRouteNameError(RouteError):
    """
    Raised when a reserved route name is used.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the exception.

        Args:
            name: Reserved route name.
        """
        self.name = name

        super().__init__(
            f"Reserved route name cannot be used: '{name}'."
        )


class RouteLengthExceededError(RouteError):
    """
    Raised when a route exceeds the maximum allowed length.
    """

    def __init__(
        self,
        length: int,
        maximum: int,
    ) -> None:
        """
        Initialize the exception.

        Args:
            length: Actual route length.
            maximum: Maximum permitted route length.
        """
        self.length = length
        self.maximum = maximum

        super().__init__(
            f"Route length ({length}) exceeds maximum allowed ({maximum})."
        )