"""Evaluation utility exceptions."""

from ai_evals.base.exceptions import (
    EvaluationError,
)


class UtilityError(EvaluationError):
    """Raised when an evaluation utility operation fails."""
