"""Operations for the ai_analytics.tracking module."""

from __future__ import annotations

from dataclasses import dataclass, field

from ai_analytics.tracking.constants import (
    DEFAULT_ENABLED,
    DEFAULT_TRACKING_TYPE,
    MAX_TRACKING_NAME_LENGTH,
    MIN_TRACKING_NAME_LENGTH,
    SUPPORTED_TRACKING_TYPES,
)
from ai_analytics.tracking.exceptions import (
    DuplicateTrackingError,
    TrackingNotFoundError,
    TrackingValidationError,
    UnsupportedTrackingTypeError,
)


@dataclass(slots=True, frozen=True)
class TrackingDefinition:
    """Represents an analytics tracking definition."""

    name: str
    identifier: str
    tracking_type: str = DEFAULT_TRACKING_TYPE
    description: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the tracking definition."""
        normalized = self.name.strip()

        if not (
            MIN_TRACKING_NAME_LENGTH
            <= len(normalized)
            <= MAX_TRACKING_NAME_LENGTH
        ):
            raise TrackingValidationError(
                "Tracking name length is outside the allowed range."
            )

        if not self.identifier.strip():
            raise TrackingValidationError(
                "Tracking identifier cannot be empty."
            )

        if self.tracking_type not in SUPPORTED_TRACKING_TYPES:
            raise UnsupportedTrackingTypeError(
                f"Unsupported tracking type: {self.tracking_type!r}."
            )

        object.__setattr__(self, "name", normalized)
        object.__setattr__(
            self,
            "identifier",
            self.identifier.strip(),
        )


class TrackingRegistry:
    """Registry for tracking definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, TrackingDefinition] = {}

    def register(self, tracking: TrackingDefinition) -> None:
        """Register a tracking definition."""
        if tracking.name in self._definitions:
            raise DuplicateTrackingError(
                f"Tracking {tracking.name!r} is already registered."
            )

        self._definitions[tracking.name] = tracking

    def unregister(self, name: str) -> None:
        """Remove a tracking definition."""
        if name not in self._definitions:
            raise TrackingNotFoundError(
                f"Tracking {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> TrackingDefinition:
        """Return a registered tracking definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise TrackingNotFoundError(
                f"Tracking {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a tracking definition exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all tracking definitions."""
        self._definitions.clear()

    def list(self) -> tuple[TrackingDefinition, ...]:
        """Return all registered tracking definitions."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered tracking definitions."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a tracking definition exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_tracking(
    *,
    name: str,
    identifier: str,
    tracking_type: str = DEFAULT_TRACKING_TYPE,
    description: str = "",
    tags: tuple[str, ...] = (),
    enabled: bool = DEFAULT_ENABLED,
) -> TrackingDefinition:
    """Build and validate a tracking definition."""
    return TrackingDefinition(
        name=name,
        identifier=identifier,
        tracking_type=tracking_type,
        description=description,
        tags=tags,
        enabled=enabled,
    )


__all__ = [
    "TrackingDefinition",
    "TrackingRegistry",
    "build_tracking",
]