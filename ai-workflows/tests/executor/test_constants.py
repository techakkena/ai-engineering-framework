from ai_workflows.executor.constants import (
    DEFAULT_EXECUTOR_NAME,
)


def test_default_executor_name() -> None:
    assert DEFAULT_EXECUTOR_NAME == "executor"
