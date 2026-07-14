"""Pipeline exceptions."""

from ai_workflows.base.exceptions import WorkflowExecutionError


class PipelineExecutionError(WorkflowExecutionError):
    """Raised when pipeline execution fails."""
