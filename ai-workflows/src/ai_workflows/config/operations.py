from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    DEFAULT_FAIL_FAST,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
)


@dataclass(slots=True)
class WorkflowConfig:
    """Workflow configuration."""

    timeout: int = DEFAULT_TIMEOUT
    max_retries: int = DEFAULT_MAX_RETRIES
    fail_fast: bool = DEFAULT_FAIL_FAST

    def validate(self) -> None:
        """Validate configuration."""

        if self.timeout <= 0:
            raise ValueError("timeout must be greater than zero.")

        if self.max_retries < 0:
            raise ValueError("max_retries cannot be negative.")
