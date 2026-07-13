"""Tests for ai_memory.entity.constants."""

from ai_memory.entity.constants import (
    DEFAULT_ENTITY_CONFIDENCE,
    DEFAULT_ENTITY_NAMESPACE,
    EntityState,
    EntityType,
)


def test_entity_type_values() -> None:
    assert EntityType.PERSON.value == "person"
    assert EntityType.ORGANIZATION.value == "organization"
    assert EntityType.LOCATION.value == "location"
    assert EntityType.PRODUCT.value == "product"
    assert EntityType.EVENT.value == "event"
    assert EntityType.CUSTOM.value == "custom"


def test_entity_state_values() -> None:
    assert EntityState.ACTIVE.value == "active"
    assert EntityState.INACTIVE.value == "inactive"
    assert EntityState.ARCHIVED.value == "archived"


def test_default_values() -> None:
    assert DEFAULT_ENTITY_CONFIDENCE == 1.0
    assert DEFAULT_ENTITY_NAMESPACE == "default"