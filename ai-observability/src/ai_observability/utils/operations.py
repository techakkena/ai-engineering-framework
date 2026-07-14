"""Utility operations for ai_observability."""

from __future__ import annotations

from .constants import DEFAULT_OBSERVATION_PREFIX


def build_observation_name(
    name: str,
) -> str:
    """Build a standardized observation name."""

    cleaned = name.strip().lower().replace(" ", "_")

    return f"{DEFAULT_OBSERVATION_PREFIX}_{cleaned}"


def validate_observation_name(
    name: str,
) -> bool:
    """Validate an observation name."""

    if not name:
        return False

    return name.replace("_", "").isalnum()
