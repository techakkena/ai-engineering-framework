"""Public exports for the events module."""

from .constants import DEFAULT_EVENT_TYPE
from .exceptions import EventError
from .operations import Event, EventDispatcher

__all__ = [
    "DEFAULT_EVENT_TYPE",
    "EventError",
    "Event",
    "EventDispatcher",
]
