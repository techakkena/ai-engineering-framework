"""
Constants for validation utilities.
"""

from __future__ import annotations

__all__ = [
    "EMAIL_PATTERN",
    "URL_PATTERN",
]

EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

URL_PATTERN = r"^https?://.+"
