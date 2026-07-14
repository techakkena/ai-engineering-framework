"""Exceptions for workflow conditions."""

from ai_workflows.base.exceptions import WorkflowExecutionError


class ConditionEvaluationError(
    WorkflowExecutionError,
):
    """Raised when condition evaluation fails."""
