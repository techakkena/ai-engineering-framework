"""Tests for ai_optimization.tuning.exceptions."""

from __future__ import annotations

import pytest

from ai_optimization.tuning.exceptions import (
    DuplicateTuningError,
    TuningError,
    TuningNotFoundError,
    TuningRegistrationError,
    TuningValidationError,
    UnsupportedTuningStrategyError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(TuningValidationError, TuningError)
    assert issubclass(
        TuningRegistrationError,
        TuningError,
    )
    assert issubclass(
        TuningNotFoundError,
        TuningRegistrationError,
    )
    assert issubclass(
        DuplicateTuningError,
        TuningRegistrationError,
    )
    assert issubclass(
        UnsupportedTuningStrategyError,
        TuningValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (TuningError, "base"),
        (TuningValidationError, "validation"),
        (TuningRegistrationError, "registration"),
        (TuningNotFoundError, "missing"),
        (DuplicateTuningError, "duplicate"),
        (UnsupportedTuningStrategyError, "strategy"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)