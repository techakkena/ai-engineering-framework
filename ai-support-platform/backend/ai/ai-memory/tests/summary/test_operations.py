from __future__ import annotations

"""Tests for ai_memory.summary.operations."""

import pytest

from ai_memory.summary.constants import (
    SummaryState,
    SummaryStrategy,
    SummaryType,
)
from ai_memory.summary.exceptions import SummaryValidationError
from ai_memory.summary.operations import (
    is_valid_summary_state,
    is_valid_summary_strategy,
    is_valid_summary_type,
    validate_summary_state,
    validate_summary_strategy,
    validate_summary_type,
)


def test_validate_summary_type() -> None:
    assert validate_summary_type("memory") is SummaryType.MEMORY


def test_validate_summary_strategy() -> None:
    assert validate_summary_strategy("hybrid") is SummaryStrategy.HYBRID


def test_validate_summary_state() -> None:
    assert validate_summary_state("active") is SummaryState.ACTIVE


@pytest.mark.parametrize(
    ("value", "validator"),
    [
        ("invalid", validate_summary_type),
        ("invalid", validate_summary_strategy),
        ("invalid", validate_summary_state),
    ],
)
def test_validation_errors(value: str, validator) -> None:
    with pytest.raises(SummaryValidationError):
        validator(value)


def test_is_valid_summary_type() -> None:
    assert is_valid_summary_type("conversation")
    assert not is_valid_summary_type("invalid")


def test_is_valid_summary_strategy() -> None:
    assert is_valid_summary_strategy("extractive")
    assert not is_valid_summary_strategy("invalid")


def test_is_valid_summary_state() -> None:
    assert is_valid_summary_state("archived")
    assert not is_valid_summary_state("invalid")
