"""Event constants."""

from enum import Enum


class EventType(str, Enum):
    """Supported event types."""

    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
