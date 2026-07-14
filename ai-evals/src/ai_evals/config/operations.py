from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    DEFAULT_ENABLED,
    DEFAULT_METRIC,
    DEFAULT_PASS_THRESHOLD,
    DEFAULT_SAVE_REPORTS,
)


@dataclass(slots=True)
class EvaluationConfig:
    """Configuration for evaluation."""

    enabled: bool = DEFAULT_ENABLED

    default_metric: str = DEFAULT_METRIC

    pass_threshold: float = DEFAULT_PASS_THRESHOLD

    save_reports: bool = DEFAULT_SAVE_REPORTS

    def validate(self) -> None:
        """Validate configuration."""

        if not self.default_metric:
            raise ValueError("default_metric cannot be empty.")

        if not (0.0 <= self.pass_threshold <= 1.0):
            raise ValueError("pass_threshold must be between 0 and 1.")
