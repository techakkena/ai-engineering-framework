"""Constants for ai_observability."""

from enum import Enum


class ObservationStatus(str, Enum):
    """Observation lifecycle status."""

    CREATED = "created"
    STARTED = "started"
    COMPLETED = "completed"
    FAILED = "failed"
