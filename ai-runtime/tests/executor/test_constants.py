"""
Unit tests for ai_runtime.executor.constants.
"""

from __future__ import annotations

from ai_runtime.executor.constants import (
    ASYNC_MODE,
    COMPLETED_STATE,
    DEFAULT_EXECUTION_TIMEOUT,
    DEFAULT_EXECUTOR_MODE,
    DEFAULT_EXECUTOR_NAME,
    DEFAULT_EXECUTOR_STATE,
    DEFAULT_MAX_CONCURRENCY,
    FAILED_STATE,
    IDLE_STATE,
    PARALLEL_MODE,
    RUNNING_STATE,
    SEQUENTIAL_MODE,
    SUPPORTED_EXECUTOR_MODES,
    SUPPORTED_EXECUTOR_STATES,
)


def test_executor_defaults() -> None:
    """Test executor default constants."""
    assert DEFAULT_EXECUTOR_NAME == "executor"
    assert DEFAULT_EXECUTOR_MODE == SEQUENTIAL_MODE
    assert DEFAULT_EXECUTOR_STATE == IDLE_STATE


def test_supported_executor_modes() -> None:
    """Test supported executor modes."""
    expected = {
        SEQUENTIAL_MODE,
        PARALLEL_MODE,
        ASYNC_MODE,
    }

    assert SUPPORTED_EXECUTOR_MODES == expected


def test_executor_modes_are_immutable() -> None:
    """Executor modes should be immutable."""
    assert isinstance(
        SUPPORTED_EXECUTOR_MODES,
        frozenset,
    )


def test_supported_executor_states() -> None:
    """Test supported executor states."""
    expected = {
        IDLE_STATE,
        RUNNING_STATE,
        COMPLETED_STATE,
        FAILED_STATE,
    }

    assert SUPPORTED_EXECUTOR_STATES == expected


def test_executor_states_are_immutable() -> None:
    """Executor states should be immutable."""
    assert isinstance(
        SUPPORTED_EXECUTOR_STATES,
        frozenset,
    )


def test_executor_configuration_defaults() -> None:
    """Test executor configuration defaults."""
    assert DEFAULT_MAX_CONCURRENCY == 10
    assert DEFAULT_EXECUTION_TIMEOUT == 300