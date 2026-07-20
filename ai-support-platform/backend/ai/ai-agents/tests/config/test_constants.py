from __future__ import annotations

from ai_agents.config.constants import (
    DEFAULT_AGENT_TIMEOUT,
    DEFAULT_MAX_ITERATIONS,
)


def test_default_timeout() -> None:
    assert DEFAULT_AGENT_TIMEOUT == 60


def test_default_iterations() -> None:
    assert DEFAULT_MAX_ITERATIONS == 10
