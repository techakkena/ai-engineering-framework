"""Tests for ai_enterprise.tenants.operations."""

from __future__ import annotations

import pytest

from ai_enterprise.tenants.constants import (
    DEFAULT_ENABLED,
    DEFAULT_TENANT_PLAN,
)
from ai_enterprise.tenants.exceptions import (
    DuplicateTenantError,
    TenantNotFoundError,
    TenantValidationError,
    UnsupportedTenantPlanError,
)
from ai_enterprise.tenants.operations import (
    TenantDefinition,
    TenantRegistry,
    build_tenant,
)


def test_tenant_definition_defaults() -> None:
    tenant = TenantDefinition(
        name="TenantA",
        organization="Acme",
    )

    assert tenant.name == "TenantA"
    assert tenant.organization == "Acme"
    assert tenant.plan == DEFAULT_TENANT_PLAN
    assert tenant.description == ""
    assert tenant.enabled is DEFAULT_ENABLED


def test_tenant_definition_trims_values() -> None:
    tenant = TenantDefinition(
        name="  TenantA  ",
        organization="  Acme  ",
    )

    assert tenant.name == "TenantA"
    assert tenant.organization == "Acme"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        TenantValidationError,
    ):
        TenantDefinition(
            name=name,
            organization="Acme",
        )


@pytest.mark.parametrize(
    "organization",
    [
        "",
        "   ",
    ],
)
def test_invalid_organization(
    organization: str,
) -> None:
    with pytest.raises(
        TenantValidationError,
    ):
        TenantDefinition(
            name="TenantA",
            organization=organization,
        )


def test_invalid_plan() -> None:
    with pytest.raises(
        UnsupportedTenantPlanError,
    ):
        TenantDefinition(
            name="TenantA",
            organization="Acme",
            plan="invalid",
        )


def test_build_tenant() -> None:
    tenant = build_tenant(
        name="TenantA",
        organization="Acme",
        plan="enterprise",
        description="Production tenant",
    )

    assert tenant.name == "TenantA"
    assert tenant.organization == "Acme"
    assert tenant.plan == "enterprise"
    assert tenant.description == "Production tenant"


def test_registry_register_and_get() -> None:
    registry = TenantRegistry()

    tenant = build_tenant(
        name="TenantA",
        organization="Acme",
    )

    registry.register(tenant)

    assert registry.get("TenantA") is tenant
    assert registry.exists("TenantA")
    assert len(registry) == 1
    assert "TenantA" in registry


def test_registry_duplicate_registration() -> None:
    registry = TenantRegistry()

    tenant = build_tenant(
        name="TenantA",
        organization="Acme",
    )

    registry.register(tenant)

    with pytest.raises(
        DuplicateTenantError,
    ):
        registry.register(tenant)


def test_registry_unregister() -> None:
    registry = TenantRegistry()

    tenant = build_tenant(
        name="TenantA",
        organization="Acme",
    )

    registry.register(tenant)
    registry.unregister("TenantA")

    assert len(registry) == 0
    assert not registry.exists("TenantA")


def test_registry_unregister_missing() -> None:
    registry = TenantRegistry()

    with pytest.raises(
        TenantNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = TenantRegistry()

    with pytest.raises(
        TenantNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = TenantRegistry()

    registry.register(
        build_tenant(
            name="One",
            organization="Org1",
        )
    )
    registry.register(
        build_tenant(
            name="Two",
            organization="Org2",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = TenantRegistry()

    first = build_tenant(
        name="One",
        organization="Org1",
    )
    second = build_tenant(
        name="Two",
        organization="Org2",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = TenantRegistry()

    assert 123 not in registry