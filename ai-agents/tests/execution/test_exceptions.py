import pytest

from ai_agents.execution.exceptions import ExecutionError


def test_execution_error() -> None:
    with pytest.raises(ExecutionError):
        raise ExecutionError()
