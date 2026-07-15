"""
Unit tests for ai_runtime.state.constants.
"""

from __future__ import annotations

from ai_runtime.state.constants import (
    AGENT_STATE,
    CANCELLED_STATUS,
    COMPLETED_STATUS,
    DEFAULT_STATE_HISTORY_SIZE,
    DEFAULT_STATE_NAME,
    DEFAULT_STATE_STATUS,
    DEFAULT_STATE_TIMEOUT,
    DEFAULT_STATE_TYPE,
    FAILED_STATUS,
    PENDING_STATUS,
    READY_STATUS,
    RUNNING_STATUS,
    RUNTIME_STATE,
    SUPPORTED_STATE_STATUSES,
    TASK_STATE,
    WORKFLOW_STATE,
)


def test_state_defaults() -> None:
    """Test state default constants."""
    assert DEFAULT_STATE_NAME == "state"
    assert DEFAULT_STATE_STATUS == PENDING_STATUS
    assert DEFAULT_STATE_TYPE == RUNTIME_STATE


def test_supported_state_statuses() -> None:
    """Test supported state statuses."""
    expected = {
        PENDING_STATUS,
        READY_STATUS,
        RUNNING_STATUS,
        COMPLETED_STATUS,
        FAILED_STATUS,
        CANCELLED_STATUS,
    }

    assert SUPPORTED_STATE_STATUSES == expected


def test_supported_state_statuses_are_immutable() -> None:
    """State statuses should be immutable."""
    assert isinstance(
        SUPPORTED_STATE_STATUSES,
        frozenset,
    )


def test_state_types() -> None:
    """Test state type constants."""
    assert RUNTIME_STATE == "runtime"
    assert WORKFLOW_STATE == "workflow"
    assert TASK_STATE == "task"
    assert AGENT_STATE == "agent"


def test_state_configuration_defaults() -> None:
    """Test configuration defaults."""
    assert DEFAULT_STATE_HISTORY_SIZE == 100
    assert DEFAULT_STATE_TIMEOUT == 300