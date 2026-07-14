from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    DEFAULT_RETRY_COUNT,
    DEFAULT_TIMEOUT,
    DEFAULT_USER_AGENT,
    DEFAULT_VERIFY_SSL,
)


@dataclass(slots=True)
class ToolConfig:
    """Configuration for tool implementations."""

    timeout: int = DEFAULT_TIMEOUT
    retry_count: int = DEFAULT_RETRY_COUNT
    user_agent: str = DEFAULT_USER_AGENT
    verify_ssl: bool = DEFAULT_VERIFY_SSL

    def validate(self) -> None:
        """Validate configuration."""

        if self.timeout <= 0:
            raise ValueError("timeout must be greater than zero.")

        if self.retry_count < 0:
            raise ValueError("retry_count cannot be negative.")

        if not self.user_agent:
            raise ValueError("user_agent cannot be empty.")
