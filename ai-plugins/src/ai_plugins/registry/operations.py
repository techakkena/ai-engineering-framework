"""Operations for the ai_plugins.registry module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_plugins.registry.constants import (
    DEFAULT_ENABLED,
    DEFAULT_PLUGIN_VERSION,
    MAX_PLUGIN_NAME_LENGTH,
    MIN_PLUGIN_NAME_LENGTH,
    REGISTERED_STATE,
    SUPPORTED_PLUGIN_STATES,
)
from ai_plugins.registry.exceptions import (
    DuplicatePluginError,
    PluginNotFoundError,
    PluginValidationError,
    UnsupportedPluginStateError,
)


@dataclass(slots=True, frozen=True)
class PluginDefinition:
    """Represents a plugin definition."""

    name: str
    version: str = DEFAULT_PLUGIN_VERSION
    state: str = REGISTERED_STATE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the plugin definition."""
        normalized = self.name.strip()

        if not (
            MIN_PLUGIN_NAME_LENGTH
            <= len(normalized)
            <= MAX_PLUGIN_NAME_LENGTH
        ):
            raise PluginValidationError(
                "Plugin name length is outside the allowed range."
            )

        if not self.version.strip():
            raise PluginValidationError(
                "Plugin version cannot be empty."
            )

        if self.state not in SUPPORTED_PLUGIN_STATES:
            raise UnsupportedPluginStateError(
                f"Unsupported plugin state: {self.state!r}."
            )

        object.__setattr__(self, "name", normalized)
        object.__setattr__(
            self,
            "version",
            self.version.strip(),
        )


class PluginRegistry:
    """Registry for plugin definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, PluginDefinition] = {}

    def register(
        self,
        plugin: PluginDefinition,
    ) -> None:
        """Register a plugin definition."""
        if plugin.name in self._definitions:
            raise DuplicatePluginError(
                f"Plugin {plugin.name!r} is already registered."
            )

        self._definitions[plugin.name] = plugin

    def unregister(self, name: str) -> None:
        """Remove a plugin definition."""
        if name not in self._definitions:
            raise PluginNotFoundError(
                f"Plugin {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> PluginDefinition:
        """Return a registered plugin definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise PluginNotFoundError(
                f"Plugin {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a plugin exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered plugins."""
        self._definitions.clear()

    def list(self) -> tuple[PluginDefinition, ...]:
        """Return all registered plugins."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered plugins."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a plugin exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_plugin(
    *,
    name: str,
    version: str = DEFAULT_PLUGIN_VERSION,
    state: str = REGISTERED_STATE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> PluginDefinition:
    """Build and validate a plugin definition."""

    return PluginDefinition(
        name=name,
        version=version,
        state=state,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "PluginDefinition",
    "PluginRegistry",
    "build_plugin",
]