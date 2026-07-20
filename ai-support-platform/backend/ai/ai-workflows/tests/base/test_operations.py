from __future__ import annotations

from ai_workflows.base.operations import (
    BaseWorkflow,
    WorkflowContext,
    WorkflowInput,
    WorkflowOutput,
)


class DummyWorkflow(BaseWorkflow):
    @property
    def name(self) -> str:
        return "dummy"

    @property
    def description(self) -> str:
        return "Dummy workflow"

    async def run(
        self,
        workflow_input: WorkflowInput,
    ) -> WorkflowOutput:
        return WorkflowOutput(result="ok")


def test_workflow_input() -> None:
    workflow_input = WorkflowInput()

    assert workflow_input.data == {}
    assert workflow_input.metadata == {}


def test_workflow_output() -> None:
    workflow_output = WorkflowOutput(result="done")

    assert workflow_output.result == "done"
    assert workflow_output.metadata == {}


def test_workflow_context() -> None:
    context = WorkflowContext()

    assert context.workflow_id is None
    assert context.variables == {}


def test_dummy_workflow() -> None:
    workflow = DummyWorkflow()

    assert workflow.name == "dummy"
    assert workflow.description == "Dummy workflow"
