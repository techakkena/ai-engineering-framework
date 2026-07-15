"""
Unit tests for ai_runtime.session.exceptions.
"""

from __future__ import annotations

import pytest

from ai_runtime.session.exceptions import (
    InvalidSessionStateError,
    SessionConfigurationError,
    SessionError,
    SessionValidationError,
)


def test_session_error_default_message() -> None:
    """Test SessionError default message."""
    error = SessionError()

    assert str(error) == "A session error occurred."


def test_session_error_custom_message() -> None:
    """Test SessionError custom message."""
    error = SessionError("Custom session error.")

    assert str(error) == "Custom session error."


@pytest.mark.parametrize(
    "state",
    [
        "",
        "running",
        "terminated",
    ],
)
def test_invalid_session_state_error(
    state: str,
) -> None:
    """Test InvalidSessionStateError."""
    error = InvalidSessionStateError(state)

    assert isinstance(error, SessionError)
    assert error.state == state
    assert (
        str(error)
        == f"Invalid session state: '{state}'."
    )


def test_session_configuration_error() -> None:
    """Test SessionConfigurationError."""
    configuration = "cleanup_interval"

    error = SessionConfigurationError(
        configuration,
    )

    assert isinstance(error, SessionError)
    assert error.configuration == configuration

    assert (
        str(error)
        == (
            "Invalid session configuration: "
            f"'{configuration}'."
        )
    )


def test_session_validation_error() -> None:
    """Test SessionValidationError."""
    session = "session-001"
    reason = "expired"

    error = SessionValidationError(
        session,
        reason,
    )

    assert isinstance(error, SessionError)
    assert error.session == session
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Session '{session}' "
            f"validation failed: {reason}."
        )
    )