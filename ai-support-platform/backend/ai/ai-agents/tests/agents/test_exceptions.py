from __future__ import annotations

import pytest

from ai_agents.agents.exceptions import (
    AgentRegistrationError,
)


def test_registration_error() -> None:
    with pytest.raises(AgentRegistrationError):
        raise AgentRegistrationError()
