"""Workflow utility exceptions."""

from ai_workflows.base.exceptions import WorkflowError


class UtilityError(WorkflowError):
    """Raised when a workflow utility operation fails."""
