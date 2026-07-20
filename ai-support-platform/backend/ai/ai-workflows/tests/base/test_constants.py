from __future__ import annotations

from ai_workflows.base.constants import WorkflowStatus


def test_workflow_status_values() -> None:
    assert WorkflowStatus.IDLE.value == "idle"
    assert WorkflowStatus.RUNNING.value == "running"
    assert WorkflowStatus.WAITING.value == "waiting"
    assert WorkflowStatus.COMPLETED.value == "completed"
    assert WorkflowStatus.FAILED.value == "failed"
    assert WorkflowStatus.CANCELLED.value == "cancelled"


def test_workflow_status_count() -> None:
    assert len(WorkflowStatus) == 6
