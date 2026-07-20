from __future__ import annotations

import pytest

from ai_agents.config.operations import AgentConfig


def test_default_config() -> None:
    config = AgentConfig()

    assert config.timeout == 60
    assert config.max_iterations == 10


def test_validate_success() -> None:
    config = AgentConfig()

    config.validate()


def test_invalid_timeout() -> None:
    config = AgentConfig(timeout=0)

    with pytest.raises(ValueError):
        config.validate()


def test_invalid_iterations() -> None:
    config = AgentConfig(max_iterations=0)

    with pytest.raises(ValueError):
        config.validate()
