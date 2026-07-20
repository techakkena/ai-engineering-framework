from __future__ import annotations

import pytest

from ai_workflows.base.operations import (
    WorkflowInput,
    WorkflowOutput,
)
from ai_workflows.executor.exceptions import (
    WorkflowExecutorError,
)
from ai_workflows.executor.operations import (
    WorkflowExecutor,
)
from ai_workflows.workflow.operations import (
    Workflow,
)


@pytest.mark.asyncio
async def test_execute_success() -> None:
    executor = WorkflowExecutor()

    workflow = Workflow()

    result = await executor.execute(
        workflow,
        WorkflowInput(
            data={
                "value": 123,
            },
        ),
    )

    assert isinstance(
        result,
        WorkflowOutput,
    )

    assert result.result == {
        "value": 123,
    }


class BrokenWorkflow(Workflow):
    async def run(
        self,
        workflow_input: WorkflowInput,
    ) -> WorkflowOutput:
        raise RuntimeError("failure")


@pytest.mark.asyncio
async def test_execute_failure() -> None:
    executor = WorkflowExecutor()

    with pytest.raises(
        WorkflowExecutorError,
    ):
        await executor.execute(
            BrokenWorkflow(),
            WorkflowInput(),
        )
