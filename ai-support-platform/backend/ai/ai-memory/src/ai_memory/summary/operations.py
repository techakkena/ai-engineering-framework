from __future__ import annotations

"""Operations for the ai_memory.summary module."""

from __future__ import annotations

from .constants import SummaryState
from .constants import SummaryStrategy
from .constants import SummaryType
from .exceptions import SummaryValidationError


def validate_summary_type(
    summary_type: SummaryType | str,
) -> SummaryType:
    """Validate a summary type."""
    try:
        return SummaryType(summary_type)
    except ValueError as exc:
        raise SummaryValidationError(
            f"Invalid summary type: {summary_type!r}."
        ) from exc


def validate_summary_strategy(
    strategy: SummaryStrategy | str,
) -> SummaryStrategy:
    """Validate a summary strategy."""
    try:
        return SummaryStrategy(strategy)
    except ValueError as exc:
        raise SummaryValidationError(
            f"Invalid summary strategy: {strategy!r}."
        ) from exc


def validate_summary_state(
    state: SummaryState | str,
) -> SummaryState:
    """Validate a summary state."""
    try:
        return SummaryState(state)
    except ValueError as exc:
        raise SummaryValidationError(
            f"Invalid summary state: {state!r}."
        ) from exc


def is_valid_summary_type(summary_type: str) -> bool:
    """Return True if the summary type is valid."""
    try:
        SummaryType(summary_type)
        return True
    except ValueError:
        return False


def is_valid_summary_strategy(strategy: str) -> bool:
    """Return True if the summary strategy is valid."""
    try:
        SummaryStrategy(strategy)
        return True
    except ValueError:
        return False


def is_valid_summary_state(state: str) -> bool:
    """Return True if the summary state is valid."""
    try:
        SummaryState(state)
        return True
    except ValueError:
        return False
