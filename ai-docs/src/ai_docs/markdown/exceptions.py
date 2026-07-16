"""Exceptions for the ai_docs.markdown module."""

from __future__ import annotations


class MarkdownError(Exception):
    """Base exception for markdown operations."""


class MarkdownValidationError(
    MarkdownError,
):
    """Raised when markdown validation fails."""


class MarkdownRegistrationError(
    MarkdownError,
):
    """Raised when markdown registration fails."""


class MarkdownNotFoundError(
    MarkdownRegistrationError,
):
    """Raised when a markdown document cannot be found."""


class DuplicateMarkdownError(
    MarkdownRegistrationError,
):
    """Raised when attempting to register a duplicate markdown."""


class UnsupportedMarkdownFormatError(
    MarkdownValidationError,
):
    """Raised when an unsupported markdown format is specified."""


__all__ = [
    "DuplicateMarkdownError",
    "MarkdownError",
    "MarkdownNotFoundError",
    "MarkdownRegistrationError",
    "MarkdownValidationError",
    "UnsupportedMarkdownFormatError",
]