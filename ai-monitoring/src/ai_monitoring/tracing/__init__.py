"""
Unit tests for ai_monitoring.logging.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.logging.exceptions import (
    LogValidationError,
)
from ai_monitoring.logging.operations import (
    LogResult,
    clear_logs,
    get_log,
    list_logs,
    log_event,
    log_message,
)


def test_log_message_success() -> None:
    """Logging a message should succeed."""
    result = log_message("Application started")

    assert isinstance(result, LogResult)
    assert result.success is True
    assert result.task == "log_message"


def test_log_message_empty() -> None:
    """Empty log messages should raise."""
    with pytest.raises(LogValidationError):
        log_message("")


def test_log_event_success() -> None:
    """Logging an event should succeed."""
    result = log_event("startup")

    assert result.success is True
    assert result.task == "log_event"


def test_get_log_success() -> None:
    """Retrieving a log should succeed."""
    result = get_log("log-001")

    assert result.success is True
    assert result.task == "get_log"


def test_list_logs_success() -> None:
    """Listing logs should succeed."""
    result = list_logs()

    assert result.success is True
    assert result.task == "list_logs"
    assert isinstance(result.data["logs"], list)


def test_clear_logs_success() -> None:
    """Clearing logs should succeed."""
    result = clear_logs()

    assert result.success is True
    assert result.task == "clear_logs"
    assert result.data["cleared"] is True


@pytest.mark.parametrize(
    "operation",
    [
        log_event,
        get_log,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """Operations requiring a non-empty identifier should reject empty values."""
    with pytest.raises(LogValidationError):
        operation("")