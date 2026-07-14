from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CalendarEvent:
    """Represents a calendar event."""

    event_id: str
    title: str
    start_time: str
    end_time: str


class CalendarClient:
    """Simple in-memory calendar client."""

    def __init__(self) -> None:
        self._events: dict[str, CalendarEvent] = {}

    def add_event(
        self,
        event: CalendarEvent,
    ) -> None:
        """Add an event."""
        self._events[event.event_id] = event

    def get_event(
        self,
        event_id: str,
    ) -> CalendarEvent | None:
        """Retrieve an event."""
        return self._events.get(event_id)

    def list_events(
        self,
    ) -> tuple[CalendarEvent, ...]:
        """Return all events."""
        return tuple(self._events.values())

    @property
    def event_count(self) -> int:
        """Return number of events."""
        return len(self._events)
