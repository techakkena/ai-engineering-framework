from __future__ import annotations

from ai_workflows.base.operations import (
    WorkflowInput,
    WorkflowOutput,
)
from ai_workflows.steps.operations import BaseStep

from .constants import DEFAULT_PIPELINE_NAME


class Pipeline:
    """Sequential workflow pipeline."""

    def __init__(
        self,
        name: str = DEFAULT_PIPELINE_NAME,
    ) -> None:
        self._name = name
        self._steps: list[BaseStep] = []

    @property
    def name(self) -> str:
        """Return pipeline name."""
        return self._name

    @property
    def steps(self) -> tuple[BaseStep, ...]:
        """Return registered steps."""
        return tuple(self._steps)

    def add_step(
        self,
        step: BaseStep,
    ) -> None:
        """Add a step."""
        self._steps.append(step)

    @property
    def size(self) -> int:
        """Return number of steps."""
        return len(self._steps)

    async def run(
        self,
        workflow_input: WorkflowInput,
    ) -> WorkflowOutput:
        """Execute all steps sequentially."""

        current = workflow_input

        result = WorkflowOutput(
            result=current.data,
        )

        for step in self._steps:
            result = await step.execute(current)
            current = WorkflowInput(
                data=result.result,
            )

        return result
