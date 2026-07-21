from __future__ import annotations

"""Application exception hierarchy."""

from http import HTTPStatus


class AppException(Exception):
    """Base application exception."""

    def __init__(
        self,
        message: str,
        status_code: int = HTTPStatus.BAD_REQUEST,
    ) -> None:
        """Initialize the exception.

        Args:
            message: Error message.
            status_code: HTTP status code.
        """
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class ValidationException(AppException):
    """Raised when validation fails."""

    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            status_code=HTTPStatus.BAD_REQUEST,
        )


class AuthenticationException(AppException):
    """Raised when authentication fails."""

    def __init__(self, message: str = "Authentication failed.") -> None:
        super().__init__(
            message=message,
            status_code=HTTPStatus.UNAUTHORIZED,
        )


class AuthorizationException(AppException):
    """Raised when authorization fails."""

    def __init__(self, message: str = "Access denied.") -> None:
        super().__init__(
            message=message,
            status_code=HTTPStatus.FORBIDDEN,
        )


class ResourceNotFoundException(AppException):
    """Raised when a resource cannot be found."""

    def __init__(self, resource: str) -> None:
        super().__init__(
            message=f"{resource} not found.",
            status_code=HTTPStatus.NOT_FOUND,
        )


class ConflictException(AppException):
    """Raised when a resource conflict occurs."""

    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            status_code=HTTPStatus.CONFLICT,
        )


class DatabaseException(AppException):
    """Raised for database-related errors."""

    def __init__(
        self,
        message: str = "Database operation failed.",
    ) -> None:
        super().__init__(
            message=message,
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        )


class AIServiceException(AppException):
    """Raised when an AI service fails."""

    def __init__(
        self,
        message: str = "AI service unavailable.",
    ) -> None:
        super().__init__(
            message=message,
            status_code=HTTPStatus.SERVICE_UNAVAILABLE,
        )
