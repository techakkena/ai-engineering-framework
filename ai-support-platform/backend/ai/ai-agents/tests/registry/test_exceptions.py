from __future__ import annotations

import pytest

from ai_agents.registry.exceptions import (
    AgentAlreadyRegisteredError,
    AgentNotFoundError,
)


def test_duplicate_registration_error() -> None:
    with pytest.raises(AgentAlreadyRegisteredError):
        raise AgentAlreadyRegisteredError()


def test_agent_not_found_error() -> None:
    with pytest.raises(AgentNotFoundError):
        raise AgentNotFoundError()
