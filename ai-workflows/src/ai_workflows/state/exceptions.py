"""Workflow state exceptions."""

from ai_workflows.base.exceptions import WorkflowError


class StateError(WorkflowError):
    """Raised when workflow state operations fail."""
