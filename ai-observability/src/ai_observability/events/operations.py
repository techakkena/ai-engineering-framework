from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .constants import EventType


@dataclass(slots=True)
class Event:
    """Represents an event."""

    name: str

    event_type: EventType

    payload: dict[str, Any] = field(
        default_factory=dict,
    )


class EventBus:
    """Simple in-memory event bus."""

    def __init__(self) -> None:
        self._handlers: list[Callable[[Event], None]] = []

    def subscribe(
        self,
        handler: Callable[[Event], None],
    ) -> None:
        """Subscribe a handler."""
        self._handlers.append(handler)

    def publish(
        self,
        event: Event,
    ) -> None:
        """Publish an event."""
        for handler in self._handlers:
            handler(event)

    @property
    def subscriber_count(self) -> int:
        return len(self._handlers)
