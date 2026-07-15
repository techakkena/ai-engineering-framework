"""
Unit tests for ai_runtime.executor.exceptions.
"""

from __future__ import annotations

import pytest

from ai_runtime.executor.exceptions import (
    ExecutorConfigurationError,
    ExecutorError,
    ExecutorValidationError,
    InvalidExecutorModeError,
)


def test_executor_error_default_message() -> None:
    """Test ExecutorError default message."""
    error = ExecutorError()

    assert str(error) == "An executor error occurred."


def test_executor_error_custom_message() -> None:
    """Test ExecutorError custom message."""
    error = ExecutorError("Custom executor error.")

    assert str(error) == "Custom executor error."


@pytest.mark.parametrize(
    "mode",
    [
        "",
        "distributed",
        "threaded",
    ],
)
def test_invalid_executor_mode_error(
    mode: str,
) -> None:
    """Test InvalidExecutorModeError."""
    error = InvalidExecutorModeError(mode)

    assert isinstance(error, ExecutorError)
    assert error.mode == mode

    assert (
        str(error)
        == f"Invalid executor mode: '{mode}'."
    )


def test_executor_configuration_error() -> None:
    """Test ExecutorConfigurationError."""
    configuration = "max_concurrency"

    error = ExecutorConfigurationError(
        configuration,
    )

    assert isinstance(error, ExecutorError)
    assert error.configuration == configuration

    assert (
        str(error)
        == (
            "Invalid executor configuration: "
            f"'{configuration}'."
        )
    )


def test_executor_validation_error() -> None:
    """Test ExecutorValidationError."""
    executor = "default"
    reason = "configuration mismatch"

    error = ExecutorValidationError(
        executor,
        reason,
    )

    assert isinstance(error, ExecutorError)
    assert error.executor == executor
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Executor '{executor}' "
            f"validation failed: {reason}."
        )
    )