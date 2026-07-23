"""Custom exceptions for the knowledge module."""

from __future__ import annotations

from app.core.exceptions import AppException


class KnowledgeError(AppException):
    """Base exception for all knowledge module errors."""

    def __init__(
        self,
        message: str = "Knowledge module error.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


class KnowledgeNotFoundError(KnowledgeError):
    """Raised when a knowledge article is not found."""

    def __init__(
        self,
        message: str = "Knowledge article not found.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


class KnowledgeAlreadyExistsError(KnowledgeError):
    """Raised when a knowledge article already exists."""

    def __init__(
        self,
        message: str = "Knowledge article already exists.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


class KnowledgeSlugExistsError(KnowledgeError):
    """Raised when a knowledge article slug already exists."""

    def __init__(
        self,
        message: str = "Knowledge article slug already exists.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


class KnowledgeValidationError(KnowledgeError):
    """Raised when knowledge article validation fails."""

    def __init__(
        self,
        message: str = "Knowledge article validation failed.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


class KnowledgePublishError(KnowledgeError):
    """Raised when a knowledge article cannot be published."""

    def __init__(
        self,
        message: str = "Knowledge article cannot be published.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


class KnowledgeArchiveError(KnowledgeError):
    """Raised when a knowledge article cannot be archived."""

    def __init__(
        self,
        message: str = "Knowledge article cannot be archived.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


class KnowledgePermissionDeniedError(KnowledgeError):
    """Raised when the user lacks permission."""

    def __init__(
        self,
        message: str = "Permission denied for knowledge article.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


class KnowledgeVersionConflictError(KnowledgeError):
    """Raised when a version conflict occurs."""

    def __init__(
        self,
        message: str = "Knowledge article version conflict.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


class KnowledgeDeletedError(KnowledgeError):
    """Raised when an operation targets a deleted article."""

    def __init__(
        self,
        message: str = "Knowledge article has been deleted.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


class KnowledgeSearchError(KnowledgeError):
    """Raised when knowledge search fails."""

    def __init__(
        self,
        message: str = "Knowledge search failed.",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)
