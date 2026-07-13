"""Exceptions for the ai_memory.entity module."""

from __future__ import annotations


class EntityError(Exception):
    """Base exception for entity operations."""


class EntityNotFoundError(EntityError):
    """Raised when an entity cannot be found."""


class EntityValidationError(EntityError):
    """Raised when entity validation fails."""


class EntityStateError(EntityError):
    """Raised when an invalid entity state is encountered."""