"""
Unit tests for ai_runtime.base.exceptions.
"""

from __future__ import annotations

import pytest

from ai_runtime.base.exceptions import (
    InvalidRuntimeError,
    RuntimeConfigurationError,
    RuntimeError,
    RuntimeValidationError,
)


def test_runtime_error_default_message() -> None:
    """Test RuntimeError default message."""
    error = RuntimeError()

    assert str(error) == "A runtime error occurred."


def test_runtime_error_custom_message() -> None:
    """Test RuntimeError custom message."""
    error = RuntimeError("Custom runtime error.")

    assert str(error) == "Custom runtime error."


@pytest.mark.parametrize(
    "runtime",
    [
        "",
        "unknown",
        "invalid",
    ],
)
def test_invalid_runtime_error(
    runtime: str,
) -> None:
    """Test InvalidRuntimeError."""
    error = InvalidRuntimeError(runtime)

    assert isinstance(error, RuntimeError)
    assert error.runtime == runtime
    assert (
        str(error)
        == f"Invalid runtime: '{runtime}'."
    )


def test_runtime_validation_error() -> None:
    """Test RuntimeValidationError."""
    runtime = "agent-runtime"
    reason = "unsupported version"

    error = RuntimeValidationError(
        runtime,
        reason,
    )

    assert isinstance(error, RuntimeError)
    assert error.runtime == runtime
    assert error.reason == reason
    assert (
        str(error)
        == (
            f"Runtime '{runtime}' "
            f"validation failed: {reason}."
        )
    )


def test_runtime_configuration_error() -> None:
    """Test RuntimeConfigurationError."""
    configuration = "workers"

    error = RuntimeConfigurationError(
        configuration,
    )

    assert isinstance(error, RuntimeError)
    assert error.configuration == configuration
    assert (
        str(error)
        == (
            "Invalid runtime configuration: "
            f"'{configuration}'."
        )
    )