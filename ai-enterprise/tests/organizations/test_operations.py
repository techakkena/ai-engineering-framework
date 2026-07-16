"""Tests for ai_enterprise.organizations.operations."""

from __future__ import annotations

import pytest

from ai_enterprise.organizations.constants import (
    DEFAULT_ENABLED,
    DEFAULT_ORGANIZATION_TYPE,
)
from ai_enterprise.organizations.exceptions import (
    DuplicateOrganizationError,
    OrganizationNotFoundError,
    OrganizationValidationError,
    UnsupportedOrganizationTypeError,
)
from ai_enterprise.organizations.operations import (
    OrganizationDefinition,
    OrganizationRegistry,
    build_organization,
)


def test_organization_definition_defaults() -> None:
    organization = OrganizationDefinition(
        name="Acme",
        domain="acme.com",
    )

    assert organization.name == "Acme"
    assert organization.domain == "acme.com"
    assert (
        organization.organization_type
        == DEFAULT_ORGANIZATION_TYPE
    )
    assert organization.description == ""
    assert organization.enabled is DEFAULT_ENABLED


def test_organization_definition_trims_values() -> None:
    organization = OrganizationDefinition(
        name="  Acme  ",
        domain="  acme.com  ",
    )

    assert organization.name == "Acme"
    assert organization.domain == "acme.com"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(
        OrganizationValidationError,
    ):
        OrganizationDefinition(
            name=name,
            domain="acme.com",
        )


@pytest.mark.parametrize(
    "domain",
    [
        "",
        "   ",
    ],
)
def test_invalid_domain(domain: str) -> None:
    with pytest.raises(
        OrganizationValidationError,
    ):
        OrganizationDefinition(
            name="Acme",
            domain=domain,
        )


def test_invalid_organization_type() -> None:
    with pytest.raises(
        UnsupportedOrganizationTypeError,
    ):
        OrganizationDefinition(
            name="Acme",
            domain="acme.com",
            organization_type="invalid",
        )


def test_build_organization() -> None:
    organization = build_organization(
        name="Acme",
        domain="acme.com",
        organization_type="business",
        description="Business organization",
    )

    assert organization.name == "Acme"
    assert organization.domain == "acme.com"
    assert organization.organization_type == "business"
    assert (
        organization.description
        == "Business organization"
    )


def test_registry_register_and_get() -> None:
    registry = OrganizationRegistry()

    organization = build_organization(
        name="Acme",
        domain="acme.com",
    )

    registry.register(organization)

    assert registry.get("Acme") is organization
    assert registry.exists("Acme")
    assert len(registry) == 1
    assert "Acme" in registry


def test_registry_duplicate_registration() -> None:
    registry = OrganizationRegistry()

    organization = build_organization(
        name="Acme",
        domain="acme.com",
    )

    registry.register(organization)

    with pytest.raises(
        DuplicateOrganizationError,
    ):
        registry.register(organization)


def test_registry_unregister() -> None:
    registry = OrganizationRegistry()

    organization = build_organization(
        name="Acme",
        domain="acme.com",
    )

    registry.register(organization)
    registry.unregister("Acme")

    assert len(registry) == 0
    assert not registry.exists("Acme")


def test_registry_unregister_missing() -> None:
    registry = OrganizationRegistry()

    with pytest.raises(
        OrganizationNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = OrganizationRegistry()

    with pytest.raises(
        OrganizationNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = OrganizationRegistry()

    registry.register(
        build_organization(
            name="One",
            domain="one.com",
        )
    )
    registry.register(
        build_organization(
            name="Two",
            domain="two.com",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = OrganizationRegistry()

    first = build_organization(
        name="One",
        domain="one.com",
    )
    second = build_organization(
        name="Two",
        domain="two.com",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = OrganizationRegistry()

    assert 123 not in registry