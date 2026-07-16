"""Operations for the ai_plugins.discovery module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_plugins.discovery.constants import (
    DEFAULT_DISCOVERY_STRATEGY,
    DEFAULT_ENABLED,
    MAX_DISCOVERY_NAME_LENGTH,
    MIN_DISCOVERY_NAME_LENGTH,
    SUPPORTED_DISCOVERY_STRATEGIES,
)
from ai_plugins.discovery.exceptions import (
    DiscoveryNotFoundError,
    DiscoveryValidationError,
    DuplicateDiscoveryError,
    UnsupportedDiscoveryStrategyError,
)


@dataclass(slots=True, frozen=True)
class DiscoveryDefinition:
    """Represents a plugin discovery configuration."""

    name: str
    path: str
    strategy: str = DEFAULT_DISCOVERY_STRATEGY
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the discovery definition."""
        normalized = self.name.strip()
        normalized_path = self.path.strip()

        if not (
            MIN_DISCOVERY_NAME_LENGTH
            <= len(normalized)
            <= MAX_DISCOVERY_NAME_LENGTH
        ):
            raise DiscoveryValidationError(
                "Discovery name length is outside the allowed range."
            )

        if not normalized_path:
            raise DiscoveryValidationError(
                "Discovery path cannot be empty."
            )

        if self.strategy not in SUPPORTED_DISCOVERY_STRATEGIES:
            raise UnsupportedDiscoveryStrategyError(
                f"Unsupported discovery strategy: {self.strategy!r}."
            )

        object.__setattr__(self, "name", normalized)
        object.__setattr__(self, "path", normalized_path)


class DiscoveryRegistry:
    """Registry for discovery definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, DiscoveryDefinition] = {}

    def register(
        self,
        discovery: DiscoveryDefinition,
    ) -> None:
        """Register a discovery definition."""
        if discovery.name in self._definitions:
            raise DuplicateDiscoveryError(
                f"Discovery {discovery.name!r} is already registered."
            )

        self._definitions[discovery.name] = discovery

    def unregister(self, name: str) -> None:
        """Remove a discovery definition."""
        if name not in self._definitions:
            raise DiscoveryNotFoundError(
                f"Discovery {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> DiscoveryDefinition:
        """Return a registered discovery definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise DiscoveryNotFoundError(
                f"Discovery {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a discovery exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered discoveries."""
        self._definitions.clear()

    def list(self) -> tuple[DiscoveryDefinition, ...]:
        """Return all registered discoveries."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered discoveries."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a discovery exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_discovery(
    *,
    name: str,
    path: str,
    strategy: str = DEFAULT_DISCOVERY_STRATEGY,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> DiscoveryDefinition:
    """Build and validate a discovery definition."""

    return DiscoveryDefinition(
        name=name,
        path=path,
        strategy=strategy,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "DiscoveryDefinition",
    "DiscoveryRegistry",
    "build_discovery",
]