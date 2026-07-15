"""
Unit tests for ai_runtime.base.operations.
"""

from __future__ import annotations

import pytest

from ai_runtime.base.exceptions import (
    InvalidRuntimeError,
)
from ai_runtime.base.operations import (
    build_runtime_name,
    is_supported_runtime_status,
    normalize_runtime_name,
    validate_runtime_name,
    validate_runtime_status,
)


# ============================================================================
# normalize_runtime_name
# ============================================================================


@pytest.mark.parametrize(
    ("runtime", "expected"),
    [
        ("AI Runtime", "ai runtime"),
        (" AGENT ", "agent"),
        ("Workflow", "workflow"),
    ],
)
def test_normalize_runtime_name(
    runtime: str,
    expected: str,
) -> None:
    """Test runtime normalization."""
    assert normalize_runtime_name(runtime) == expected


# ============================================================================
# validate_runtime_name
# ============================================================================


@pytest.mark.parametrize(
    "runtime",
    [
        "runtime",
        "agent-runtime",
        "workflow_runtime",
        "runtime123",
    ],
)
def test_validate_runtime_name(
    runtime: str,
) -> None:
    """Test valid runtime names."""
    assert validate_runtime_name(runtime) == runtime


@pytest.mark.parametrize(
    "runtime",
    [
        "",
        "123runtime",
        "runtime name",
        "@runtime",
    ],
)
def test_validate_runtime_name_invalid(
    runtime: str,
) -> None:
    """Invalid runtime names should raise."""
    with pytest.raises(
        InvalidRuntimeError,
    ):
        validate_runtime_name(runtime)


# ============================================================================
# validate_runtime_status
# ============================================================================


@pytest.mark.parametrize(
    "status",
    [
        "initialized",
        "starting",
        "running",
        "paused",
        "stopping",
        "stopped",
        "failed",
    ],
)
def test_validate_runtime_status(
    status: str,
) -> None:
    """Test valid runtime statuses."""
    assert validate_runtime_status(status) == status


@pytest.mark.parametrize(
    "status",
    [
        "",
        "ready",
        "completed",
        "unknown",
    ],
)
def test_validate_runtime_status_invalid(
    status: str,
) -> None:
    """Invalid runtime statuses should raise."""
    with pytest.raises(
        InvalidRuntimeError,
    ):
        validate_runtime_status(status)


# ============================================================================
# is_supported_runtime_status
# ============================================================================


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        ("running", True),
        ("paused", True),
        ("failed", True),
        ("ready", False),
        ("completed", False),
    ],
)
def test_is_supported_runtime_status(
    status: str,
    expected: bool,
) -> None:
    """Test runtime status support."""
    assert (
        is_supported_runtime_status(status)
        is expected
    )


# ============================================================================
# build_runtime_name
# ============================================================================


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("AI Runtime", "ai-runtime"),
        ("Agent Runtime", "agent-runtime"),
        ("Workflow Engine", "workflow-engine"),
    ],
)
def test_build_runtime_name(
    name: str,
    expected: str,
) -> None:
    """Test runtime name generation."""
    assert build_runtime_name(name) == expected