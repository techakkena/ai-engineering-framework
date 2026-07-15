"""
Unit tests for ai_runtime.context.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_runtime.context.exceptions import (
    InvalidContextScopeError,
)
from ai_runtime.context.operations import (
    build_context_id,
    is_supported_context_scope,
    normalize_context_scope,
    validate_context_id,
    validate_context_scope,
)


# ============================================================================
# normalize_context_scope
# ============================================================================


@pytest.mark.parametrize(
    ("scope", "expected"),
    [
        ("REQUEST", "request"),
        (" Session ", "session"),
        ("Workflow", "workflow"),
        ("Agent", "agent"),
        ("Global", "global"),
    ],
)
def test_normalize_context_scope(
    scope: str,
    expected: str,
) -> None:
    """Test context scope normalization."""
    assert normalize_context_scope(scope) == expected


# ============================================================================
# validate_context_scope
# ============================================================================


@pytest.mark.parametrize(
    "scope",
    [
        "request",
        "session",
        "workflow",
        "agent",
        "global",
    ],
)
def test_validate_context_scope(
    scope: str,
) -> None:
    """Test valid context scopes."""
    assert validate_context_scope(scope) == scope


@pytest.mark.parametrize(
    "scope",
    [
        "",
        "runtime",
        "thread",
        "process",
    ],
)
def test_validate_context_scope_invalid(
    scope: str,
) -> None:
    """Invalid context scopes should raise."""
    with pytest.raises(
        InvalidContextScopeError,
    ):
        validate_context_scope(scope)


# ============================================================================
# is_supported_context_scope
# ============================================================================


@pytest.mark.parametrize(
    ("scope", "expected"),
    [
        ("request", True),
        ("session", True),
        ("workflow", True),
        ("agent", True),
        ("global", True),
        ("runtime", False),
        ("thread", False),
    ],
)
def test_is_supported_context_scope(
    scope: str,
    expected: bool,
) -> None:
    """Test supported context scope detection."""
    assert (
        is_supported_context_scope(scope)
        is expected
    )


# ============================================================================
# validate_context_id
# ============================================================================


@pytest.mark.parametrize(
    "context_id",
    [
        "context",
        "request_context",
        "workflow-01",
        "agent123",
    ],
)
def test_validate_context_id(
    context_id: str,
) -> None:
    """Test valid context identifiers."""
    assert (
        validate_context_id(context_id)
        == context_id.lower()
    )


@pytest.mark.parametrize(
    "context_id",
    [
        "",
        "123context",
        "context name",
        "@context",
    ],
)
def test_validate_context_id_invalid(
    context_id: str,
) -> None:
    """Invalid context identifiers should raise."""
    with pytest.raises(ValueError):
        validate_context_id(context_id)


# ============================================================================
# build_context_id
# ============================================================================


def test_build_context_id() -> None:
    """Test context ID generation."""
    context_id = build_context_id()

    assert context_id.startswith("context-")

    pattern = re.compile(
        (
            r"^context-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(context_id) is not None