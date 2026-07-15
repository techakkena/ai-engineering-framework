"""
Operations for ai_runtime.state.
"""

from __future__ import annotations

import re
import uuid

from ai_runtime.state.constants import (
    SUPPORTED_STATE_STATUSES,
)
from ai_runtime.state.exceptions import (
    InvalidStateStatusError,
)


def normalize_state_status(
    status: str,
) -> str:
    """
    Normalize a state status.
    """
    return status.strip().lower()


def validate_state_status(
    status: str,
) -> str:
    """
    Validate a state status.
    """
    normalized = normalize_state_status(status)

    if normalized not in SUPPORTED_STATE_STATUSES:
        raise InvalidStateStatusError(status)

    return normalized


def is_supported_state_status(
    status: str,
) -> bool:
    """
    Determine whether a state status is supported.
    """
    return (
        normalize_state_status(status)
        in SUPPORTED_STATE_STATUSES
    )


def validate_state_id(
    state_id: str,
) -> str:
    """
    Validate a state identifier.
    """
    normalized = state_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid state identifier: '{state_id}'."
        )

    return normalized


def build_state_id() -> str:
    """
    Build a unique state identifier.

    Returns:
        State identifier.
    """
    return f"state-{uuid.uuid4()}"