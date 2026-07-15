"""
Custom exceptions for the ai_api.authentication module.

This module defines the exception hierarchy used throughout the
authentication components of the AI API package.

All authentication-related exceptions inherit from
``AuthenticationError`` to provide consistent error handling.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations


class AuthenticationError(Exception):
    """
    Base exception for all authentication-related errors.
    """

    def __init__(
        self,
        message: str = "An authentication error occurred.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class InvalidCredentialsError(AuthenticationError):
    """
    Raised when user credentials are invalid.
    """

    def __init__(
        self,
        username: str = "",
    ) -> None:
        """
        Initialize the exception.

        Args:
            username: Username associated with the failed authentication.
        """
        self.username = username

        message = (
            f"Invalid credentials for user '{username}'."
            if username
            else "Invalid credentials."
        )

        super().__init__(message)


class InvalidTokenError(AuthenticationError):
    """
    Raised when an authentication token is invalid.
    """

    def __init__(
        self,
        token: str = "",
    ) -> None:
        """
        Initialize the exception.

        Args:
            token: Invalid token.
        """
        self.token = token

        super().__init__("Invalid authentication token.")


class ExpiredTokenError(AuthenticationError):
    """
    Raised when an authentication token has expired.
    """

    def __init__(
        self,
        token: str = "",
    ) -> None:
        """
        Initialize the exception.

        Args:
            token: Expired token.
        """
        self.token = token

        super().__init__("Authentication token has expired.")


class MissingAuthorizationHeaderError(AuthenticationError):
    """
    Raised when the Authorization header is missing.
    """

    def __init__(self) -> None:
        """Initialize the exception."""
        super().__init__("Authorization header is missing.")


class UnsupportedAuthenticationSchemeError(AuthenticationError):
    """
    Raised when an unsupported authentication scheme is used.
    """

    def __init__(
        self,
        scheme: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            scheme: Unsupported authentication scheme.
        """
        self.scheme = scheme

        super().__init__(
            f"Unsupported authentication scheme: '{scheme}'."
        )


class AuthenticationConfigurationError(AuthenticationError):
    """
    Raised when authentication configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            configuration: Invalid configuration value.
        """
        self.configuration = configuration

        super().__init__(
            f"Invalid authentication configuration: '{configuration}'."
        )


class AuthenticationRequiredError(AuthenticationError):
    """
    Raised when authentication is required but not provided.
    """

    def __init__(self) -> None:
        """Initialize the exception."""
        super().__init__("Authentication is required.")


class AuthenticationTimeoutError(AuthenticationError):
    """
    Raised when an authentication operation times out.
    """

    def __init__(
        self,
        timeout: int,
    ) -> None:
        """
        Initialize the exception.

        Args:
            timeout: Timeout value in seconds.
        """
        self.timeout = timeout

        super().__init__(
            f"Authentication operation timed out after {timeout} seconds."
        )