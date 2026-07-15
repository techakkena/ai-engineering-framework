"""
Operations for ai_runtime.scheduler.
"""

from __future__ import annotations

import re
import uuid

from ai_runtime.scheduler.constants import (
    SUPPORTED_SCHEDULER_MODES,
)
from ai_runtime.scheduler.exceptions import (
    InvalidSchedulerModeError,
)


def normalize_scheduler_mode(
    mode: str,
) -> str:
    """
    Normalize a scheduler mode.
    """
    return mode.strip().lower()


def validate_scheduler_mode(
    mode: str,
) -> str:
    """
    Validate a scheduler mode.
    """
    normalized = normalize_scheduler_mode(mode)

    if normalized not in SUPPORTED_SCHEDULER_MODES:
        raise InvalidSchedulerModeError(mode)

    return normalized


def is_supported_scheduler_mode(
    mode: str,
) -> bool:
    """
    Determine whether a scheduler mode is supported.
    """
    return (
        normalize_scheduler_mode(mode)
        in SUPPORTED_SCHEDULER_MODES
    )


def validate_scheduler_id(
    scheduler_id: str,
) -> str:
    """
    Validate a scheduler identifier.
    """
    normalized = scheduler_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid scheduler identifier: '{scheduler_id}'."
        )

    return normalized


def build_scheduler_id() -> str:
    """
    Build a unique scheduler identifier.

    Returns:
        Scheduler identifier.
    """
    return f"scheduler-{uuid.uuid4()}"