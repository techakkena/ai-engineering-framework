from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    DEFAULT_AGENT_TIMEOUT,
    DEFAULT_MAX_ITERATIONS,
)


@dataclass(slots=True)
class AgentConfig:
    """Configuration for an AI agent."""

    timeout: int = DEFAULT_AGENT_TIMEOUT
    max_iterations: int = DEFAULT_MAX_ITERATIONS

    def validate(self) -> None:
        """Validate configuration."""

        if self.timeout <= 0:
            raise ValueError("timeout must be greater than zero.")

        if self.max_iterations <= 0:
            raise ValueError("max_iterations must be greater than zero.")
