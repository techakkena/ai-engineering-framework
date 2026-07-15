"""
Custom exceptions for the ai_api.responses module.

This module defines the exception hierarchy used throughout the
response components of the AI API package.

All response-related exceptions inherit from ``ResponseError`` to
provide consistent error handling.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations


class ResponseError(Exception):
    """
    Base exception for all response-related errors.
    """

    def __init__(
        self,
        message: str = "A response error occurred.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class InvalidResponseError(ResponseError):
    """
    Raised when a response object is invalid.
    """

    def __init__(
        self,
        reason: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            reason: Validation failure reason.
        """
        self.reason = reason

        super().__init__(
            f"Invalid response: {reason}."
        )


class InvalidContentTypeError(ResponseError):
    """
    Raised when an invalid content type is supplied.
    """

    def __init__(
        self,
        content_type: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            content_type: Invalid content type.
        """
        self.content_type = content_type

        super().__init__(
            f"Invalid content type: '{content_type}'."
        )


class UnsupportedResponseTypeError(ResponseError):
    """
    Raised when an unsupported response type is requested.
    """

    def __init__(
        self,
        response_type: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            response_type: Unsupported response type.
        """
        self.response_type = response_type

        super().__init__(
            f"Unsupported response type: '{response_type}'."
        )


class ResponseSerializationError(ResponseError):
    """
    Raised when response serialization fails.
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
            f"Response serialization failed: {reason}."
        )


class ResponseValidationError(ResponseError):
    """
    Raised when response validation fails.
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
            f"Response validation failed for '{field}': {reason}."
        )


class ResponseSizeExceededError(ResponseError):
    """
    Raised when a response exceeds the maximum allowed size.
    """

    def __init__(
        self,
        size: int,
        maximum: int,
    ) -> None:
        """
        Initialize the exception.

        Args:
            size: Actual response size.
            maximum: Maximum allowed response size.
        """
        self.size = size
        self.maximum = maximum

        super().__init__(
            f"Response size ({size} bytes) exceeds maximum allowed ({maximum} bytes)."
        )


class ResponseConfigurationError(ResponseError):
    """
    Raised when response configuration is invalid.
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
            f"Invalid response configuration: '{configuration}'."
        )