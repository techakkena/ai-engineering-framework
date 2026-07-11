"""
Datetime operations for the AI Engineering Framework.
"""

from __future__ import annotations

from datetime import UTC, datetime

from ai_utils.datetime_utils.constants import DEFAULT_DATETIME_FORMAT
from ai_utils.datetime_utils.exceptions import (
    DateTimeFormatError,
    DateTimeParseError,
)

__all__ = [
    "format_datetime",
    "from_iso",
    "from_timestamp",
    "local_now",
    "parse_datetime",
    "to_iso",
    "to_timestamp",
    "utc_now",
]


def utc_now() -> datetime:
    """Return the current UTC datetime."""
    return datetime.now(UTC)


def local_now() -> datetime:
    """Return the current local datetime."""
    return datetime.now()


def to_iso(value: datetime) -> str:
    """Convert a datetime to ISO-8601 format."""
    return value.isoformat()


def from_iso(value: str) -> datetime:
    """Parse an ISO-8601 datetime string."""
    try:
        return datetime.fromisoformat(value)
    except ValueError as exc:
        raise DateTimeParseError(f"Invalid ISO datetime: {value}") from exc


def to_timestamp(value: datetime) -> float:
    """Convert a datetime to a Unix timestamp."""
    return value.timestamp()


def from_timestamp(value: float) -> datetime:
    """Convert a Unix timestamp to a datetime."""
    return datetime.fromtimestamp(value)


def format_datetime(
    value: datetime,
    fmt: str = DEFAULT_DATETIME_FORMAT,
) -> str:
    """Format a datetime."""
    try:
        return value.strftime(fmt)
    except Exception as exc:
        raise DateTimeFormatError("Unable to format datetime.") from exc


def parse_datetime(
    value: str,
    fmt: str = DEFAULT_DATETIME_FORMAT,
) -> datetime:
    """Parse a datetime string."""
    try:
        return datetime.strptime(value, fmt)
    except ValueError as exc:
        raise DateTimeParseError(f"Unable to parse datetime: {value}") from exc
