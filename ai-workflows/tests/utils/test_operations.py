from ai_workflows.utils.operations import (
    build_workflow_name,
    validate_workflow_name,
)


def test_build_name() -> None:
    assert build_workflow_name("Customer") == "workflow_customer"


def test_build_name_spaces() -> None:
    assert build_workflow_name("Customer Workflow") == "workflow_customer_workflow"


def test_validate_name() -> None:
    assert validate_workflow_name("workflow_demo")


def test_validate_empty_name() -> None:
    assert not validate_workflow_name("")


def test_validate_invalid_name() -> None:
    assert not validate_workflow_name("workflow-demo")
