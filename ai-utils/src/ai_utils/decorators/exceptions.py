"""
Decorator exceptions.
"""

from __future__ import annotations

__all__ = [
    "DecoratorError",
]


class DecoratorError(Exception):
    """Base exception for decorators."""
