"""
Unit tests for ai_runtime.state.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_runtime.state.exceptions import (
    InvalidStateStatusError,
)
from ai_runtime.state.operations import (
    build_state_id,
    is_supported_state_status,
    normalize_state_status,
    validate_state_id,
    validate_state_status,
)


# ============================================================================
# normalize_state_status
# ============================================================================


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        ("PENDING", "pending"),
        (" Ready ", "ready"),
        ("RUNNING", "running"),
        ("Completed", "completed"),
        ("FAILED", "failed"),
        ("Cancelled", "cancelled"),
    ],
)
def test_normalize_state_status(
    status: str,
    expected: str,
) -> None:
    """Test state status normalization."""
    assert normalize_state_status(status) == expected


# ============================================================================
# validate_state_status
# ============================================================================


@pytest.mark.parametrize(
    "status",
    [
        "pending",
        "ready",
        "running",
        "completed",
        "failed",
        "cancelled",
    ],
)
def test_validate_state_status(
    status: str,
) -> None:
    """Test valid state statuses."""
    assert validate_state_status(status) == status


@pytest.mark.parametrize(
    "status",
    [
        "",
        "waiting",
        "paused",
        "terminated",
    ],
)
def test_validate_state_status_invalid(
    status: str,
) -> None:
    """Invalid state statuses should raise."""
    with pytest.raises(
        InvalidStateStatusError,
    ):
        validate_state_status(status)


# ============================================================================
# is_supported_state_status
# ============================================================================


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        ("pending", True),
        ("ready", True),
        ("running", True),
        ("completed", True),
        ("failed", True),
        ("cancelled", True),
        ("waiting", False),
        ("terminated", False),
    ],
)
def test_is_supported_state_status(
    status: str,
    expected: bool,
) -> None:
    """Test supported state status detection."""
    assert (
        is_supported_state_status(status)
        is expected
    )


# ============================================================================
# validate_state_id
# ============================================================================


@pytest.mark.parametrize(
    "state_id",
    [
        "state",
        "state_01",
        "state-01",
        "runtime123",
    ],
)
def test_validate_state_id(
    state_id: str,
) -> None:
    """Test valid state identifiers."""
    assert (
        validate_state_id(state_id)
        == state_id.lower()
    )


@pytest.mark.parametrize(
    "state_id",
    [
        "",
        "123state",
        "state name",
        "@state",
    ],
)
def test_validate_state_id_invalid(
    state_id: str,
) -> None:
    """Invalid state identifiers should raise."""
    with pytest.raises(ValueError):
        validate_state_id(state_id)


# ============================================================================
# build_state_id
# ============================================================================


def test_build_state_id() -> None:
    """Test state ID generation."""
    state_id = build_state_id()

    assert state_id.startswith("state-")

    pattern = re.compile(
        (
            r"^state-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(state_id) is not None