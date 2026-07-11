"""
String operations for the AI Engineering Framework.
"""

from __future__ import annotations

import re

from ai_utils.string_utils.constants import (
    DEFAULT_TRUNCATE_SUFFIX,
)

__all__ = [
    "capitalize_words",
    "is_blank",
    "normalize_whitespace",
    "remove_whitespace",
    "reverse",
    "to_camel_case",
    "to_pascal_case",
    "to_snake_case",
    "truncate",
]


def is_blank(value: str) -> bool:
    """Return True if the string is empty or whitespace."""
    return not value.strip()


def to_snake_case(value: str) -> str:
    """Convert text to snake_case."""
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[\s\-]+", "_", value)
    return value.lower()


def to_pascal_case(value: str) -> str:
    """Convert text to PascalCase."""
    words = re.split(r"[\s_\-]+", value)
    return "".join(word.capitalize() for word in words if word)


def to_camel_case(value: str) -> str:
    """Convert text to camelCase."""
    pascal = to_pascal_case(value)

    if not pascal:
        return ""

    return pascal[0].lower() + pascal[1:]


def truncate(
    value: str,
    length: int,
    suffix: str = DEFAULT_TRUNCATE_SUFFIX,
) -> str:
    """Truncate a string."""
    if len(value) <= length:
        return value

    return value[:length] + suffix


def remove_whitespace(value: str) -> str:
    """Remove all whitespace."""
    return "".join(value.split())


def normalize_whitespace(value: str) -> str:
    """Collapse consecutive whitespace."""
    return " ".join(value.split())


def reverse(value: str) -> str:
    """Reverse a string."""
    return value[::-1]


def capitalize_words(value: str) -> str:
    """Capitalize every word."""
    return value.title()
