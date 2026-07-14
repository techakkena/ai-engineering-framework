"""Workflow exceptions."""


class WorkflowError(Exception):
    """Base workflow exception."""


class WorkflowConfigurationError(WorkflowError):
    """Raised when workflow configuration is invalid."""


class WorkflowExecutionError(WorkflowError):
    """Raised when workflow execution fails."""


class WorkflowValidationError(WorkflowError):
    """Raised when workflow validation fails."""
