"""Operations for the ai_enterprise.organizations module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_enterprise.organizations.constants import (
    DEFAULT_ENABLED,
    DEFAULT_ORGANIZATION_TYPE,
    MAX_ORGANIZATION_NAME_LENGTH,
    MIN_ORGANIZATION_NAME_LENGTH,
    SUPPORTED_ORGANIZATION_TYPES,
)
from ai_enterprise.organizations.exceptions import (
    DuplicateOrganizationError,
    OrganizationNotFoundError,
    OrganizationValidationError,
    UnsupportedOrganizationTypeError,
)


@dataclass(slots=True, frozen=True)
class OrganizationDefinition:
    """Represents an enterprise organization."""

    name: str
    domain: str
    organization_type: str = DEFAULT_ORGANIZATION_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate organization."""
        normalized_name = self.name.strip()
        normalized_domain = self.domain.strip()

        if not (
            MIN_ORGANIZATION_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_ORGANIZATION_NAME_LENGTH
        ):
            raise OrganizationValidationError(
                "Organization name length is outside the allowed range."
            )

        if not normalized_domain:
            raise OrganizationValidationError(
                "Organization domain cannot be empty."
            )

        if (
            self.organization_type
            not in SUPPORTED_ORGANIZATION_TYPES
        ):
            raise UnsupportedOrganizationTypeError(
                f"Unsupported organization type: "
                f"{self.organization_type!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized_name,
        )
        object.__setattr__(
            self,
            "domain",
            normalized_domain,
        )


class OrganizationRegistry:
    """Registry for organizations."""

    __slots__ = ("_organizations",)

    def __init__(self) -> None:
        """Initialize registry."""
        self._organizations: dict[
            str,
            OrganizationDefinition,
        ] = {}

    def register(
        self,
        organization: OrganizationDefinition,
    ) -> None:
        """Register an organization."""
        if organization.name in self._organizations:
            raise DuplicateOrganizationError(
                f"Organization {organization.name!r} "
                "is already registered."
            )

        self._organizations[
            organization.name
        ] = organization

    def unregister(
        self,
        name: str,
    ) -> None:
        """Remove an organization."""
        if name not in self._organizations:
            raise OrganizationNotFoundError(
                f"Organization {name!r} "
                "is not registered."
            )

        del self._organizations[name]

    def get(
        self,
        name: str,
    ) -> OrganizationDefinition:
        """Return an organization."""
        try:
            return self._organizations[name]
        except KeyError as exc:
            raise OrganizationNotFoundError(
                f"Organization {name!r} "
                "is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether organization exists."""
        return name in self._organizations

    def clear(self) -> None:
        """Clear registry."""
        self._organizations.clear()

    def list(
        self,
    ) -> tuple[
        OrganizationDefinition,
        ...,
    ]:
        """Return all organizations."""
        return tuple(
            self._organizations.values()
        )

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._organizations)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        """Return membership."""
        return (
            isinstance(name, str)
            and name in self._organizations
        )


def build_organization(
    *,
    name: str,
    domain: str,
    organization_type: str = DEFAULT_ORGANIZATION_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> OrganizationDefinition:
    """Build a validated organization."""

    return OrganizationDefinition(
        name=name,
        domain=domain,
        organization_type=organization_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "OrganizationDefinition",
    "OrganizationRegistry",
    "build_organization",
]