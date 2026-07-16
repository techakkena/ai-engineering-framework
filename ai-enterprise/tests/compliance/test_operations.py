"""Tests for ai_enterprise.compliance.operations."""

from __future__ import annotations

import pytest

from ai_enterprise.compliance.constants import (
    DEFAULT_ENABLED,
    DEFAULT_STANDARD,
)
from ai_enterprise.compliance.exceptions import (
    ComplianceNotFoundError,
    ComplianceValidationError,
    DuplicateComplianceError,
    UnsupportedComplianceStandardError,
)
from ai_enterprise.compliance.operations import (
    ComplianceDefinition,
    ComplianceRegistry,
    build_compliance,
)


def test_compliance_defaults() -> None:
    compliance = ComplianceDefinition(
        name="baseline",
    )

    assert compliance.name == "baseline"
    assert compliance.standard == DEFAULT_STANDARD
    assert compliance.description == ""
    assert compliance.enabled is DEFAULT_ENABLED


def test_compliance_trims_name() -> None:
    compliance = ComplianceDefinition(
        name="  baseline  ",
    )

    assert compliance.name == "baseline"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "  ",
        "ab",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        ComplianceValidationError,
    ):
        ComplianceDefinition(
            name=name,
        )


def test_invalid_standard() -> None:
    with pytest.raises(
        UnsupportedComplianceStandardError,
    ):
        ComplianceDefinition(
            name="baseline",
            standard="pci",
        )


def test_build_compliance() -> None:
    compliance = build_compliance(
        name="gdpr-policy",
        standard="gdpr",
        description="GDPR compliance",
    )

    assert compliance.name == "gdpr-policy"
    assert compliance.standard == "gdpr"
    assert (
        compliance.description
        == "GDPR compliance"
    )


def test_registry_register_and_get() -> None:
    registry = ComplianceRegistry()

    compliance = build_compliance(
        name="baseline",
    )

    registry.register(compliance)

    assert registry.get("baseline") is compliance
    assert registry.exists("baseline")
    assert len(registry) == 1
    assert "baseline" in registry


def test_registry_duplicate_registration() -> None:
    registry = ComplianceRegistry()

    compliance = build_compliance(
        name="baseline",
    )

    registry.register(compliance)

    with pytest.raises(
        DuplicateComplianceError,
    ):
        registry.register(compliance)


def test_registry_unregister() -> None:
    registry = ComplianceRegistry()

    compliance = build_compliance(
        name="baseline",
    )

    registry.register(compliance)
    registry.unregister("baseline")

    assert len(registry) == 0
    assert not registry.exists("baseline")


def test_registry_unregister_missing() -> None:
    registry = ComplianceRegistry()

    with pytest.raises(
        ComplianceNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = ComplianceRegistry()

    with pytest.raises(
        ComplianceNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = ComplianceRegistry()

    registry.register(
        build_compliance(
            name="baseline",
        )
    )
    registry.register(
        build_compliance(
            name="gdpr",
            standard="gdpr",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = ComplianceRegistry()

    first = build_compliance(
        name="baseline",
    )
    second = build_compliance(
        name="gdpr",
        standard="gdpr",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = ComplianceRegistry()

    assert 123 not in registry