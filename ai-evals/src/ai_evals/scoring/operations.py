from __future__ import annotations

from dataclasses import dataclass

from .constants import DEFAULT_SCORE_NAME


@dataclass(slots=True)
class Score:
    """Represents an evaluation score."""

    name: str = DEFAULT_SCORE_NAME

    value: float = 0.0


class ScoreRegistry:
    """Registry of evaluation scores."""

    def __init__(self) -> None:
        self._scores: dict[str, Score] = {}

    def register(
        self,
        score: Score,
    ) -> None:
        """Register a score."""
        self._scores[score.name] = score

    def get(
        self,
        name: str,
    ) -> Score | None:
        """Return a score."""
        return self._scores.get(name)

    @property
    def count(self) -> int:
        """Return number of scores."""
        return len(self._scores)

    @property
    def average_score(self) -> float:
        """Return average score."""
        if not self._scores:
            return 0.0

        return round(
            sum(score.value for score in self._scores.values()) / len(self._scores),
            6,
        )
