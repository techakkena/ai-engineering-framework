from __future__ import annotations

"""Planning exceptions."""

from ai_agents.base.exceptions import AgentError


class PlanningError(AgentError):
    """Raised when planning fails."""
