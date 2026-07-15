"""
Operations for ai_runtime.lifecycle.
"""

from __future__ import annotations

import re
import uuid

from ai_runtime.lifecycle.constants import (
    SUPPORTED_LIFECYCLE_PHASES,
)
from ai_runtime.lifecycle.exceptions import (
    InvalidLifecyclePhaseError,
)


def normalize_lifecycle_phase(
    phase: str,
) -> str:
    """
    Normalize a lifecycle phase.
    """
    return phase.strip().lower()


def validate_lifecycle_phase(
    phase: str,
) -> str:
    """
    Validate a lifecycle phase.
    """
    normalized = normalize_lifecycle_phase(phase)

    if normalized not in SUPPORTED_LIFECYCLE_PHASES:
        raise InvalidLifecyclePhaseError(phase)

    return normalized


def is_supported_lifecycle_phase(
    phase: str,
) -> bool:
    """
    Determine whether a lifecycle phase is supported.
    """
    return (
        normalize_lifecycle_phase(phase)
        in SUPPORTED_LIFECYCLE_PHASES
    )


def validate_lifecycle_id(
    lifecycle_id: str,
) -> str:
    """
    Validate a lifecycle identifier.
    """
    normalized = lifecycle_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid lifecycle identifier: '{lifecycle_id}'."
        )

    return normalized


def build_lifecycle_id() -> str:
    """
    Build a unique lifecycle identifier.

    Returns:
        Lifecycle identifier.
    """
    return f"lifecycle-{uuid.uuid4()}"