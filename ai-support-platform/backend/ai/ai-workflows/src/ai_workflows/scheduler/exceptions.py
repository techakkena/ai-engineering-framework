from __future__ import annotations

"""Scheduler exceptions."""

from ai_workflows.base.exceptions import WorkflowError


class SchedulerError(WorkflowError):
    """Raised for scheduler errors."""
