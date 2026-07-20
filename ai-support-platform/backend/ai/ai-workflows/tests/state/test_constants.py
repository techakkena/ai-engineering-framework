from __future__ import annotations

from ai_workflows.state.constants import DEFAULT_STATE_NAME


def test_default_state_name() -> None:
    assert DEFAULT_STATE_NAME == "default"
