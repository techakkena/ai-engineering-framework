"""Operations for the ai_cloud.networking module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_cloud.networking.constants import (
    DEFAULT_ENABLED,
    DEFAULT_NETWORK_TYPE,
    MAX_NETWORK_NAME_LENGTH,
    MIN_NETWORK_NAME_LENGTH,
    SUPPORTED_NETWORK_TYPES,
)
from ai_cloud.networking.exceptions import (
    DuplicateNetworkError,
    NetworkNotFoundError,
    NetworkValidationError,
    UnsupportedNetworkTypeError,
)


@dataclass(slots=True, frozen=True)
class NetworkDefinition:
    """Represents a cloud network configuration."""

    name: str
    cidr: str
    network_type: str = DEFAULT_NETWORK_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the network definition."""
        normalized_name = self.name.strip()
        normalized_cidr = self.cidr.strip()

        if not (
            MIN_NETWORK_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_NETWORK_NAME_LENGTH
        ):
            raise NetworkValidationError(
                "Network name length is outside the allowed range."
            )

        if not normalized_cidr:
            raise NetworkValidationError(
                "Network CIDR cannot be empty."
            )

        if (
            self.network_type
            not in SUPPORTED_NETWORK_TYPES
        ):
            raise UnsupportedNetworkTypeError(
                f"Unsupported network type: "
                f"{self.network_type!r}."
            )

        object.__setattr__(self, "name", normalized_name)
        object.__setattr__(self, "cidr", normalized_cidr)


class NetworkRegistry:
    """Registry for network definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, NetworkDefinition] = {}

    def register(
        self,
        network: NetworkDefinition,
    ) -> None:
        """Register a network definition."""
        if network.name in self._definitions:
            raise DuplicateNetworkError(
                f"Network {network.name!r} is already registered."
            )

        self._definitions[network.name] = network

    def unregister(self, name: str) -> None:
        """Remove a network definition."""
        if name not in self._definitions:
            raise NetworkNotFoundError(
                f"Network {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> NetworkDefinition:
        """Return a registered network definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise NetworkNotFoundError(
                f"Network {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a network exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered networks."""
        self._definitions.clear()

    def list(self) -> tuple[NetworkDefinition, ...]:
        """Return all registered networks."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered networks."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a network exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_network(
    *,
    name: str,
    cidr: str,
    network_type: str = DEFAULT_NETWORK_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> NetworkDefinition:
    """Build and validate a network definition."""

    return NetworkDefinition(
        name=name,
        cidr=cidr,
        network_type=network_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "NetworkDefinition",
    "NetworkRegistry",
    "build_network",
]