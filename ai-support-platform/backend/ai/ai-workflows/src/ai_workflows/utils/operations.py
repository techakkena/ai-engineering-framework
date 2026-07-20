from __future__ import annotations

"""Workflow utility operations."""

from __future__ import annotations

from .constants import DEFAULT_WORKFLOW_PREFIX


def build_workflow_name(name: str) -> str:
    """Build a standardized workflow name."""

    cleaned = name.strip().lower().replace(" ", "_")

    return f"{DEFAULT_WORKFLOW_PREFIX}_{cleaned}"


def validate_workflow_name(name: str) -> bool:
    """Validate a workflow name."""

    if not name:
        return False

    return name.replace("_", "").isalnum()
