"""Operations for the ai_optimization.caching module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_optimization.caching.constants import (
    DEFAULT_CACHE_BACKEND,
    DEFAULT_ENABLED,
    MAX_CACHE_NAME_LENGTH,
    MIN_CACHE_NAME_LENGTH,
    SUPPORTED_CACHE_BACKENDS,
)
from ai_optimization.caching.exceptions import (
    CacheNotFoundError,
    CacheValidationError,
    DuplicateCacheError,
    UnsupportedCacheBackendError,
)


@dataclass(slots=True, frozen=True)
class CacheDefinition:
    """Represents a cache configuration."""

    name: str
    capacity: int
    backend: str = DEFAULT_CACHE_BACKEND
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the cache definition."""
        normalized = self.name.strip()

        if not (
            MIN_CACHE_NAME_LENGTH
            <= len(normalized)
            <= MAX_CACHE_NAME_LENGTH
        ):
            raise CacheValidationError(
                "Cache name length is outside the allowed range."
            )

        if self.capacity <= 0:
            raise CacheValidationError(
                "Cache capacity must be greater than zero."
            )

        if self.backend not in SUPPORTED_CACHE_BACKENDS:
            raise UnsupportedCacheBackendError(
                f"Unsupported cache backend: {self.backend!r}."
            )

        object.__setattr__(self, "name", normalized)


class CacheRegistry:
    """Registry for cache definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, CacheDefinition] = {}

    def register(
        self,
        cache: CacheDefinition,
    ) -> None:
        """Register a cache definition."""
        if cache.name in self._definitions:
            raise DuplicateCacheError(
                f"Cache {cache.name!r} is already registered."
            )

        self._definitions[cache.name] = cache

    def unregister(self, name: str) -> None:
        """Remove a cache definition."""
        if name not in self._definitions:
            raise CacheNotFoundError(
                f"Cache {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> CacheDefinition:
        """Return a registered cache definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise CacheNotFoundError(
                f"Cache {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a cache exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered cache definitions."""
        self._definitions.clear()

    def list(self) -> tuple[CacheDefinition, ...]:
        """Return all registered cache definitions."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered cache definitions."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a cache exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_cache(
    *,
    name: str,
    capacity: int,
    backend: str = DEFAULT_CACHE_BACKEND,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> CacheDefinition:
    """Build and validate a cache definition."""

    return CacheDefinition(
        name=name,
        capacity=capacity,
        backend=backend,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "CacheDefinition",
    "CacheRegistry",
    "build_cache",
]