"""
Retry exceptions.
"""

from __future__ import annotations

__all__ = [
    "RetryError",
]


class RetryError(Exception):
    """Raised when all retry attempts fail."""
