from __future__ import annotations

"""Constants for the base workflow module."""

from enum import Enum


class WorkflowStatus(str, Enum):
    """Workflow execution status."""

    IDLE = "idle"
    RUNNING = "running"
    WAITING = "waiting"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
