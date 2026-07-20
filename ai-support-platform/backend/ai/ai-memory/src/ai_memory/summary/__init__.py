from __future__ import annotations

"""Summary module."""

from .constants import (
    DEFAULT_MAX_SUMMARY_LENGTH,
    DEFAULT_SUMMARY_NAMESPACE,
    SummaryState,
    SummaryStrategy,
    SummaryType,
)

from .exceptions import (
    SummaryError,
    SummaryNotFoundError,
    SummaryStateError,
    SummaryValidationError,
)

from .operations import (
    is_valid_summary_state,
    is_valid_summary_strategy,
    is_valid_summary_type,
    validate_summary_state,
    validate_summary_strategy,
    validate_summary_type,
)

__all__ = [
    "SummaryType",
    "SummaryStrategy",
    "SummaryState",
    "DEFAULT_MAX_SUMMARY_LENGTH",
    "DEFAULT_SUMMARY_NAMESPACE",
    "SummaryError",
    "SummaryNotFoundError",
    "SummaryValidationError",
    "SummaryStateError",
    "validate_summary_type",
    "validate_summary_strategy",
    "validate_summary_state",
    "is_valid_summary_type",
    "is_valid_summary_strategy",
    "is_valid_summary_state",
]
