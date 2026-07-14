from __future__ import annotations

from ai_workflows.base.operations import (
    BaseWorkflow,
    WorkflowInput,
    WorkflowOutput,
)

from .exceptions import WorkflowExecutorError


class WorkflowExecutor:
    """Executes workflows."""

    async def execute(
        self,
        workflow: BaseWorkflow,
        workflow_input: WorkflowInput,
    ) -> WorkflowOutput:
        """Execute a workflow."""

        try:
            await workflow.initialize()
            await workflow.before_run(
                workflow_input,
            )

            result = await workflow.run(
                workflow_input,
            )

            await workflow.after_run(
                result,
            )

            await workflow.shutdown()

            return result

        except Exception as exc:
            raise WorkflowExecutorError(
                str(exc),
            ) from exc
