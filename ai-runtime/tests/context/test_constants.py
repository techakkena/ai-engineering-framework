"""
Unit tests for ai_runtime.context.constants.
"""

from __future__ import annotations

from ai_runtime.context.constants import (
    ACTIVE_STATE,
    AGENT_SCOPE,
    DEFAULT_CONTEXT_ID,
    DEFAULT_CONTEXT_SCOPE,
    DEFAULT_CONTEXT_STATE,
    DEFAULT_CONTEXT_TIMEOUT,
    DEFAULT_MAX_CONTEXT_SIZE,
    EXPIRED_STATE,
    GLOBAL_SCOPE,
    INACTIVE_STATE,
    REQUEST_SCOPE,
    SESSION_SCOPE,
    SUPPORTED_CONTEXT_SCOPES,
    SUPPORTED_CONTEXT_STATES,
    WORKFLOW_SCOPE,
)


def test_context_defaults() -> None:
    """Test default context constants."""
    assert DEFAULT_CONTEXT_ID == "context"
    assert DEFAULT_CONTEXT_SCOPE == REQUEST_SCOPE
    assert DEFAULT_CONTEXT_STATE == ACTIVE_STATE


def test_supported_context_scopes() -> None:
    """Test supported context scopes."""
    expected = {
        REQUEST_SCOPE,
        SESSION_SCOPE,
        WORKFLOW_SCOPE,
        AGENT_SCOPE,
        GLOBAL_SCOPE,
    }

    assert SUPPORTED_CONTEXT_SCOPES == expected


def test_context_scopes_are_immutable() -> None:
    """Context scopes should be immutable."""
    assert isinstance(
        SUPPORTED_CONTEXT_SCOPES,
        frozenset,
    )


def test_supported_context_states() -> None:
    """Test supported context states."""
    expected = {
        ACTIVE_STATE,
        INACTIVE_STATE,
        EXPIRED_STATE,
    }

    assert SUPPORTED_CONTEXT_STATES == expected


def test_context_states_are_immutable() -> None:
    """Context states should be immutable."""
    assert isinstance(
        SUPPORTED_CONTEXT_STATES,
        frozenset,
    )


def test_context_configuration_defaults() -> None:
    """Test context configuration defaults."""
    assert DEFAULT_CONTEXT_TIMEOUT == 300
    assert DEFAULT_MAX_CONTEXT_SIZE == 1024