from __future__ import annotations

from ai_agents.conversations.constants import (
    DEFAULT_CONVERSATION_ID,
)


def test_default_conversation_id() -> None:
    assert DEFAULT_CONVERSATION_ID == "default"
