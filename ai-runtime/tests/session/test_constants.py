"""
Unit tests for ai_runtime.session.constants.
"""

from __future__ import annotations

from ai_runtime.session.constants import (
    ACTIVE_STATE,
    CLOSED_STATE,
    CREATED_STATE,
    DEFAULT_CLEANUP_INTERVAL,
    DEFAULT_MAX_SESSIONS,
    DEFAULT_SESSION_ID,
    DEFAULT_SESSION_STATE,
    DEFAULT_SESSION_TIMEOUT,
    EXPIRED_STATE,
    IDLE_STATE,
    SUPPORTED_SESSION_STATES,
)


def test_session_defaults() -> None:
    """Test session default constants."""
    assert DEFAULT_SESSION_ID == "session"
    assert DEFAULT_SESSION_STATE == CREATED_STATE
    assert DEFAULT_SESSION_TIMEOUT == 1800


def test_supported_session_states() -> None:
    """Test supported session states."""
    expected = {
        CREATED_STATE,
        ACTIVE_STATE,
        IDLE_STATE,
        EXPIRED_STATE,
        CLOSED_STATE,
    }

    assert SUPPORTED_SESSION_STATES == expected


def test_supported_session_states_are_immutable() -> None:
    """Supported session states should be immutable."""
    assert isinstance(
        SUPPORTED_SESSION_STATES,
        frozenset,
    )


def test_session_configuration_defaults() -> None:
    """Test session configuration defaults."""
    assert DEFAULT_MAX_SESSIONS == 1000
    assert DEFAULT_CLEANUP_INTERVAL == 300