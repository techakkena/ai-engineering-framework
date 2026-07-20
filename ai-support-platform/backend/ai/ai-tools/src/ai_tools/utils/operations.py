from __future__ import annotations

"""Utility operations for ai_tools."""

from __future__ import annotations

from .constants import DEFAULT_TOOL_PREFIX


def build_tool_name(name: str) -> str:
    """Build a standardized tool name."""

    cleaned = name.strip().lower().replace(" ", "_")

    return f"{DEFAULT_TOOL_PREFIX}_{cleaned}"


def validate_tool_name(
    name: str,
) -> bool:
    """Validate a tool name."""

    if not name:
        return False

    return name.replace("_", "").isalnum()
