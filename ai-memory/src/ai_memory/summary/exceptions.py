"""Exceptions for the ai_memory.summary module."""

from __future__ import annotations


class SummaryError(Exception):
    """Base exception for summary operations."""


class SummaryNotFoundError(SummaryError):
    """Raised when a summary cannot be found."""


class SummaryValidationError(SummaryError):
    """Raised when summary validation fails."""


class SummaryStateError(SummaryError):
    """Raised when an invalid summary state is encountered."""