"""
Operations for ai_runtime.session.
"""

from __future__ import annotations

import re
import uuid

from ai_runtime.session.constants import (
    SUPPORTED_SESSION_STATES,
)
from ai_runtime.session.exceptions import (
    InvalidSessionStateError,
)


def normalize_session_state(
    state: str,
) -> str:
    """
    Normalize a session state.
    """
    return state.strip().lower()


def validate_session_state(
    state: str,
) -> str:
    """
    Validate a session state.
    """
    normalized = normalize_session_state(state)

    if normalized not in SUPPORTED_SESSION_STATES:
        raise InvalidSessionStateError(state)

    return normalized


def is_supported_session_state(
    state: str,
) -> bool:
    """
    Determine whether a session state is supported.
    """
    return (
        normalize_session_state(state)
        in SUPPORTED_SESSION_STATES
    )


def validate_session_id(
    session_id: str,
) -> str:
    """
    Validate a session identifier.
    """
    normalized = session_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid session identifier: '{session_id}'."
        )

    return normalized


def build_session_id() -> str:
    """
    Build a unique session identifier.

    Returns:
        Session identifier.
    """
    return f"session-{uuid.uuid4()}"