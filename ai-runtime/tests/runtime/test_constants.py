"""
Unit tests for ai_runtime.runtime.constants.
"""

from __future__ import annotations

from ai_runtime.runtime.constants import (
    ASYNC_MODE,
    COMPLETED_STATE,
    DEFAULT_HEARTBEAT_INTERVAL,
    DEFAULT_RUNTIME_ID,
    DEFAULT_RUNTIME_MODE,
    DEFAULT_RUNTIME_STATE,
    DEFAULT_SHUTDOWN_TIMEOUT,
    DISTRIBUTED_MODE,
    EXECUTING_STATE,
    FAILED_STATE,
    IDLE_STATE,
    SUPPORTED_RUNTIME_MODES,
    SUPPORTED_RUNTIME_STATES,
    SYNC_MODE,
    WAITING_STATE,
)


def test_runtime_defaults() -> None:
    """Test runtime default constants."""
    assert DEFAULT_RUNTIME_ID == "runtime"
    assert DEFAULT_RUNTIME_MODE == SYNC_MODE
    assert DEFAULT_RUNTIME_STATE == IDLE_STATE


def test_supported_runtime_modes() -> None:
    """Test supported runtime modes."""
    expected = {
        SYNC_MODE,
        ASYNC_MODE,
        DISTRIBUTED_MODE,
    }

    assert SUPPORTED_RUNTIME_MODES == expected


def test_runtime_modes_are_immutable() -> None:
    """Runtime modes should be immutable."""
    assert isinstance(
        SUPPORTED_RUNTIME_MODES,
        frozenset,
    )


def test_supported_runtime_states() -> None:
    """Test supported runtime states."""
    expected = {
        IDLE_STATE,
        EXECUTING_STATE,
        WAITING_STATE,
        COMPLETED_STATE,
        FAILED_STATE,
    }

    assert SUPPORTED_RUNTIME_STATES == expected


def test_runtime_states_are_immutable() -> None:
    """Runtime states should be immutable."""
    assert isinstance(
        SUPPORTED_RUNTIME_STATES,
        frozenset,
    )


def test_runtime_configuration_defaults() -> None:
    """Test runtime configuration defaults."""
    assert DEFAULT_HEARTBEAT_INTERVAL == 30
    assert DEFAULT_SHUTDOWN_TIMEOUT == 60