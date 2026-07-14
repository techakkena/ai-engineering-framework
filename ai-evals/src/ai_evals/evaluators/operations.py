from __future__ import annotations

from dataclasses import dataclass

from ai_evals.base.constants import (
    EvaluationStatus,
)
from ai_evals.base.operations import (
    BaseEvaluator,
    EvaluationContext,
    EvaluationResult,
)

from .constants import DEFAULT_EVALUATOR_NAME


@dataclass(slots=True)
class Evaluator(BaseEvaluator):
    """Simple evaluator."""

    name: str = DEFAULT_EVALUATOR_NAME

    score: float = 1.0

    def evaluate(
        self,
        context: EvaluationContext,
    ) -> EvaluationResult:
        """Evaluate a context."""

        return EvaluationResult(
            score=self.score,
            status=EvaluationStatus.PASSED,
        )


class EvaluatorRegistry:
    """Registry of evaluators."""

    def __init__(self) -> None:
        self._evaluators: dict[
            str,
            Evaluator,
        ] = {}

    def register(
        self,
        evaluator: Evaluator,
    ) -> None:
        self._evaluators[evaluator.name] = evaluator

    def get(
        self,
        name: str,
    ) -> Evaluator | None:
        return self._evaluators.get(name)

    @property
    def count(self) -> int:
        return len(self._evaluators)
