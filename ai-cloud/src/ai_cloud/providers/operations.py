"""Operations for the ai_cloud.providers module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_cloud.providers.constants import (
    DEFAULT_ENABLED,
    DEFAULT_PROVIDER_TYPE,
    MAX_PROVIDER_NAME_LENGTH,
    MIN_PROVIDER_NAME_LENGTH,
    SUPPORTED_PROVIDER_TYPES,
)
from ai_cloud.providers.exceptions import (
    DuplicateProviderError,
    ProviderNotFoundError,
    ProviderValidationError,
    UnsupportedProviderTypeError,
)


@dataclass(slots=True, frozen=True)
class CloudProvider:
    """Represents a cloud provider configuration."""

    name: str
    region: str
    provider_type: str = DEFAULT_PROVIDER_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the cloud provider."""
        normalized_name = self.name.strip()
        normalized_region = self.region.strip()

        if not (
            MIN_PROVIDER_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_PROVIDER_NAME_LENGTH
        ):
            raise ProviderValidationError(
                "Provider name length is outside the allowed range."
            )

        if not normalized_region:
            raise ProviderValidationError(
                "Provider region cannot be empty."
            )

        if (
            self.provider_type
            not in SUPPORTED_PROVIDER_TYPES
        ):
            raise UnsupportedProviderTypeError(
                f"Unsupported provider type: "
                f"{self.provider_type!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized_name,
        )
        object.__setattr__(
            self,
            "region",
            normalized_region,
        )


class CloudProviderRegistry:
    """Registry for cloud providers."""

    __slots__ = ("_providers",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._providers: dict[
            str,
            CloudProvider,
        ] = {}

    def register(
        self,
        provider: CloudProvider,
    ) -> None:
        """Register a provider."""
        if provider.name in self._providers:
            raise DuplicateProviderError(
                f"Provider {provider.name!r} "
                "is already registered."
            )

        self._providers[
            provider.name
        ] = provider

    def unregister(
        self,
        name: str,
    ) -> None:
        """Remove a provider."""
        if name not in self._providers:
            raise ProviderNotFoundError(
                f"Provider {name!r} "
                "is not registered."
            )

        del self._providers[name]

    def get(
        self,
        name: str,
    ) -> CloudProvider:
        """Return a provider."""
        try:
            return self._providers[name]
        except KeyError as exc:
            raise ProviderNotFoundError(
                f"Provider {name!r} "
                "is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether a provider exists."""
        return name in self._providers

    def clear(self) -> None:
        """Remove all providers."""
        self._providers.clear()

    def list(
        self,
    ) -> tuple[
        CloudProvider,
        ...,
    ]:
        """Return all providers."""
        return tuple(
            self._providers.values()
        )

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._providers)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        """Return whether a provider exists."""
        return (
            isinstance(name, str)
            and name in self._providers
        )


def build_provider(
    *,
    name: str,
    region: str,
    provider_type: str = DEFAULT_PROVIDER_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> CloudProvider:
    """Build a validated cloud provider."""

    return CloudProvider(
        name=name,
        region=region,
        provider_type=provider_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "CloudProvider",
    "CloudProviderRegistry",
    "build_provider",
]