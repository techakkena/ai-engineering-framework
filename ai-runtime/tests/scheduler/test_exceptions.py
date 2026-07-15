"""
Unit tests for ai_runtime.scheduler.exceptions.
"""

from __future__ import annotations

import pytest

from ai_runtime.scheduler.exceptions import (
    InvalidSchedulerModeError,
    SchedulerConfigurationError,
    SchedulerError,
    SchedulerValidationError,
)


def test_scheduler_error_default_message() -> None:
    """Test SchedulerError default message."""
    error = SchedulerError()

    assert str(error) == "A scheduler error occurred."


def test_scheduler_error_custom_message() -> None:
    """Test SchedulerError custom message."""
    error = SchedulerError(
        "Custom scheduler error.",
    )

    assert str(error) == "Custom scheduler error."


@pytest.mark.parametrize(
    "mode",
    [
        "",
        "random",
        "weighted",
    ],
)
def test_invalid_scheduler_mode_error(
    mode: str,
) -> None:
    """Test InvalidSchedulerModeError."""
    error = InvalidSchedulerModeError(mode)

    assert isinstance(error, SchedulerError)
    assert error.mode == mode

    assert (
        str(error)
        == f"Invalid scheduler mode: '{mode}'."
    )


def test_scheduler_configuration_error() -> None:
    """Test SchedulerConfigurationError."""
    configuration = "queue_size"

    error = SchedulerConfigurationError(
        configuration,
    )

    assert isinstance(error, SchedulerError)
    assert error.configuration == configuration

    assert (
        str(error)
        == (
            "Invalid scheduler configuration: "
            f"'{configuration}'."
        )
    )


def test_scheduler_validation_error() -> None:
    """Test SchedulerValidationError."""
    scheduler = "default"
    reason = "queue overflow"

    error = SchedulerValidationError(
        scheduler,
        reason,
    )

    assert isinstance(error, SchedulerError)
    assert error.scheduler == scheduler
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Scheduler '{scheduler}' "
            f"validation failed: {reason}."
        )
    )