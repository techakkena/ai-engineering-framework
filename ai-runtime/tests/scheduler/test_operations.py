"""
Unit tests for ai_runtime.scheduler.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_runtime.scheduler.exceptions import (
    InvalidSchedulerModeError,
)
from ai_runtime.scheduler.operations import (
    build_scheduler_id,
    is_supported_scheduler_mode,
    normalize_scheduler_mode,
    validate_scheduler_id,
    validate_scheduler_mode,
)


# ============================================================================
# normalize_scheduler_mode
# ============================================================================


@pytest.mark.parametrize(
    ("mode", "expected"),
    [
        ("FIFO", "fifo"),
        (" Priority ", "priority"),
        ("ROUND_ROBIN", "round_robin"),
    ],
)
def test_normalize_scheduler_mode(
    mode: str,
    expected: str,
) -> None:
    """Test scheduler mode normalization."""
    assert normalize_scheduler_mode(mode) == expected


# ============================================================================
# validate_scheduler_mode
# ============================================================================


@pytest.mark.parametrize(
    "mode",
    [
        "fifo",
        "priority",
        "round_robin",
    ],
)
def test_validate_scheduler_mode(
    mode: str,
) -> None:
    """Test valid scheduler modes."""
    assert validate_scheduler_mode(mode) == mode


@pytest.mark.parametrize(
    "mode",
    [
        "",
        "weighted",
        "random",
        "parallel",
    ],
)
def test_validate_scheduler_mode_invalid(
    mode: str,
) -> None:
    """Invalid scheduler modes should raise."""
    with pytest.raises(
        InvalidSchedulerModeError,
    ):
        validate_scheduler_mode(mode)


# ============================================================================
# is_supported_scheduler_mode
# ============================================================================


@pytest.mark.parametrize(
    ("mode", "expected"),
    [
        ("fifo", True),
        ("priority", True),
        ("round_robin", True),
        ("weighted", False),
        ("random", False),
    ],
)
def test_is_supported_scheduler_mode(
    mode: str,
    expected: bool,
) -> None:
    """Test supported scheduler mode detection."""
    assert (
        is_supported_scheduler_mode(mode)
        is expected
    )


# ============================================================================
# validate_scheduler_id
# ============================================================================


@pytest.mark.parametrize(
    "scheduler_id",
    [
        "scheduler",
        "scheduler_01",
        "scheduler-01",
        "runtime123",
    ],
)
def test_validate_scheduler_id(
    scheduler_id: str,
) -> None:
    """Test valid scheduler identifiers."""
    assert (
        validate_scheduler_id(scheduler_id)
        == scheduler_id.lower()
    )


@pytest.mark.parametrize(
    "scheduler_id",
    [
        "",
        "123scheduler",
        "scheduler name",
        "@scheduler",
    ],
)
def test_validate_scheduler_id_invalid(
    scheduler_id: str,
) -> None:
    """Invalid scheduler identifiers should raise."""
    with pytest.raises(ValueError):
        validate_scheduler_id(scheduler_id)


# ============================================================================
# build_scheduler_id
# ============================================================================


def test_build_scheduler_id() -> None:
    """Test scheduler ID generation."""
    scheduler_id = build_scheduler_id()

    assert scheduler_id.startswith("scheduler-")

    pattern = re.compile(
        (
            r"^scheduler-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(scheduler_id) is not None