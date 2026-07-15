"""
Custom exceptions for the ai_api.errors module.

This module defines the exception hierarchy used throughout the
error handling components of the AI API package.

All error-related exceptions inherit from ``ErrorHandlingError``
to provide consistent and predictable error handling.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations


class ErrorHandlingError(Exception):
    """
    Base exception for all error handling exceptions.
    """

    def __init__(
        self,
        message: str = "An error handling error occurred.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class InvalidErrorCodeError(ErrorHandlingError):
    """
    Raised when an invalid error code is supplied.
    """

    def __init__(
        self,
        error_code: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            error_code: Invalid error code.
        """
        self.error_code = error_code

        super().__init__(
            f"Invalid error code: '{error_code}'."
        )


class InvalidErrorTypeError(ErrorHandlingError):
    """
    Raised when an invalid error type is supplied.
    """

    def __init__(
        self,
        error_type: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            error_type: Invalid error type.
        """
        self.error_type = error_type

        super().__init__(
            f"Invalid error type: '{error_type}'."
        )


class ErrorMappingError(ErrorHandlingError):
    """
    Raised when an error cannot be mapped.
    """

    def __init__(
        self,
        source: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            source: Source error.
        """
        self.source = source

        super().__init__(
            f"Unable to map error: '{source}'."
        )


class ErrorConfigurationError(ErrorHandlingError):
    """
    Raised when error configuration is invalid.
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
            f"Invalid error configuration: '{configuration}'."
        )


class ErrorSerializationError(ErrorHandlingError):
    """
    Raised when error serialization fails.
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
            f"Error serialization failed: {reason}."
        )


class ErrorValidationError(ErrorHandlingError):
    """
    Raised when error validation fails.
    """

    def __init__(
        self,
        field: str,
        reason: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            field: Invalid field.
            reason: Validation failure reason.
        """
        self.field = field
        self.reason = reason

        super().__init__(
            f"Error validation failed for '{field}': {reason}."
        )


class ErrorCategoryError(ErrorHandlingError):
    """
    Raised when an invalid error category is supplied.
    """

    def __init__(
        self,
        category: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            category: Invalid category.
        """
        self.category = category

        super().__init__(
            f"Invalid error category: '{category}'."
        )