from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from .constants import EvaluationStatus


@dataclass(slots=True)
class EvaluationResult:
    """Evaluation result."""

    score: float = 0.0

    status: EvaluationStatus = EvaluationStatus.PENDING

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )


@dataclass(slots=True)
class EvaluationContext:
    """Evaluation context."""

    inputs: dict[str, Any] = field(
        default_factory=dict,
    )

    outputs: dict[str, Any] = field(
        default_factory=dict,
    )


class BaseEvaluator(ABC):
    """Base evaluator."""

    @abstractmethod
    def evaluate(
        self,
        context: EvaluationContext,
    ) -> EvaluationResult:
        """Run evaluation."""
