"""
Unit tests for ai_runtime.state.exceptions.
"""

from __future__ import annotations

import pytest

from ai_runtime.state.exceptions import (
    InvalidStateStatusError,
    StateConfigurationError,
    StateError,
    StateValidationError,
)


def test_state_error_default_message() -> None:
    """Test StateError default message."""
    error = StateError()

    assert str(error) == "A state error occurred."


def test_state_error_custom_message() -> None:
    """Test StateError custom message."""
    error = StateError(
        "Custom state error.",
    )

    assert str(error) == "Custom state error."


@pytest.mark.parametrize(
    "status",
    [
        "",
        "waiting",
        "terminated",
    ],
)
def test_invalid_state_status_error(
    status: str,
) -> None:
    """Test InvalidStateStatusError."""
    error = InvalidStateStatusError(status)

    assert isinstance(error, StateError)
    assert error.status == status

    assert (
        str(error)
        == f"Invalid state status: '{status}'."
    )


def test_state_configuration_error() -> None:
    """Test StateConfigurationError."""
    configuration = "history_size"

    error = StateConfigurationError(
        configuration,
    )

    assert isinstance(error, StateError)
    assert error.configuration == configuration

    assert (
        str(error)
        == (
            "Invalid state configuration: "
            f"'{configuration}'."
        )
    )


def test_state_validation_error() -> None:
    """Test StateValidationError."""
    state = "runtime"
    reason = "invalid transition"

    error = StateValidationError(
        state,
        reason,
    )

    assert isinstance(error, StateError)
    assert error.state == state
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"State '{state}' "
            f"validation failed: {reason}."
        )
    )