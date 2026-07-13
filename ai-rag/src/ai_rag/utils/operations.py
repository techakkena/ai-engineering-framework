"""General utility operations."""

from .constants import DEFAULT_SEPARATOR


def is_empty(value: str) -> bool:
    """Return True if the string is empty."""

    return not value.strip()


def normalize_text(text: str) -> str:
    """Normalize whitespace in text."""

    return " ".join(text.split())


def join_lines(lines: list[str]) -> str:
    """Join multiple lines into a single string."""

    return DEFAULT_SEPARATOR.join(lines)


def unique_strings(values: list[str]) -> list[str]:
    """Return unique strings while preserving order."""

    return list(dict.fromkeys(values))