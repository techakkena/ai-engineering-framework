from ai_workflows.utils.constants import (
    DEFAULT_WORKFLOW_PREFIX,
)


def test_default_prefix() -> None:
    assert DEFAULT_WORKFLOW_PREFIX == "workflow"
