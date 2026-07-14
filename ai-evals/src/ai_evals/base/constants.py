"""Constants for evaluation."""

from enum import Enum


class EvaluationStatus(str, Enum):
    """Evaluation lifecycle."""

    PENDING = "pending"
    RUNNING = "running"
    PASSED = "passed"
    FAILED = "failed"
