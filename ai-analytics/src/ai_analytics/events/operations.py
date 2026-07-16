"""Operations for the ai_analytics.events module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_analytics.events.constants import (
    DEFAULT_ENABLED,
    DEFAULT_EVENT_TYPE,
    MAX_EVENT_NAME_LENGTH,
    MIN_EVENT_NAME_LENGTH,
    SUPPORTED_EVENT_TYPES,
)
from ai_analytics.events.exceptions import (
    DuplicateEventError,
    EventNotFoundError,
    EventValidationError,
    UnsupportedEventTypeError,
)


@dataclass(slots=True, frozen=True)
class EventDefinition:
    """Represents an analytics event."""

    name: str
    payload: dict[str, Any] = field(default_factory=dict)
    event_type: str = DEFAULT_EVENT_TYPE
    description: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the event definition."""
        normalized = self.name.strip()

        if not (
            MIN_EVENT_NAME_LENGTH
            <= len(normalized)
            <= MAX_EVENT_NAME_LENGTH
        ):
            raise EventValidationError(
                "Event name length is outside the allowed range."
            )

        if self.event_type not in SUPPORTED_EVENT_TYPES:
            raise UnsupportedEventTypeError(
                f"Unsupported event type: {self.event_type!r}."
            )

        object.__setattr__(self, "name", normalized)


class EventRegistry:
    """Registry for analytics events."""

    __slots__ = ("_events",)

    def __init__(self) -> None:
        """Initialize an empty event registry."""
        self._events: dict[str, EventDefinition] = {}

    def register(self, event: EventDefinition) -> None:
        """Register an event."""
        if event.name in self._events:
            raise DuplicateEventError(
                f"Event {event.name!r} is already registered."
            )

        self._events[event.name] = event

    def unregister(self, name: str) -> None:
        """Remove an event."""
        if name not in self._events:
            raise EventNotFoundError(
                f"Event {name!r} is not registered."
            )

        del self._events[name]

    def get(self, name: str) -> EventDefinition:
        """Return a registered event."""
        try:
            return self._events[name]
        except KeyError as exc:
            raise EventNotFoundError(
                f"Event {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether an event exists."""
        return name in self._events

    def clear(self) -> None:
        """Remove all registered events."""
        self._events.clear()

    def list(self) -> tuple[EventDefinition, ...]:
        """Return all registered events."""
        return tuple(self._events.values())

    def __len__(self) -> int:
        """Return the number of registered events."""
        return len(self._events)

    def __contains__(self, name: object) -> bool:
        """Return whether an event exists."""
        return isinstance(name, str) and name in self._events


def build_event(
    *,
    name: str,
    payload: dict[str, Any] | None = None,
    event_type: str = DEFAULT_EVENT_TYPE,
    description: str = "",
    tags: tuple[str, ...] = (),
    enabled: bool = DEFAULT_ENABLED,
) -> EventDefinition:
    """Build and validate an event definition."""
    return EventDefinition(
        name=name,
        payload={} if payload is None else payload,
        event_type=event_type,
        description=description,
        tags=tags,
        enabled=enabled,
    )


__all__ = [
    "EventDefinition",
    "EventRegistry",
    "build_event",
]