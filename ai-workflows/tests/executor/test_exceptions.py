import pytest

from ai_workflows.executor.exceptions import (
    WorkflowExecutorError,
)


def test_executor_error() -> None:
    with pytest.raises(
        WorkflowExecutorError,
    ):
        raise WorkflowExecutorError()
