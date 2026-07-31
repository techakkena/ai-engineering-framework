"""Custom exceptions for the knowledge module."""

from __future__ import annotations

from http import HTTPStatus

from app.core.exceptions import AppException


class KnowledgeError(AppException):
    """Base exception for the knowledge module."""

    def __init__(
        self,
        message: str = "Knowledge module error.",
        status_code: HTTPStatus = HTTPStatus.BAD_REQUEST,
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=status_code,
        )


class KnowledgeNotFoundError(KnowledgeError):
    """Raised when a knowledge article cannot be found."""

    def __init__(
        self,
        message: str = "Knowledge article not found.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=HTTPStatus.NOT_FOUND,
        )


class KnowledgeAlreadyExistsError(KnowledgeError):
    """Raised when a knowledge article already exists."""

    def __init__(
        self,
        message: str = "Knowledge article already exists.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=HTTPStatus.CONFLICT,
        )


class KnowledgeSlugExistsError(KnowledgeError):
    """Raised when a knowledge article slug already exists."""

    def __init__(
        self,
        message: str = "Knowledge article slug already exists.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=HTTPStatus.CONFLICT,
        )


class KnowledgeValidationError(KnowledgeError):
    """Raised when knowledge article validation fails."""

    def __init__(
        self,
        message: str = "Knowledge article validation failed.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        )


class KnowledgePublishError(KnowledgeError):
    """Raised when a knowledge article cannot be published."""

    def __init__(
        self,
        message: str = "Knowledge article cannot be published.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=HTTPStatus.BAD_REQUEST,
        )


class KnowledgeArchiveError(KnowledgeError):
    """Raised when a knowledge article cannot be archived."""

    def __init__(
        self,
        message: str = "Knowledge article cannot be archived.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=HTTPStatus.BAD_REQUEST,
        )


class KnowledgePermissionDeniedError(KnowledgeError):
    """Raised when the user lacks permission to access a knowledge article."""

    def __init__(
        self,
        message: str = "Permission denied for knowledge article.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=HTTPStatus.FORBIDDEN,
        )


class KnowledgeVersionConflictError(KnowledgeError):
    """Raised when a knowledge article version conflict occurs."""

    def __init__(
        self,
        message: str = "Knowledge article version conflict.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=HTTPStatus.CONFLICT,
        )


class KnowledgeDeletedError(KnowledgeError):
    """Raised when an operation targets a deleted knowledge article."""

    def __init__(
        self,
        message: str = "Knowledge article has been deleted.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=HTTPStatus.GONE,
        )


class KnowledgeSearchError(KnowledgeError):
    """Raised when a knowledge search operation fails."""

    def __init__(
        self,
        message: str = "Knowledge search failed.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(
            message=message,
            status_code=HTTPStatus.BAD_REQUEST,
        )
