"""
Unit tests for ai_runtime.lifecycle.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_runtime.lifecycle.exceptions import (
    InvalidLifecyclePhaseError,
)
from ai_runtime.lifecycle.operations import (
    build_lifecycle_id,
    is_supported_lifecycle_phase,
    normalize_lifecycle_phase,
    validate_lifecycle_id,
    validate_lifecycle_phase,
)


# ============================================================================
# normalize_lifecycle_phase
# ============================================================================


@pytest.mark.parametrize(
    ("phase", "expected"),
    [
        ("CREATED", "created"),
        (" Initializing ", "initializing"),
        ("STARTING", "starting"),
        ("Running", "running"),
        ("Stopping", "stopping"),
        ("Stopped", "stopped"),
        ("Terminated", "terminated"),
    ],
)
def test_normalize_lifecycle_phase(
    phase: str,
    expected: str,
) -> None:
    """Test lifecycle phase normalization."""
    assert normalize_lifecycle_phase(phase) == expected


# ============================================================================
# validate_lifecycle_phase
# ============================================================================


@pytest.mark.parametrize(
    "phase",
    [
        "created",
        "initializing",
        "starting",
        "running",
        "stopping",
        "stopped",
        "terminated",
    ],
)
def test_validate_lifecycle_phase(
    phase: str,
) -> None:
    """Test valid lifecycle phases."""
    assert validate_lifecycle_phase(phase) == phase


@pytest.mark.parametrize(
    "phase",
    [
        "",
        "booting",
        "paused",
        "restarting",
    ],
)
def test_validate_lifecycle_phase_invalid(
    phase: str,
) -> None:
    """Invalid lifecycle phases should raise."""
    with pytest.raises(
        InvalidLifecyclePhaseError,
    ):
        validate_lifecycle_phase(phase)


# ============================================================================
# is_supported_lifecycle_phase
# ============================================================================


@pytest.mark.parametrize(
    ("phase", "expected"),
    [
        ("created", True),
        ("running", True),
        ("terminated", True),
        ("booting", False),
        ("paused", False),
    ],
)
def test_is_supported_lifecycle_phase(
    phase: str,
    expected: bool,
) -> None:
    """Test supported lifecycle phase detection."""
    assert (
        is_supported_lifecycle_phase(
            phase,
        )
        is expected
    )


# ============================================================================
# validate_lifecycle_id
# ============================================================================


@pytest.mark.parametrize(
    "lifecycle_id",
    [
        "lifecycle",
        "lifecycle_01",
        "lifecycle-01",
        "runtime123",
    ],
)
def test_validate_lifecycle_id(
    lifecycle_id: str,
) -> None:
    """Test valid lifecycle identifiers."""
    assert (
        validate_lifecycle_id(
            lifecycle_id,
        )
        == lifecycle_id.lower()
    )


@pytest.mark.parametrize(
    "lifecycle_id",
    [
        "",
        "123lifecycle",
        "lifecycle name",
        "@lifecycle",
    ],
)
def test_validate_lifecycle_id_invalid(
    lifecycle_id: str,
) -> None:
    """Invalid lifecycle identifiers should raise."""
    with pytest.raises(ValueError):
        validate_lifecycle_id(
            lifecycle_id,
        )


# ============================================================================
# build_lifecycle_id
# ============================================================================


def test_build_lifecycle_id() -> None:
    """Test lifecycle ID generation."""
    lifecycle_id = build_lifecycle_id()

    assert lifecycle_id.startswith(
        "lifecycle-",
    )

    pattern = re.compile(
        (
            r"^lifecycle-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert (
        pattern.fullmatch(
            lifecycle_id,
        )
        is not None
    )