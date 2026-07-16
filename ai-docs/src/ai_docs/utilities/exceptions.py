"""Exceptions for the ai_docs.utilities module."""

from __future__ import annotations


class UtilityError(Exception):
    """Base utility exception."""


class UtilityValidationError(
    UtilityError,
):
    """Raised when utility validation fails."""


__all__ = [
    "UtilityError",
    "UtilityValidationError",
]