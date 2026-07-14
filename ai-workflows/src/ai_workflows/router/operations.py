from __future__ import annotations

from .exceptions import (
    RouteAlreadyExistsError,
    RouteNotFoundError,
)


class Router:
    """Workflow router."""

    def __init__(self) -> None:
        self._routes: dict[str, str] = {}

    def register(
        self,
        name: str,
        target: str,
    ) -> None:
        """Register a route."""

        if name in self._routes:
            raise RouteAlreadyExistsError(f"Route '{name}' already exists.")

        self._routes[name] = target

    def resolve(
        self,
        name: str,
    ) -> str:
        """Resolve a route."""

        try:
            return self._routes[name]
        except KeyError as exc:
            raise RouteNotFoundError(f"Route '{name}' not found.") from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether a route exists."""

        return name in self._routes

    def remove(
        self,
        name: str,
    ) -> None:
        """Remove a route."""

        if name not in self._routes:
            raise RouteNotFoundError(f"Route '{name}' not found.")

        del self._routes[name]

    def clear(self) -> None:
        """Remove all routes."""

        self._routes.clear()

    @property
    def size(self) -> int:
        """Return number of routes."""

        return len(self._routes)
