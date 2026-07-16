"""Operations for the ai_plugins.dependencies module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_plugins.dependencies.constants import (
    DEFAULT_DEPENDENCY_TYPE,
    DEFAULT_ENABLED,
    MAX_DEPENDENCY_NAME_LENGTH,
    MIN_DEPENDENCY_NAME_LENGTH,
    SUPPORTED_DEPENDENCY_TYPES,
)
from ai_plugins.dependencies.exceptions import (
    DependencyNotFoundError,
    DependencyValidationError,
    DuplicateDependencyError,
    UnsupportedDependencyTypeError,
)


@dataclass(slots=True, frozen=True)
class DependencyDefinition:
    """Represents a plugin dependency."""

    name: str
    version: str
    dependency_type: str = DEFAULT_DEPENDENCY_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the dependency definition."""
        normalized = self.name.strip()
        normalized_version = self.version.strip()

        if not (
            MIN_DEPENDENCY_NAME_LENGTH
            <= len(normalized)
            <= MAX_DEPENDENCY_NAME_LENGTH
        ):
            raise DependencyValidationError(
                "Dependency name length is outside the allowed range."
            )

        if not normalized_version:
            raise DependencyValidationError(
                "Dependency version cannot be empty."
            )

        if (
            self.dependency_type
            not in SUPPORTED_DEPENDENCY_TYPES
        ):
            raise UnsupportedDependencyTypeError(
                f"Unsupported dependency type: "
                f"{self.dependency_type!r}."
            )

        object.__setattr__(self, "name", normalized)
        object.__setattr__(
            self,
            "version",
            normalized_version,
        )


class DependencyRegistry:
    """Registry for dependency definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[
            str,
            DependencyDefinition,
        ] = {}

    def register(
        self,
        dependency: DependencyDefinition,
    ) -> None:
        """Register a dependency."""
        if dependency.name in self._definitions:
            raise DuplicateDependencyError(
                f"Dependency {dependency.name!r} "
                "is already registered."
            )

        self._definitions[
            dependency.name
        ] = dependency

    def unregister(self, name: str) -> None:
        """Remove a dependency."""
        if name not in self._definitions:
            raise DependencyNotFoundError(
                f"Dependency {name!r} "
                "is not registered."
            )

        del self._definitions[name]

    def get(
        self,
        name: str,
    ) -> DependencyDefinition:
        """Return a dependency."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise DependencyNotFoundError(
                f"Dependency {name!r} "
                "is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a dependency exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all dependencies."""
        self._definitions.clear()

    def list(
        self,
    ) -> tuple[
        DependencyDefinition,
        ...,
    ]:
        """Return registered dependencies."""
        return tuple(
            self._definitions.values()
        )

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._definitions)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        """Return whether a dependency exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_dependency(
    *,
    name: str,
    version: str,
    dependency_type: str = DEFAULT_DEPENDENCY_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> DependencyDefinition:
    """Build a validated dependency."""

    return DependencyDefinition(
        name=name,
        version=version,
        dependency_type=dependency_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "DependencyDefinition",
    "DependencyRegistry",
    "build_dependency",
]