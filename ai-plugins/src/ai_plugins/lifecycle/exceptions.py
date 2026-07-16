"""Exceptions for the ai_plugins.lifecycle module."""

from __future__ import annotations


class LifecycleError(Exception):
    """Base exception for lifecycle operations."""


class LifecycleValidationError(LifecycleError):
    """Raised when lifecycle validation fails."""


class LifecycleRegistrationError(LifecycleError):
    """Raised when lifecycle registration fails."""


class LifecycleNotFoundError(
    LifecycleRegistrationError,
):
    """Raised when a lifecycle definition cannot be found."""


class DuplicateLifecycleError(
    LifecycleRegistrationError,
):
    """Raised when attempting to register a duplicate lifecycle."""


class UnsupportedLifecyclePhaseError(
    LifecycleValidationError,
):
    """Raised when an unsupported lifecycle phase is specified."""


__all__ = [
    "DuplicateLifecycleError",
    "LifecycleError",
    "LifecycleNotFoundError",
    "LifecycleRegistrationError",
    "LifecycleValidationError",
    "UnsupportedLifecyclePhaseError",
]