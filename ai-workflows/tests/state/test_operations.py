import pytest

from ai_workflows.state.operations import (
    WorkflowState,
    WorkflowStateStore,
)


def test_create_state() -> None:
    state = WorkflowState(
        name="workflow",
    )

    assert state.name == "workflow"
    assert state.data == {}


def test_store_state() -> None:
    store = WorkflowStateStore()

    store.set(
        WorkflowState(
            name="workflow",
        )
    )

    assert store.size == 1


def test_get_state() -> None:
    store = WorkflowStateStore()

    state = WorkflowState(
        name="workflow",
    )

    store.set(state)

    assert store.get("workflow") is state


def test_exists() -> None:
    store = WorkflowStateStore()

    store.set(
        WorkflowState(
            name="workflow",
        )
    )

    assert store.exists("workflow")
    assert not store.exists("missing")


def test_remove_state() -> None:
    store = WorkflowStateStore()

    store.set(
        WorkflowState(
            name="workflow",
        )
    )

    store.remove("workflow")

    assert store.size == 0


def test_clear_store() -> None:
    store = WorkflowStateStore()

    store.set(WorkflowState(name="a"))
    store.set(WorkflowState(name="b"))

    store.clear()

    assert store.size == 0


def test_missing_state() -> None:
    store = WorkflowStateStore()

    with pytest.raises(KeyError):
        store.get("missing")
