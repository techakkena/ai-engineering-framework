from __future__ import annotations

"""Workflow exceptions."""

from ai_workflows.base.exceptions import WorkflowError


class WorkflowRegistrationError(WorkflowError):
    """Raised when a workflow cannot be registered."""
