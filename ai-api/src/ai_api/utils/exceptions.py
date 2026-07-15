"""
Custom exceptions for the ai_api.utils module.

This module defines the exception hierarchy used throughout the
utility components of the AI API package.

All utility-related exceptions inherit from ``UtilityError`` to
provide consistent and predictable error handling.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations


class UtilityError(Exception):
    """
    Base exception for all utility-related errors.
    """

    def __init__(
        self,
        message: str = "A utility error occurred.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class InvalidEncodingError(UtilityError):
    """
    Raised when an unsupported encoding is supplied.
    """

    def __init__(
        self,
        encoding: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            encoding: Invalid encoding.
        """
        self.encoding = encoding

        super().__init__(
            f"Invalid encoding: '{encoding}'."
        )


class InvalidIdentifierError(UtilityError):
    """
    Raised when an identifier is invalid.
    """

    def __init__(
        self,
        identifier: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            identifier: Invalid identifier.
        """
        self.identifier = identifier

        super().__init__(
            f"Invalid identifier: '{identifier}'."
        )


class InvalidUtilityOperationError(UtilityError):
    """
    Raised when a utility operation cannot be completed.
    """

    def __init__(
        self,
        operation: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            operation: Operation name.
        """
        self.operation = operation

        super().__init__(
            f"Invalid utility operation: '{operation}'."
        )


class UtilityConfigurationError(UtilityError):
    """
    Raised when utility configuration is invalid.
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
            f"Invalid utility configuration: '{configuration}'."
        )


class UtilityValidationError(UtilityError):
    """
    Raised when utility validation fails.
    """

    def __init__(
        self,
        field: str,
        reason: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            field: Field name.
            reason: Validation failure reason.
        """
        self.field = field
        self.reason = reason

        super().__init__(
            f"Utility validation failed for '{field}': {reason}."
        )


class UtilitySerializationError(UtilityError):
    """
    Raised when utility serialization fails.
    """

    def __init__(
        self,
        reason: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            reason: Serialization failure reason.
        """
        self.reason = reason

        super().__init__(
            f"Utility serialization failed: {reason}."
        )


class UtilityTimeoutError(UtilityError):
    """
    Raised when a utility operation exceeds the timeout.
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
            f"Utility operation timed out after {timeout} seconds."
        )