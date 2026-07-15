"""
Unit tests for ai_runtime.runtime.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_runtime.runtime.exceptions import (
    InvalidRuntimeModeError,
    RuntimeStateError,
)
from ai_runtime.runtime.operations import (
    build_runtime_id,
    is_supported_runtime_mode,
    normalize_runtime_mode,
    validate_runtime_mode,
    validate_runtime_state,
)


# ============================================================================
# normalize_runtime_mode
# ============================================================================


@pytest.mark.parametrize(
    ("mode", "expected"),
    [
        ("SYNC", "sync"),
        (" Async ", "async"),
        ("Distributed", "distributed"),
    ],
)
def test_normalize_runtime_mode(
    mode: str,
    expected: str,
) -> None:
    """Test runtime mode normalization."""
    assert normalize_runtime_mode(mode) == expected


# ============================================================================
# validate_runtime_mode
# ============================================================================


@pytest.mark.parametrize(
    "mode",
    [
        "sync",
        "async",
        "distributed",
    ],
)
def test_validate_runtime_mode(
    mode: str,
) -> None:
    """Test supported runtime modes."""
    assert validate_runtime_mode(mode) == mode


@pytest.mark.parametrize(
    "mode",
    [
        "",
        "parallel",
        "threaded",
    ],
)
def test_validate_runtime_mode_invalid(
    mode: str,
) -> None:
    """Invalid runtime modes should raise."""
    with pytest.raises(
        InvalidRuntimeModeError,
    ):
        validate_runtime_mode(mode)


# ============================================================================
# validate_runtime_state
# ============================================================================


@pytest.mark.parametrize(
    "state",
    [
        "idle",
        "executing",
        "waiting",
        "completed",
        "failed",
    ],
)
def test_validate_runtime_state(
    state: str,
) -> None:
    """Test supported runtime states."""
    assert validate_runtime_state(state) == state


@pytest.mark.parametrize(
    "state",
    [
        "",
        "running",
        "paused",
        "terminated",
    ],
)
def test_validate_runtime_state_invalid(
    state: str,
) -> None:
    """Invalid runtime states should raise."""
    with pytest.raises(
        RuntimeStateError,
    ):
        validate_runtime_state(state)


# ============================================================================
# is_supported_runtime_mode
# ============================================================================


@pytest.mark.parametrize(
    ("mode", "expected"),
    [
        ("sync", True),
        ("async", True),
        ("distributed", True),
        ("parallel", False),
        ("threaded", False),
    ],
)
def test_is_supported_runtime_mode(
    mode: str,
    expected: bool,
) -> None:
    """Test runtime mode support."""
    assert (
        is_supported_runtime_mode(mode)
        is expected
    )


# ============================================================================
# build_runtime_id
# ============================================================================


def test_build_runtime_id() -> None:
    """Test runtime ID generation."""
    runtime_id = build_runtime_id()

    assert runtime_id.startswith("runtime-")

    pattern = re.compile(
        (
            r"^runtime-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(runtime_id) is not None