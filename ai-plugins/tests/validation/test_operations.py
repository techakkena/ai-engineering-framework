"""Tests for ai_plugins.validation.operations."""

from __future__ import annotations

import pytest

from ai_plugins.validation.constants import (
    DEFAULT_ENABLED,
    DEFAULT_VALIDATION_LEVEL,
)
from ai_plugins.validation.exceptions import (
    DuplicateValidationError,
    UnsupportedValidationLevelError,
    ValidationDefinitionError,
    ValidationNotFoundError,
)
from ai_plugins.validation.operations import (
    ValidationDefinition,
    ValidationRegistry,
    build_validation,
)


def test_validation_definition_defaults() -> None:
    validation = ValidationDefinition(
        name="default",
        rule_count=5,
    )

    assert validation.name == "default"
    assert validation.rule_count == 5
    assert validation.level == DEFAULT_VALIDATION_LEVEL
    assert validation.description == ""
    assert validation.enabled is DEFAULT_ENABLED


def test_validation_definition_trims_name() -> None:
    validation = ValidationDefinition(
        name="  default  ",
        rule_count=5,
    )

    assert validation.name == "default"


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
        ValidationDefinitionError,
    ):
        ValidationDefinition(
            name=name,
            rule_count=5,
        )


@pytest.mark.parametrize(
    "rule_count",
    [
        0,
        -1,
        -10,
    ],
)
def test_invalid_rule_count(
    rule_count: int,
) -> None:
    with pytest.raises(
        ValidationDefinitionError,
    ):
        ValidationDefinition(
            name="default",
            rule_count=rule_count,
        )


def test_invalid_level() -> None:
    with pytest.raises(
        UnsupportedValidationLevelError,
    ):
        ValidationDefinition(
            name="default",
            rule_count=5,
            level="invalid",
        )


def test_build_validation() -> None:
    validation = build_validation(
        name="strict",
        rule_count=10,
        level="strict",
        description="Strict validation",
    )

    assert validation.name == "strict"
    assert validation.rule_count == 10
    assert validation.level == "strict"
    assert validation.description == "Strict validation"


def test_registry_register_and_get() -> None:
    registry = ValidationRegistry()

    validation = build_validation(
        name="default",
        rule_count=5,
    )

    registry.register(validation)

    assert registry.get("default") is validation
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = ValidationRegistry()

    validation = build_validation(
        name="default",
        rule_count=5,
    )

    registry.register(validation)

    with pytest.raises(
        DuplicateValidationError,
    ):
        registry.register(validation)


def test_registry_unregister() -> None:
    registry = ValidationRegistry()

    validation = build_validation(
        name="default",
        rule_count=5,
    )

    registry.register(validation)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = ValidationRegistry()

    with pytest.raises(
        ValidationNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = ValidationRegistry()

    with pytest.raises(
        ValidationNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = ValidationRegistry()

    registry.register(
        build_validation(
            name="one",
            rule_count=1,
        )
    )
    registry.register(
        build_validation(
            name="two",
            rule_count=2,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = ValidationRegistry()

    first = build_validation(
        name="one",
        rule_count=1,
    )
    second = build_validation(
        name="two",
        rule_count=2,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = ValidationRegistry()

    assert 123 not in registry