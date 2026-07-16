"""Exceptions for the ai_cloud.utilities module."""

from __future__ import annotations


class UtilityError(Exception):
    """Base exception for utility operations."""


class UtilityValidationError(UtilityError):
    """Raised when utility validation fails."""


__all__ = [
    "UtilityError",
    "UtilityValidationError",
]