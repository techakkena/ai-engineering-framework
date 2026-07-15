"""
Unit tests for ai_runtime.scheduler.constants.
"""

from __future__ import annotations

from ai_runtime.scheduler.constants import (
    DEFAULT_MAX_QUEUE_SIZE,
    DEFAULT_POLL_INTERVAL,
    DEFAULT_SCHEDULER_MODE,
    DEFAULT_SCHEDULER_NAME,
    DEFAULT_SCHEDULER_STATE,
    FIFO_MODE,
    IDLE_STATE,
    PAUSED_STATE,
    PRIORITY_MODE,
    ROUND_ROBIN_MODE,
    RUNNING_STATE,
    STOPPED_STATE,
    SUPPORTED_SCHEDULER_MODES,
    SUPPORTED_SCHEDULER_STATES,
)


def test_scheduler_defaults() -> None:
    """Test scheduler default constants."""
    assert DEFAULT_SCHEDULER_NAME == "scheduler"
    assert DEFAULT_SCHEDULER_MODE == FIFO_MODE
    assert DEFAULT_SCHEDULER_STATE == IDLE_STATE


def test_supported_scheduler_modes() -> None:
    """Test supported scheduler modes."""
    expected = {
        FIFO_MODE,
        PRIORITY_MODE,
        ROUND_ROBIN_MODE,
    }

    assert SUPPORTED_SCHEDULER_MODES == expected


def test_scheduler_modes_are_immutable() -> None:
    """Scheduler modes should be immutable."""
    assert isinstance(
        SUPPORTED_SCHEDULER_MODES,
        frozenset,
    )


def test_supported_scheduler_states() -> None:
    """Test supported scheduler states."""
    expected = {
        IDLE_STATE,
        RUNNING_STATE,
        PAUSED_STATE,
        STOPPED_STATE,
    }

    assert SUPPORTED_SCHEDULER_STATES == expected


def test_scheduler_states_are_immutable() -> None:
    """Scheduler states should be immutable."""
    assert isinstance(
        SUPPORTED_SCHEDULER_STATES,
        frozenset,
    )


def test_scheduler_configuration_defaults() -> None:
    """Test scheduler configuration defaults."""
    assert DEFAULT_MAX_QUEUE_SIZE == 1000
    assert DEFAULT_POLL_INTERVAL == 5