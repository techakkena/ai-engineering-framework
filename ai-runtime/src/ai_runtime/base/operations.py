"""
Operations for the ai_runtime.base module.
"""

from __future__ import annotations

import re

from ai_runtime.base.constants import (
    SUPPORTED_RUNTIME_STATUSES,
)
from ai_runtime.base.exceptions import (
    InvalidRuntimeError,
)


def normalize_runtime_name(
    runtime_name: str,
) -> str:
    """
    Normalize a runtime name.
    """
    return runtime_name.strip().lower()


def validate_runtime_name(
    runtime_name: str,
) -> str:
    """
    Validate a runtime name.
    """
    normalized = normalize_runtime_name(runtime_name)

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise InvalidRuntimeError(runtime_name)

    return normalized


def validate_runtime_status(
    status: str,
) -> str:
    """
    Validate a runtime status.
    """
    normalized = status.strip().lower()

    if normalized not in SUPPORTED_RUNTIME_STATUSES:
        raise InvalidRuntimeError(status)

    return normalized


def is_supported_runtime_status(
    status: str,
) -> bool:
    """
    Determine whether a runtime status is supported.
    """
    return (
        status.strip().lower()
        in SUPPORTED_RUNTIME_STATUSES
    )


def build_runtime_name(
    name: str,
) -> str:
    """
    Build a normalized runtime name.
    """
    return (
        name.strip()
        .lower()
        .replace(" ", "-")
    )