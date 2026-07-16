"""Operations for the ai_enterprise.tenants module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_enterprise.tenants.constants import (
    DEFAULT_ENABLED,
    DEFAULT_TENANT_PLAN,
    MAX_TENANT_NAME_LENGTH,
    MIN_TENANT_NAME_LENGTH,
    SUPPORTED_TENANT_PLANS,
)
from ai_enterprise.tenants.exceptions import (
    DuplicateTenantError,
    TenantNotFoundError,
    TenantValidationError,
    UnsupportedTenantPlanError,
)


@dataclass(slots=True, frozen=True)
class TenantDefinition:
    """Represents an enterprise tenant."""

    name: str
    organization: str
    plan: str = DEFAULT_TENANT_PLAN
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the tenant."""
        normalized_name = self.name.strip()
        normalized_organization = self.organization.strip()

        if not (
            MIN_TENANT_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_TENANT_NAME_LENGTH
        ):
            raise TenantValidationError(
                "Tenant name length is outside the allowed range."
            )

        if not normalized_organization:
            raise TenantValidationError(
                "Organization cannot be empty."
            )

        if self.plan not in SUPPORTED_TENANT_PLANS:
            raise UnsupportedTenantPlanError(
                f"Unsupported tenant plan: {self.plan!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized_name,
        )
        object.__setattr__(
            self,
            "organization",
            normalized_organization,
        )


class TenantRegistry:
    """Registry for tenant definitions."""

    __slots__ = ("_tenants",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._tenants: dict[
            str,
            TenantDefinition,
        ] = {}

    def register(
        self,
        tenant: TenantDefinition,
    ) -> None:
        """Register a tenant."""
        if tenant.name in self._tenants:
            raise DuplicateTenantError(
                f"Tenant {tenant.name!r} is already registered."
            )

        self._tenants[tenant.name] = tenant

    def unregister(
        self,
        name: str,
    ) -> None:
        """Remove a tenant."""
        if name not in self._tenants:
            raise TenantNotFoundError(
                f"Tenant {name!r} is not registered."
            )

        del self._tenants[name]

    def get(
        self,
        name: str,
    ) -> TenantDefinition:
        """Return a tenant."""
        try:
            return self._tenants[name]
        except KeyError as exc:
            raise TenantNotFoundError(
                f"Tenant {name!r} is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether the tenant exists."""
        return name in self._tenants

    def clear(self) -> None:
        """Remove all tenants."""
        self._tenants.clear()

    def list(
        self,
    ) -> tuple[
        TenantDefinition,
        ...,
    ]:
        """Return all registered tenants."""
        return tuple(self._tenants.values())

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._tenants)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        """Return whether a tenant exists."""
        return (
            isinstance(name, str)
            and name in self._tenants
        )


def build_tenant(
    *,
    name: str,
    organization: str,
    plan: str = DEFAULT_TENANT_PLAN,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> TenantDefinition:
    """Build a validated tenant."""

    return TenantDefinition(
        name=name,
        organization=organization,
        plan=plan,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "TenantDefinition",
    "TenantRegistry",
    "build_tenant",
]