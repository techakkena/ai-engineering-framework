from __future__ import annotations

"""Utility operations."""

from __future__ import annotations


def normalize_text(text: str) -> str:
    """Normalize whitespace."""

    return " ".join(text.split())


def is_blank(text: str) -> bool:
    """Return True if text is empty."""

    return text.strip() == ""


def ensure_trailing_newline(text: str) -> str:
    """Ensure text ends with a newline."""

    if text.endswith("\n"):
        return text

    return f"{text}\n"


def count_lines(text: str) -> int:
    """Return number of lines."""

    if not text:
        return 0

    return len(text.splitlines())


__all__ = [
    "normalize_text",
    "is_blank",
    "ensure_trailing_newline",
    "count_lines",
]
