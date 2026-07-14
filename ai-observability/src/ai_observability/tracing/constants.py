"""Tracing constants."""

from enum import Enum


class SpanStatus(str, Enum):
    """Span status."""

    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
