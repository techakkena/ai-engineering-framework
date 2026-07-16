"""Operations for the ai_optimization.routing module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_optimization.routing.constants import (
    DEFAULT_ENABLED,
    DEFAULT_ROUTING_STRATEGY,
    MAX_ROUTE_NAME_LENGTH,
    MIN_ROUTE_NAME_LENGTH,
    SUPPORTED_ROUTING_STRATEGIES,
)
from ai_optimization.routing.exceptions import (
    DuplicateRouteError,
    RouteNotFoundError,
    RouteValidationError,
    UnsupportedRoutingStrategyError,
)


@dataclass(slots=True, frozen=True)
class RouteDefinition:
    """Represents a routing configuration."""

    name: str
    weight: int
    strategy: str = DEFAULT_ROUTING_STRATEGY
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the route definition."""
        normalized = self.name.strip()

        if not (
            MIN_ROUTE_NAME_LENGTH
            <= len(normalized)
            <= MAX_ROUTE_NAME_LENGTH
        ):
            raise RouteValidationError(
                "Route name length is outside the allowed range."
            )

        if self.weight <= 0:
            raise RouteValidationError(
                "Route weight must be greater than zero."
            )

        if self.strategy not in SUPPORTED_ROUTING_STRATEGIES:
            raise UnsupportedRoutingStrategyError(
                f"Unsupported routing strategy: {self.strategy!r}."
            )

        object.__setattr__(self, "name", normalized)


class RouteRegistry:
    """Registry for route definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, RouteDefinition] = {}

    def register(self, route: RouteDefinition) -> None:
        """Register a route definition."""
        if route.name in self._definitions:
            raise DuplicateRouteError(
                f"Route {route.name!r} is already registered."
            )

        self._definitions[route.name] = route

    def unregister(self, name: str) -> None:
        """Remove a route definition."""
        if name not in self._definitions:
            raise RouteNotFoundError(
                f"Route {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> RouteDefinition:
        """Return a registered route definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise RouteNotFoundError(
                f"Route {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a route exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered routes."""
        self._definitions.clear()

    def list(self) -> tuple[RouteDefinition, ...]:
        """Return all registered routes."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered routes."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a route exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_route(
    *,
    name: str,
    weight: int,
    strategy: str = DEFAULT_ROUTING_STRATEGY,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> RouteDefinition:
    """Build and validate a route definition."""
    return RouteDefinition(
        name=name,
        weight=weight,
        strategy=strategy,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "RouteDefinition",
    "RouteRegistry",
    "build_route",
]