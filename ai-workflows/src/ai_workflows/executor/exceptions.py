"""Workflow executor exceptions."""

from ai_workflows.base.exceptions import WorkflowExecutionError


class WorkflowExecutorError(WorkflowExecutionError):
    """Raised when workflow execution fails."""
