from __future__ import annotations

from dataclasses import dataclass, field

from .constants import DEFAULT_EXPERIMENT_NAME


@dataclass(slots=True)
class Experiment:
    """Represents an evaluation experiment."""

    name: str = DEFAULT_EXPERIMENT_NAME

    scores: dict[str, float] = field(
        default_factory=dict,
    )

    def record_score(
        self,
        metric: str,
        score: float,
    ) -> None:
        """Record a score."""
        self.scores[metric] = score

    @property
    def average_score(self) -> float:
        """Return average score."""
        if not self.scores:
            return 0.0

        return round(
            sum(self.scores.values()) / len(self.scores),
            6,
        )


class ExperimentRegistry:
    """Registry of experiments."""

    def __init__(self) -> None:
        self._experiments: dict[
            str,
            Experiment,
        ] = {}

    def register(
        self,
        experiment: Experiment,
    ) -> None:
        """Register an experiment."""
        self._experiments[experiment.name] = experiment

    def get(
        self,
        name: str,
    ) -> Experiment | None:
        """Return an experiment."""
        return self._experiments.get(name)

    @property
    def count(self) -> int:
        """Return number of experiments."""
        return len(self._experiments)
