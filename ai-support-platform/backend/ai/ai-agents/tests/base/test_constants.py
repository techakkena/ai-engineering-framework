from __future__ import annotations

from ai_agents.base.constants import AgentStatus


def test_agent_status_values() -> None:
    assert AgentStatus.IDLE.value == "idle"
    assert AgentStatus.RUNNING.value == "running"
    assert AgentStatus.WAITING.value == "waiting"
    assert AgentStatus.COMPLETED.value == "completed"
    assert AgentStatus.FAILED.value == "failed"
    assert AgentStatus.CANCELLED.value == "cancelled"


def test_agent_status_count() -> None:
    assert len(AgentStatus) == 6
