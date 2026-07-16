"""Tests for ai_enterprise.auditing.operations."""

from __future__ import annotations

import pytest

from ai_enterprise.auditing.constants import (
    DEFAULT_AUDIT_LEVEL,
    DEFAULT_ENABLED,
)
from ai_enterprise.auditing.exceptions import (
    AuditNotFoundError,
    AuditValidationError,
    DuplicateAuditError,
    UnsupportedAuditLevelError,
)
from ai_enterprise.auditing.operations import (
    AuditDefinition,
    AuditRegistry,
    build_audit,
)


def test_audit_defaults() -> None:
    audit = AuditDefinition(
        name="system",
    )

    assert audit.name == "system"
    assert audit.level == DEFAULT_AUDIT_LEVEL
    assert audit.description == ""
    assert audit.enabled is DEFAULT_ENABLED


def test_audit_trims_name() -> None:
    audit = AuditDefinition(
        name="  system  ",
    )

    assert audit.name == "system"


@pytest.mark.parametrize(
    "name",
    [
        "",
        " ",
        "ab",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        AuditValidationError,
    ):
        AuditDefinition(
            name=name,
        )


def test_invalid_level() -> None:
    with pytest.raises(
        UnsupportedAuditLevelError,
    ):
        AuditDefinition(
            name="system",
            level="debug",
        )


def test_build_audit() -> None:
    audit = build_audit(
        name="security",
        level="critical",
        description="Security audit",
    )

    assert audit.name == "security"
    assert audit.level == "critical"
    assert audit.description == "Security audit"


def test_registry_register_and_get() -> None:
    registry = AuditRegistry()

    audit = build_audit(
        name="system",
    )

    registry.register(audit)

    assert registry.get("system") is audit
    assert registry.exists("system")
    assert len(registry) == 1
    assert "system" in registry


def test_registry_duplicate_registration() -> None:
    registry = AuditRegistry()

    audit = build_audit(
        name="system",
    )

    registry.register(audit)

    with pytest.raises(
        DuplicateAuditError,
    ):
        registry.register(audit)


def test_registry_unregister() -> None:
    registry = AuditRegistry()

    audit = build_audit(
        name="system",
    )

    registry.register(audit)
    registry.unregister("system")

    assert len(registry) == 0
    assert not registry.exists("system")


def test_registry_unregister_missing() -> None:
    registry = AuditRegistry()

    with pytest.raises(
        AuditNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = AuditRegistry()

    with pytest.raises(
        AuditNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = AuditRegistry()

    registry.register(
        build_audit(
            name="system",
        )
    )
    registry.register(
        build_audit(
            name="security",
            level="critical",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = AuditRegistry()

    first = build_audit(
        name="system",
    )
    second = build_audit(
        name="security",
        level="critical",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = AuditRegistry()

    assert 123 not in registry