"""
Operations for ai_runtime.executor.
"""

from __future__ import annotations

import re
import uuid

from ai_runtime.executor.constants import (
    SUPPORTED_EXECUTOR_MODES,
)
from ai_runtime.executor.exceptions import (
    InvalidExecutorModeError,
)


def normalize_executor_mode(
    mode: str,
) -> str:
    """
    Normalize an executor mode.
    """
    return mode.strip().lower()


def validate_executor_mode(
    mode: str,
) -> str:
    """
    Validate an executor mode.
    """
    normalized = normalize_executor_mode(mode)

    if normalized not in SUPPORTED_EXECUTOR_MODES:
        raise InvalidExecutorModeError(mode)

    return normalized


def is_supported_executor_mode(
    mode: str,
) -> bool:
    """
    Determine whether an executor mode is supported.
    """
    return (
        normalize_executor_mode(mode)
        in SUPPORTED_EXECUTOR_MODES
    )


def validate_executor_id(
    executor_id: str,
) -> str:
    """
    Validate an executor identifier.
    """
    normalized = executor_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid executor identifier: '{executor_id}'."
        )

    return normalized


def build_executor_id() -> str:
    """
    Build a unique executor identifier.

    Returns:
        Executor identifier.
    """
    return f"executor-{uuid.uuid4()}"