"""Utility operations for ai_evals."""

from __future__ import annotations

from .constants import DEFAULT_EVALUATION_PREFIX


def build_evaluation_name(
    name: str,
) -> str:
    """Build a standardized evaluation name."""

    cleaned = name.strip().lower().replace(" ", "_")

    return f"{DEFAULT_EVALUATION_PREFIX}_{cleaned}"


def validate_evaluation_name(
    name: str,
) -> bool:
    """Validate an evaluation name."""

    if not name:
        return False

    return name.replace("_", "").isalnum()
