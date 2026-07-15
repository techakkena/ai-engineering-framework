"""
Unit tests for ai_runtime.lifecycle.constants.
"""

from __future__ import annotations

from ai_runtime.lifecycle.constants import (
    ACTIVE_STATE,
    CREATED_PHASE,
    DEFAULT_LIFECYCLE_NAME,
    DEFAULT_LIFECYCLE_PHASE,
    DEFAULT_LIFECYCLE_STATE,
    DEFAULT_SHUTDOWN_TIMEOUT,
    DEFAULT_STARTUP_TIMEOUT,
    FAILED_STATE,
    INITIALIZING_PHASE,
    INACTIVE_STATE,
    RUNNING_PHASE,
    STARTING_PHASE,
    STOPPED_PHASE,
    STOPPING_PHASE,
    SUPPORTED_LIFECYCLE_PHASES,
    SUPPORTED_LIFECYCLE_STATES,
    TERMINATED_PHASE,
)


def test_lifecycle_defaults() -> None:
    """Test lifecycle default constants."""
    assert DEFAULT_LIFECYCLE_NAME == "lifecycle"
    assert DEFAULT_LIFECYCLE_PHASE == CREATED_PHASE
    assert DEFAULT_LIFECYCLE_STATE == INACTIVE_STATE


def test_supported_lifecycle_phases() -> None:
    """Test supported lifecycle phases."""
    expected = {
        CREATED_PHASE,
        INITIALIZING_PHASE,
        STARTING_PHASE,
        RUNNING_PHASE,
        STOPPING_PHASE,
        STOPPED_PHASE,
        TERMINATED_PHASE,
    }

    assert SUPPORTED_LIFECYCLE_PHASES == expected


def test_lifecycle_phases_are_immutable() -> None:
    """Lifecycle phases should be immutable."""
    assert isinstance(
        SUPPORTED_LIFECYCLE_PHASES,
        frozenset,
    )


def test_supported_lifecycle_states() -> None:
    """Test supported lifecycle states."""
    expected = {
        ACTIVE_STATE,
        INACTIVE_STATE,
        FAILED_STATE,
    }

    assert SUPPORTED_LIFECYCLE_STATES == expected


def test_lifecycle_states_are_immutable() -> None:
    """Lifecycle states should be immutable."""
    assert isinstance(
        SUPPORTED_LIFECYCLE_STATES,
        frozenset,
    )


def test_lifecycle_configuration_defaults() -> None:
    """Test lifecycle configuration defaults."""
    assert DEFAULT_STARTUP_TIMEOUT == 60
    assert DEFAULT_SHUTDOWN_TIMEOUT == 60