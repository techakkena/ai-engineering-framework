from __future__ import annotations

from ai_workflows.workflow.constants import (
    DEFAULT_WORKFLOW_DESCRIPTION,
    DEFAULT_WORKFLOW_NAME,
)


def test_default_workflow_name() -> None:
    assert DEFAULT_WORKFLOW_NAME == "workflow"


def test_default_workflow_description() -> None:
    assert "Default" in DEFAULT_WORKFLOW_DESCRIPTION
