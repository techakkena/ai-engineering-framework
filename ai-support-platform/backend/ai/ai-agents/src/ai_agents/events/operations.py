from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass(slots=True, frozen=True)
class Event:
    """Represents an event."""

    event_type: str
    payload: dict[str, Any] = field(default_factory=dict)


class EventDispatcher:
    """Simple in-memory event dispatcher."""

    def __init__(self) -> None:
        self._handlers: dict[
            str,
            list[Callable[[Event], None]],
        ] = {}

    def subscribe(
        self,
        event_type: str,
        handler: Callable[[Event], None],
    ) -> None:
        """Register an event handler."""
        self._handlers.setdefault(
            event_type,
            [],
        ).append(handler)

    def publish(
        self,
        event: Event,
    ) -> None:
        """Publish an event."""
        for handler in self._handlers.get(
            event.event_type,
            [],
        ):
            handler(event)

    def handler_count(
        self,
        event_type: str,
    ) -> int:
        """Return number of handlers."""
        return len(
            self._handlers.get(
                event_type,
                [],
            )
        )

    def clear(self) -> None:
        """Remove all handlers."""
        self._handlers.clear()
