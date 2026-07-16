"""Operations for the ai_plugins.lifecycle module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_plugins.lifecycle.constants import (
    DEFAULT_ENABLED,
    DEFAULT_PHASE,
    MAX_LIFECYCLE_NAME_LENGTH,
    MIN_LIFECYCLE_NAME_LENGTH,
    SUPPORTED_LIFECYCLE_PHASES,
)
from ai_plugins.lifecycle.exceptions import (
    DuplicateLifecycleError,
    LifecycleNotFoundError,
    LifecycleValidationError,
    UnsupportedLifecyclePhaseError,
)


@dataclass(slots=True, frozen=True)
class LifecycleDefinition:
    """Represents a plugin lifecycle configuration."""

    name: str
    order: int
    phase: str = DEFAULT_PHASE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the lifecycle definition."""
        normalized = self.name.strip()

        if not (
            MIN_LIFECYCLE_NAME_LENGTH
            <= len(normalized)
            <= MAX_LIFECYCLE_NAME_LENGTH
        ):
            raise LifecycleValidationError(
                "Lifecycle name length is outside the allowed range."
            )

        if self.order < 0:
            raise LifecycleValidationError(
                "Lifecycle order must be zero or greater."
            )

        if self.phase not in SUPPORTED_LIFECYCLE_PHASES:
            raise UnsupportedLifecyclePhaseError(
                f"Unsupported lifecycle phase: {self.phase!r}."
            )

        object.__setattr__(self, "name", normalized)


class LifecycleRegistry:
    """Registry for lifecycle definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, LifecycleDefinition] = {}

    def register(
        self,
        lifecycle: LifecycleDefinition,
    ) -> None:
        """Register a lifecycle definition."""
        if lifecycle.name in self._definitions:
            raise DuplicateLifecycleError(
                f"Lifecycle {lifecycle.name!r} is already registered."
            )

        self._definitions[lifecycle.name] = lifecycle

    def unregister(self, name: str) -> None:
        """Remove a lifecycle definition."""
        if name not in self._definitions:
            raise LifecycleNotFoundError(
                f"Lifecycle {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> LifecycleDefinition:
        """Return a registered lifecycle definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise LifecycleNotFoundError(
                f"Lifecycle {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a lifecycle exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered lifecycles."""
        self._definitions.clear()

    def list(self) -> tuple[LifecycleDefinition, ...]:
        """Return all registered lifecycles."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered lifecycles."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a lifecycle exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_lifecycle(
    *,
    name: str,
    order: int,
    phase: str = DEFAULT_PHASE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> LifecycleDefinition:
    """Build and validate a lifecycle definition."""

    return LifecycleDefinition(
        name=name,
        order=order,
        phase=phase,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "LifecycleDefinition",
    "LifecycleRegistry",
    "build_lifecycle",
]