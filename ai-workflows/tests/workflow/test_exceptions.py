import pytest

from ai_workflows.workflow.exceptions import (
    WorkflowRegistrationError,
)


def test_workflow_registration_error() -> None:
    with pytest.raises(WorkflowRegistrationError):
        raise WorkflowRegistrationError()
