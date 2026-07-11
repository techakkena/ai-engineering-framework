"""
Constants for the datetime utilities package.
"""

from __future__ import annotations

__all__ = [
    "DEFAULT_DATETIME_FORMAT",
    "DEFAULT_DATE_FORMAT",
    "DEFAULT_TIME_FORMAT",
    "ISO_FORMAT",
    "UTC_TIMEZONE",
]

DEFAULT_DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

DEFAULT_DATE_FORMAT: str = "%Y-%m-%d"

DEFAULT_TIME_FORMAT: str = "%H:%M:%S"

ISO_FORMAT: str = "%Y-%m-%dT%H:%M:%S"

UTC_TIMEZONE: str = "UTC"
