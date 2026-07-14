"""Exceptions for workflow steps."""

from ai_workflows.base.exceptions import WorkflowExecutionError


class StepExecutionError(WorkflowExecutionError):
    """Raised when a workflow step fails."""
