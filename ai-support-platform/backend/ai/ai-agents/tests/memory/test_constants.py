from __future__ import annotations

from ai_agents.memory.constants import DEFAULT_MEMORY_KEY


def test_default_memory_key() -> None:
    assert DEFAULT_MEMORY_KEY == "default"
