"""Exceptions for evaluation."""


class EvaluationError(Exception):
    """Base evaluation exception."""


class EvaluationConfigurationError(
    EvaluationError,
):
    """Raised for invalid evaluator configuration."""
