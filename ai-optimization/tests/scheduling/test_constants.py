"""Tests for ai_optimization.scheduling.constants."""

from __future__ import annotations

from ai_optimization.scheduling import constants


def test_default_values() -> None:
    assert constants.DEFAULT_SCHEDULE_NAME == "schedule"
    assert constants.DEFAULT_SCHEDULER == "fifo"
    assert constants.DEFAULT_ENABLED is True


def test_supported_schedulers() -> None:
    assert constants.SUPPORTED_SCHEDULERS == frozenset(
        {
            "fifo",
            "priority",
            "round_robin",
            "adaptive",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_SCHEDULE_NAME_LENGTH == 1
    assert constants.MAX_SCHEDULE_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.SCHEDULER_KEY == "scheduler"
    assert constants.MAX_CONCURRENCY_KEY == "max_concurrency"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"