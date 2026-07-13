"""Prompt utility functions."""

from .constants import (
    DEFAULT_ENCODING,
    DEFAULT_LINE_SEPARATOR,
)
from .exceptions import (
    EmptyTextError,
    InvalidTextError,
    UtilityError,
)
from .operations import (
    count_lines,
    ensure_trailing_newline,
    is_blank,
    normalize_text,
)

__all__ = [
    "DEFAULT_ENCODING",
    "DEFAULT_LINE_SEPARATOR",
    "UtilityError",
    "InvalidTextError",
    "EmptyTextError",
    "normalize_text",
    "is_blank",
    "ensure_trailing_newline",
    "count_lines",
]
