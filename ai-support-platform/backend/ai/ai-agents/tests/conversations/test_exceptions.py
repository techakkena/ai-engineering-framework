from __future__ import annotations

import pytest

from ai_agents.conversations.exceptions import (
    ConversationError,
)


def test_conversation_error() -> None:
    with pytest.raises(ConversationError):
        raise ConversationError()
