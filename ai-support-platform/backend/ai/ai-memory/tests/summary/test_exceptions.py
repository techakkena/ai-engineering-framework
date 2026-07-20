from __future__ import annotations

"""Tests for ai_memory.summary.exceptions."""

from ai_memory.summary.exceptions import (
    SummaryError,
    SummaryNotFoundError,
    SummaryStateError,
    SummaryValidationError,
)


def test_exception_inheritance() -> None:
    assert issubclass(SummaryNotFoundError, SummaryError)
    assert issubclass(SummaryValidationError, SummaryError)
    assert issubclass(SummaryStateError, SummaryError)


def test_raise_summary_not_found_error() -> None:
    try:
        raise SummaryNotFoundError("not found")
    except SummaryNotFoundError as exc:
        assert str(exc) == "not found"


def test_raise_summary_validation_error() -> None:
    try:
        raise SummaryValidationError("validation")
    except SummaryValidationError as exc:
        assert str(exc) == "validation"


def test_raise_summary_state_error() -> None:
    try:
        raise SummaryStateError("state")
    except SummaryStateError as exc:
        assert str(exc) == "state"
