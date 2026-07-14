import pytest

from ai_workflows.steps.exceptions import StepExecutionError


def test_step_execution_error() -> None:
    with pytest.raises(StepExecutionError):
        raise StepExecutionError()
