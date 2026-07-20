from __future__ import annotations

import pytest

from ai_workflows.base.operations import (
    WorkflowInput,
    WorkflowOutput,
)
from ai_workflows.workflow.operations import Workflow


def test_default_constructor() -> None:
    workflow = Workflow()

    assert workflow.name == "workflow"
    assert "Default" in workflow.description


def test_custom_constructor() -> None:
    workflow = Workflow(
        name="customer_support",
        description="Customer Support Workflow",
    )

    assert workflow.name == "customer_support"
    assert workflow.description == "Customer Support Workflow"


@pytest.mark.asyncio
async def test_run() -> None:
    workflow = Workflow()

    output = await workflow.run(
        WorkflowInput(
            data={
                "message": "hello",
            }
        )
    )

    assert isinstance(output, WorkflowOutput)
    assert output.result == {
        "message": "hello",
    }
