"""Exceptions for the ai_plugins.loading module."""

from __future__ import annotations


class LoaderError(Exception):
    """Base exception for loader operations."""


class LoaderValidationError(LoaderError):
    """Raised when loader validation fails."""


class LoaderRegistrationError(LoaderError):
    """Raised when loader registration fails."""


class LoaderNotFoundError(
    LoaderRegistrationError,
):
    """Raised when a loader definition cannot be found."""


class DuplicateLoaderError(
    LoaderRegistrationError,
):
    """Raised when attempting to register a duplicate loader."""


class UnsupportedLoadingModeError(
    LoaderValidationError,
):
    """Raised when an unsupported loading mode is specified."""


__all__ = [
    "DuplicateLoaderError",
    "LoaderError",
    "LoaderNotFoundError",
    "LoaderRegistrationError",
    "LoaderValidationError",
    "UnsupportedLoadingModeError",
]