"""
Operations for ai_runtime.runtime.
"""

from __future__ import annotations

import uuid

from ai_runtime.runtime.constants import (
    SUPPORTED_RUNTIME_MODES,
    SUPPORTED_RUNTIME_STATES,
)
from ai_runtime.runtime.exceptions import (
    InvalidRuntimeModeError,
    RuntimeStateError,
)


def normalize_runtime_mode(
    mode: str,
) -> str:
    """
    Normalize a runtime mode.
    """
    return mode.strip().lower()


def validate_runtime_mode(
    mode: str,
) -> str:
    """
    Validate a runtime mode.
    """
    normalized = normalize_runtime_mode(mode)

    if normalized not in SUPPORTED_RUNTIME_MODES:
        raise InvalidRuntimeModeError(mode)

    return normalized


def validate_runtime_state(
    state: str,
) -> str:
    """
    Validate a runtime state.
    """
    normalized = state.strip().lower()

    if normalized not in SUPPORTED_RUNTIME_STATES:
        raise RuntimeStateError(state)

    return normalized


def is_supported_runtime_mode(
    mode: str,
) -> bool:
    """
    Determine whether a runtime mode is supported.
    """
    return (
        normalize_runtime_mode(mode)
        in SUPPORTED_RUNTIME_MODES
    )


def build_runtime_id() -> str:
    """
    Build a unique runtime identifier.

    Returns:
        Runtime identifier.
    """
    return f"runtime-{uuid.uuid4()}"