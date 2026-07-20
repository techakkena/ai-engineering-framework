from __future__ import annotations

"""Utility operations for ai_agents."""

from __future__ import annotations

from .constants import DEFAULT_AGENT_PREFIX


def build_agent_name(name: str) -> str:
    """Build a standardized agent name."""

    cleaned = name.strip().lower().replace(" ", "_")
    return f"{DEFAULT_AGENT_PREFIX}_{cleaned}"


def validate_agent_name(name: str) -> bool:
    """Validate an agent name."""

    if not name:
        return False

    return name.replace("_", "").isalnum()
