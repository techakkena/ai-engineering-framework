import pytest

from ai_workflows.base.operations import (
    WorkflowInput,
    WorkflowOutput,
)
from ai_workflows.pipeline.operations import Pipeline
from ai_workflows.steps.operations import Step


@pytest.mark.asyncio
async def test_empty_pipeline() -> None:
    pipeline = Pipeline()

    result = await pipeline.run(
        WorkflowInput(
            data={"value": 1},
        )
    )

    assert result.result == {"value": 1}


def test_add_step() -> None:
    pipeline = Pipeline()

    pipeline.add_step(
        Step(),
    )

    assert pipeline.size == 1


def test_pipeline_name() -> None:
    pipeline = Pipeline(
        name="customer_pipeline",
    )

    assert pipeline.name == "customer_pipeline"


@pytest.mark.asyncio
async def test_pipeline_run() -> None:
    pipeline = Pipeline()

    pipeline.add_step(
        Step(),
    )

    pipeline.add_step(
        Step(),
    )

    result = await pipeline.run(
        WorkflowInput(
            data={"message": "hello"},
        )
    )

    assert isinstance(
        result,
        WorkflowOutput,
    )

    assert result.result == {
        "message": "hello",
    }
