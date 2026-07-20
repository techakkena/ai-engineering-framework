from __future__ import annotations

import pytest

from ai_workflows.base.exceptions import (
    WorkflowConfigurationError,
    WorkflowError,
    WorkflowExecutionError,
    WorkflowValidationError,
)


def test_workflow_error() -> None:
    with pytest.raises(WorkflowError):
        raise WorkflowError()


def test_configuration_error() -> None:
    with pytest.raises(WorkflowConfigurationError):
        raise WorkflowConfigurationError()


def test_execution_error() -> None:
    with pytest.raises(WorkflowExecutionError):
        raise WorkflowExecutionError()


def test_validation_error() -> None:
    with pytest.raises(WorkflowValidationError):
        raise WorkflowValidationError()
