from __future__ import annotations

"""Exceptions for the ai_memory.store module."""

from __future__ import annotations


class StoreError(Exception):
    """Base exception for store operations."""


class StoreNotFoundError(StoreError):
    """Raised when a store cannot be found."""


class StoreValidationError(StoreError):
    """Raised when store validation fails."""


class StoreStateError(StoreError):
    """Raised when an invalid store state is encountered."""
