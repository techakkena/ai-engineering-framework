"""
Unit tests for ai_runtime.executor.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_runtime.executor.exceptions import (
    InvalidExecutorModeError,
)
from ai_runtime.executor.operations import (
    build_executor_id,
    is_supported_executor_mode,
    normalize_executor_mode,
    validate_executor_id,
    validate_executor_mode,
)


# ============================================================================
# normalize_executor_mode
# ============================================================================


@pytest.mark.parametrize(
    ("mode", "expected"),
    [
        ("SEQUENTIAL", "sequential"),
        (" Parallel ", "parallel"),
        ("ASYNC", "async"),
    ],
)
def test_normalize_executor_mode(
    mode: str,
    expected: str,
) -> None:
    """Test executor mode normalization."""
    assert normalize_executor_mode(mode) == expected


# ============================================================================
# validate_executor_mode
# ============================================================================


@pytest.mark.parametrize(
    "mode",
    [
        "sequential",
        "parallel",
        "async",
    ],
)
def test_validate_executor_mode(
    mode: str,
) -> None:
    """Test valid executor modes."""
    assert validate_executor_mode(mode) == mode


@pytest.mark.parametrize(
    "mode",
    [
        "",
        "distributed",
        "threaded",
        "batch",
    ],
)
def test_validate_executor_mode_invalid(
    mode: str,
) -> None:
    """Invalid executor modes should raise."""
    with pytest.raises(
        InvalidExecutorModeError,
    ):
        validate_executor_mode(mode)


# ============================================================================
# is_supported_executor_mode
# ============================================================================


@pytest.mark.parametrize(
    ("mode", "expected"),
    [
        ("sequential", True),
        ("parallel", True),
        ("async", True),
        ("distributed", False),
        ("threaded", False),
    ],
)
def test_is_supported_executor_mode(
    mode: str,
    expected: bool,
) -> None:
    """Test supported executor mode detection."""
    assert (
        is_supported_executor_mode(mode)
        is expected
    )


# ============================================================================
# validate_executor_id
# ============================================================================


@pytest.mark.parametrize(
    "executor_id",
    [
        "executor",
        "executor_01",
        "executor-01",
        "runtime123",
    ],
)
def test_validate_executor_id(
    executor_id: str,
) -> None:
    """Test valid executor identifiers."""
    assert (
        validate_executor_id(executor_id)
        == executor_id.lower()
    )


@pytest.mark.parametrize(
    "executor_id",
    [
        "",
        "123executor",
        "executor name",
        "@executor",
    ],
)
def test_validate_executor_id_invalid(
    executor_id: str,
) -> None:
    """Invalid executor identifiers should raise."""
    with pytest.raises(ValueError):
        validate_executor_id(executor_id)


# ============================================================================
# build_executor_id
# ============================================================================


def test_build_executor_id() -> None:
    """Test executor ID generation."""
    executor_id = build_executor_id()

    assert executor_id.startswith("executor-")

    pattern = re.compile(
        (
            r"^executor-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(executor_id) is not None