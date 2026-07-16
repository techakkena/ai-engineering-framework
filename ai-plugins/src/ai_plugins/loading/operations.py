"""Operations for the ai_plugins.loading module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_plugins.loading.constants import (
    DEFAULT_ENABLED,
    DEFAULT_LOADING_MODE,
    MAX_LOADER_NAME_LENGTH,
    MIN_LOADER_NAME_LENGTH,
    SUPPORTED_LOADING_MODES,
)
from ai_plugins.loading.exceptions import (
    DuplicateLoaderError,
    LoaderNotFoundError,
    LoaderValidationError,
    UnsupportedLoadingModeError,
)


@dataclass(slots=True, frozen=True)
class LoaderDefinition:
    """Represents a plugin loader configuration."""

    name: str
    timeout: float
    mode: str = DEFAULT_LOADING_MODE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the loader definition."""
        normalized = self.name.strip()

        if not (
            MIN_LOADER_NAME_LENGTH
            <= len(normalized)
            <= MAX_LOADER_NAME_LENGTH
        ):
            raise LoaderValidationError(
                "Loader name length is outside the allowed range."
            )

        if self.timeout <= 0:
            raise LoaderValidationError(
                "Loader timeout must be greater than zero."
            )

        if self.mode not in SUPPORTED_LOADING_MODES:
            raise UnsupportedLoadingModeError(
                f"Unsupported loading mode: {self.mode!r}."
            )

        object.__setattr__(self, "name", normalized)


class LoaderRegistry:
    """Registry for loader definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, LoaderDefinition] = {}

    def register(
        self,
        loader: LoaderDefinition,
    ) -> None:
        """Register a loader definition."""
        if loader.name in self._definitions:
            raise DuplicateLoaderError(
                f"Loader {loader.name!r} is already registered."
            )

        self._definitions[loader.name] = loader

    def unregister(self, name: str) -> None:
        """Remove a loader definition."""
        if name not in self._definitions:
            raise LoaderNotFoundError(
                f"Loader {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> LoaderDefinition:
        """Return a registered loader definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise LoaderNotFoundError(
                f"Loader {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a loader exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered loaders."""
        self._definitions.clear()

    def list(self) -> tuple[LoaderDefinition, ...]:
        """Return all registered loaders."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered loaders."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a loader exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_loader(
    *,
    name: str,
    timeout: float,
    mode: str = DEFAULT_LOADING_MODE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> LoaderDefinition:
    """Build and validate a loader definition."""

    return LoaderDefinition(
        name=name,
        timeout=timeout,
        mode=mode,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "LoaderDefinition",
    "LoaderRegistry",
    "build_loader",
]