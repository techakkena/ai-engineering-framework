"""
Custom exceptions for the ai_api.base module.

This module defines the exception hierarchy used throughout the
AI API package. All custom exceptions inherit from ``APIError``,
providing a consistent error model for API-related operations.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations


class APIError(Exception):
    """
    Base exception for all AI API errors.

    All custom exceptions in the ai_api package should inherit from
    this class.
    """

    def __init__(self, message: str = "An API error occurred.") -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class ConfigurationError(APIError):
    """
    Raised when the API configuration is invalid.
    """

    def __init__(
        self,
        message: str = "Invalid API configuration.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class InvalidRouteError(APIError):
    """
    Raised when an API route is invalid.
    """

    def __init__(self, route: str) -> None:
        """
        Initialize the exception.

        Args:
            route: Invalid route.
        """
        self.route = route

        super().__init__(f"Invalid API route: '{route}'.")


class RouteAlreadyExistsError(APIError):
    """
    Raised when attempting to register an existing route.
    """

    def __init__(self, route: str) -> None:
        """
        Initialize the exception.

        Args:
            route: Duplicate route.
        """
        self.route = route

        super().__init__(f"Route already exists: '{route}'.")


class UnsupportedHTTPMethodError(APIError):
    """
    Raised when an unsupported HTTP method is used.
    """

    def __init__(self, method: str) -> None:
        """
        Initialize the exception.

        Args:
            method: Unsupported HTTP method.
        """
        self.method = method.upper()

        super().__init__(f"Unsupported HTTP method: '{self.method}'.")


class InvalidAPIVersionError(APIError):
    """
    Raised when an API version is invalid.
    """

    def __init__(self, version: str = "") -> None:
        """
        Initialize the exception.

        Args:
            version: Invalid API version.
        """
        self.version = version

        if version:
            message = f"Invalid API version: '{version}'."
        else:
            message = "API version cannot be empty."

        super().__init__(message)
