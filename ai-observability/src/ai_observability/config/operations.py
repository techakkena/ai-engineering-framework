from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    DEFAULT_ENABLED,
    DEFAULT_EXPORT_INTERVAL,
    DEFAULT_LOG_LEVEL,
    DEFAULT_SAMPLING_RATE,
)


@dataclass(slots=True)
class ObservabilityConfig:
    """Configuration for observability."""

    enabled: bool = DEFAULT_ENABLED

    export_interval: int = DEFAULT_EXPORT_INTERVAL

    log_level: str = DEFAULT_LOG_LEVEL

    sampling_rate: float = DEFAULT_SAMPLING_RATE

    def validate(self) -> None:
        """Validate configuration."""

        if self.export_interval <= 0:
            raise ValueError("export_interval must be greater than zero.")

        if not (0.0 <= self.sampling_rate <= 1.0):
            raise ValueError("sampling_rate must be between 0 and 1.")

        if not self.log_level:
            raise ValueError("log_level cannot be empty.")
