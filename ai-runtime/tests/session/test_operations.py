"""
Unit tests for ai_runtime.session.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_runtime.session.exceptions import (
    InvalidSessionStateError,
)
from ai_runtime.session.operations import (
    build_session_id,
    is_supported_session_state,
    normalize_session_state,
    validate_session_id,
    validate_session_state,
)


# ============================================================================
# normalize_session_state
# ============================================================================


@pytest.mark.parametrize(
    ("state", "expected"),
    [
        ("CREATED", "created"),
        (" Active ", "active"),
        ("Idle", "idle"),
        ("Expired", "expired"),
        ("Closed", "closed"),
    ],
)
def test_normalize_session_state(
    state: str,
    expected: str,
) -> None:
    """Test session state normalization."""
    assert normalize_session_state(state) == expected


# ============================================================================
# validate_session_state
# ============================================================================


@pytest.mark.parametrize(
    "state",
    [
        "created",
        "active",
        "idle",
        "expired",
        "closed",
    ],
)
def test_validate_session_state(
    state: str,
) -> None:
    """Test valid session states."""
    assert validate_session_state(state) == state


@pytest.mark.parametrize(
    "state",
    [
        "",
        "running",
        "terminated",
        "paused",
    ],
)
def test_validate_session_state_invalid(
    state: str,
) -> None:
    """Invalid session states should raise."""
    with pytest.raises(
        InvalidSessionStateError,
    ):
        validate_session_state(state)


# ============================================================================
# is_supported_session_state
# ============================================================================


@pytest.mark.parametrize(
    ("state", "expected"),
    [
        ("created", True),
        ("active", True),
        ("idle", True),
        ("expired", True),
        ("closed", True),
        ("running", False),
        ("terminated", False),
    ],
)
def test_is_supported_session_state(
    state: str,
    expected: bool,
) -> None:
    """Test supported session state detection."""
    assert (
        is_supported_session_state(state)
        is expected
    )


# ============================================================================
# validate_session_id
# ============================================================================


@pytest.mark.parametrize(
    "session_id",
    [
        "session",
        "session_001",
        "session-01",
        "runtime123",
    ],
)
def test_validate_session_id(
    session_id: str,
) -> None:
    """Test valid session identifiers."""
    assert (
        validate_session_id(session_id)
        == session_id.lower()
    )


@pytest.mark.parametrize(
    "session_id",
    [
        "",
        "123session",
        "session name",
        "@session",
    ],
)
def test_validate_session_id_invalid(
    session_id: str,
) -> None:
    """Invalid session identifiers should raise."""
    with pytest.raises(ValueError):
        validate_session_id(session_id)


# ============================================================================
# build_session_id
# ============================================================================


def test_build_session_id() -> None:
    """Test session ID generation."""
    session_id = build_session_id()

    assert session_id.startswith("session-")

    pattern = re.compile(
        (
            r"^session-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(session_id) is not None