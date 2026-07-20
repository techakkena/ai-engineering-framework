from __future__ import annotations

import pytest

from ai_workflows.base.operations import (
    WorkflowInput,
    WorkflowOutput,
)
from ai_workflows.steps.operations import (
    Step,
)


def test_default_step() -> None:
    step = Step()

    assert step.name == "step"
    assert "Default" in step.description


def test_custom_step() -> None:
    step = Step(
        name="validate",
        description="Validate input",
    )

    assert step.name == "validate"
    assert step.description == "Validate input"


@pytest.mark.asyncio
async def test_execute() -> None:
    step = Step()

    result = await step.execute(
        WorkflowInput(
            data={
                "value": 100,
            }
        )
    )

    assert isinstance(
        result,
        WorkflowOutput,
    )

    assert result.result == {
        "value": 100,
    }
