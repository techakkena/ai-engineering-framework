"""Tests for ai_optimization.scheduling.exceptions."""

from __future__ import annotations

import pytest

from ai_optimization.scheduling.exceptions import (
    DuplicateScheduleError,
    ScheduleError,
    ScheduleNotFoundError,
    ScheduleRegistrationError,
    ScheduleValidationError,
    UnsupportedSchedulerError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        ScheduleValidationError,
        ScheduleError,
    )
    assert issubclass(
        ScheduleRegistrationError,
        ScheduleError,
    )
    assert issubclass(
        ScheduleNotFoundError,
        ScheduleRegistrationError,
    )
    assert issubclass(
        DuplicateScheduleError,
        ScheduleRegistrationError,
    )
    assert issubclass(
        UnsupportedSchedulerError,
        ScheduleValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (ScheduleError, "base"),
        (ScheduleValidationError, "validation"),
        (ScheduleRegistrationError, "registration"),
        (ScheduleNotFoundError, "missing"),
        (DuplicateScheduleError, "duplicate"),
        (UnsupportedSchedulerError, "scheduler"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)