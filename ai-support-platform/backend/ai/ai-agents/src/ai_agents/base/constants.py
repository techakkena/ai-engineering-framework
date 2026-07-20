from __future__ import annotations

from enum import Enum


class AgentStatus(str, Enum):
    """Execution status of an agent."""

    IDLE = "idle"
    RUNNING = "running"
    WAITING = "waiting"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
