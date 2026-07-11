"""
Validation operations for the AI Engineering Framework.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from uuid import UUID

from ai_utils.validation_utils.constants import (
    EMAIL_PATTERN,
    URL_PATTERN,
)

__all__ = [
    "is_email",
    "is_file_path",
    "is_json",
    "is_non_empty",
    "is_positive_integer",
    "is_url",
    "is_uuid",
    "is_valid_length",
]


def is_email(value: str) -> bool:
    """
    Return True if the string is a valid email address.
    """
    return re.fullmatch(EMAIL_PATTERN, value) is not None


def is_url(value: str) -> bool:
    """
    Return True if the string is a valid HTTP/HTTPS URL.
    """
    return re.fullmatch(URL_PATTERN, value) is not None


def is_uuid(value: str) -> bool:
    """
    Return True if the string is a valid UUID.
    """
    try:
        UUID(value)
        return True
    except ValueError:
        return False


def is_non_empty(value: str) -> bool:
    """
    Return True if the string is not empty after stripping whitespace.
    """
    return bool(value.strip())


def is_positive_integer(value: int) -> bool:
    """
    Return True if the value is a positive integer.
    """
    return value > 0


def is_valid_length(
    value: str,
    minimum: int = 0,
    maximum: int | None = None,
) -> bool:
    """
    Return True if the string length is within the specified range.
    """
    length = len(value)

    if length < minimum:
        return False

    if maximum is not None and length > maximum:
        return False

    return True


def is_json(value: str) -> bool:
    """
    Return True if the string contains valid JSON.
    """
    try:
        json.loads(value)
        return True
    except json.JSONDecodeError:
        return False


def is_file_path(value: str | Path) -> bool:
    """
    Return True if the path exists.
    """
    return Path(value).exists()
