from __future__ import annotations

from ai_workflows.base.operations import (
    BaseWorkflow,
    WorkflowInput,
    WorkflowOutput,
)

from .constants import (
    DEFAULT_WORKFLOW_DESCRIPTION,
    DEFAULT_WORKFLOW_NAME,
)


class Workflow(BaseWorkflow):
    """Default workflow implementation."""

    def __init__(
        self,
        name: str = DEFAULT_WORKFLOW_NAME,
        description: str = DEFAULT_WORKFLOW_DESCRIPTION,
    ) -> None:
        self._name = name
        self._description = description

    @property
    def name(self) -> str:
        """Return workflow name."""
        return self._name

    @property
    def description(self) -> str:
        """Return workflow description."""
        return self._description

    async def run(
        self,
        workflow_input: WorkflowInput,
    ) -> WorkflowOutput:
        """Execute workflow."""

        return WorkflowOutput(
            result=workflow_input.data,
        )
