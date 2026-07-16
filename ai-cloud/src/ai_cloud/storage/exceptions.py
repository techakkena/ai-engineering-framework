"""Exceptions for the ai_cloud.storage module."""

from __future__ import annotations


class StorageError(Exception):
    """Base exception for storage operations."""


class StorageValidationError(StorageError):
    """Raised when storage validation fails."""


class StorageRegistrationError(StorageError):
    """Raised when storage registration fails."""


class StorageNotFoundError(
    StorageRegistrationError,
):
    """Raised when a storage definition cannot be found."""


class DuplicateStorageError(
    StorageRegistrationError,
):
    """Raised when attempting to register a duplicate storage."""


class UnsupportedStorageTypeError(
    StorageValidationError,
):
    """Raised when an unsupported storage type is specified."""


__all__ = [
    "DuplicateStorageError",
    "StorageError",
    "StorageNotFoundError",
    "StorageRegistrationError",
    "StorageValidationError",
    "UnsupportedStorageTypeError",
]