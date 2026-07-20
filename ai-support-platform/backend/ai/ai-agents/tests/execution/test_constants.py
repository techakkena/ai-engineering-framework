from __future__ import annotations

from ai_agents.execution.constants import DEFAULT_EXECUTION_NAME


def test_default_execution_name() -> None:
    assert DEFAULT_EXECUTION_NAME == "executor"
