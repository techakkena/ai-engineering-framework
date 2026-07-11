"""
Custom exceptions for validation utilities.
"""

from __future__ import annotations

__all__ = [
    "ValidationUtilsError",
]


class ValidationUtilsError(Exception):
    """Base exception for validation utilities."""
