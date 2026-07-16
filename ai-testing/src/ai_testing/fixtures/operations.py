"""Operations for the ai_testing.fixtures module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_testing.fixtures.constants import (
    DEFAULT_AUTOUSE,
    DEFAULT_CACHE_ENABLED,
    DEFAULT_FIXTURE_SCOPE,
    MAX_FIXTURE_NAME_LENGTH,
    MIN_FIXTURE_NAME_LENGTH,
    SUPPORTED_FIXTURE_SCOPES,
)
from ai_testing.fixtures.exceptions import (
    DuplicateFixtureError,
    FixtureNotFoundError,
    FixtureValidationError,
    UnsupportedFixtureScopeError,
)


@dataclass(slots=True, frozen=True)
class FixtureDefinition:
    """Represents a reusable fixture definition."""

    name: str
    value: Any
    scope: str = DEFAULT_FIXTURE_SCOPE
    autouse: bool = DEFAULT_AUTOUSE
    description: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)
    cache: bool = DEFAULT_CACHE_ENABLED

    def __post_init__(self) -> None:
        """Validate the fixture definition."""
        normalized_name = self.name.strip()

        if not (
            MIN_FIXTURE_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_FIXTURE_NAME_LENGTH
        ):
            raise FixtureValidationError(
                "Fixture name length is outside the allowed range."
            )

        if self.scope not in SUPPORTED_FIXTURE_SCOPES:
            raise UnsupportedFixtureScopeError(
                f"Unsupported fixture scope: {self.scope!r}."
            )

        object.__setattr__(self, "name", normalized_name)


class FixtureRegistry:
    """Registry for fixture definitions."""

    __slots__ = ("_fixtures",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._fixtures: dict[str, FixtureDefinition] = {}

    def register(self, fixture: FixtureDefinition) -> None:
        """Register a fixture.

        Args:
            fixture: Fixture definition to register.

        Raises:
            DuplicateFixtureError: If a fixture with the same name exists.
        """
        if fixture.name in self._fixtures:
            raise DuplicateFixtureError(
                f"Fixture {fixture.name!r} is already registered."
            )

        self._fixtures[fixture.name] = fixture

    def unregister(self, name: str) -> None:
        """Remove a fixture from the registry.

        Args:
            name: Fixture name.

        Raises:
            FixtureNotFoundError: If the fixture is not registered.
        """
        if name not in self._fixtures:
            raise FixtureNotFoundError(
                f"Fixture {name!r} is not registered."
            )

        del self._fixtures[name]

    def get(self, name: str) -> FixtureDefinition:
        """Return a registered fixture.

        Args:
            name: Fixture name.

        Returns:
            The registered fixture.

        Raises:
            FixtureNotFoundError: If the fixture is not registered.
        """
        try:
            return self._fixtures[name]
        except KeyError as exc:
            raise FixtureNotFoundError(
                f"Fixture {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Determine whether a fixture is registered."""
        return name in self._fixtures

    def clear(self) -> None:
        """Remove all registered fixtures."""
        self._fixtures.clear()

    def list(self) -> tuple[FixtureDefinition, ...]:
        """Return all registered fixtures."""
        return tuple(self._fixtures.values())

    def __len__(self) -> int:
        """Return the number of registered fixtures."""
        return len(self._fixtures)

    def __contains__(self, name: object) -> bool:
        """Return whether a fixture name exists."""
        return isinstance(name, str) and name in self._fixtures


def build_fixture(
    *,
    name: str,
    value: Any,
    scope: str = DEFAULT_FIXTURE_SCOPE,
    autouse: bool = DEFAULT_AUTOUSE,
    description: str = "",
    tags: tuple[str, ...] = (),
    cache: bool = DEFAULT_CACHE_ENABLED,
) -> FixtureDefinition:
    """Build and validate a fixture definition.

    Args:
        name: Fixture name.
        value: Fixture value.
        scope: Fixture scope.
        autouse: Whether the fixture is automatically used.
        description: Human-readable description.
        tags: Classification tags.
        cache: Whether the fixture is cacheable.

    Returns:
        A validated fixture definition.
    """
    return FixtureDefinition(
        name=name,
        value=value,
        scope=scope,
        autouse=autouse,
        description=description,
        tags=tags,
        cache=cache,
    )


__all__ = [
    "FixtureDefinition",
    "FixtureRegistry",
    "build_fixture",
]