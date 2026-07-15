"""
Unit tests for ai_runtime.runtime.exceptions.
"""

from __future__ import annotations

import pytest

from ai_runtime.runtime.exceptions import (
    InvalidRuntimeModeError,
    RuntimeExecutionError,
    RuntimeInitializationError,
    RuntimeStateError,
)


def test_runtime_execution_error_default_message() -> None:
    """Test RuntimeExecutionError."""
    error = RuntimeExecutionError()

    assert str(error) == (
        "A runtime execution error occurred."
    )


def test_runtime_execution_error_custom_message() -> None:
    """Test RuntimeExecutionError custom message."""
    error = RuntimeExecutionError(
        "Custom runtime error."
    )

    assert str(error) == "Custom runtime error."


@pytest.mark.parametrize(
    "runtime",
    [
        "",
        "agent-runtime",
        "workflow-runtime",
    ],
)
def test_runtime_initialization_error(
    runtime: str,
) -> None:
    """Test RuntimeInitializationError."""
    error = RuntimeInitializationError(runtime)

    assert isinstance(
        error,
        RuntimeExecutionError,
    )

    assert error.runtime == runtime

    assert (
        str(error)
        == f"Runtime initialization failed: '{runtime}'."
    )


@pytest.mark.parametrize(
    "state",
    [
        "",
        "ready",
        "unknown",
    ],
)
def test_runtime_state_error(
    state: str,
) -> None:
    """Test RuntimeStateError."""
    error = RuntimeStateError(state)

    assert isinstance(
        error,
        RuntimeExecutionError,
    )

    assert error.state == state

    assert (
        str(error)
        == f"Invalid runtime state: '{state}'."
    )


@pytest.mark.parametrize(
    "mode",
    [
        "",
        "parallel",
        "threaded",
    ],
)
def test_invalid_runtime_mode_error(
    mode: str,
) -> None:
    """Test InvalidRuntimeModeError."""
    error = InvalidRuntimeModeError(mode)

    assert isinstance(
        error,
        RuntimeExecutionError,
    )

    assert error.mode == mode

    assert (
        str(error)
        == f"Invalid runtime mode: '{mode}'."
    )