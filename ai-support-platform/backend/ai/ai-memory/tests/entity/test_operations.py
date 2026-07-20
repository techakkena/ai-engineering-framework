from __future__ import annotations

"""Tests for ai_memory.entity.operations."""

import pytest

from ai_memory.entity.constants import EntityState
from ai_memory.entity.constants import EntityType
from ai_memory.entity.exceptions import EntityValidationError
from ai_memory.entity.operations import (
    is_valid_entity_state,
    is_valid_entity_type,
    validate_entity_state,
    validate_entity_type,
)


def test_validate_entity_type() -> None:
    assert validate_entity_type("person") is EntityType.PERSON


def test_validate_entity_state() -> None:
    assert validate_entity_state("active") is EntityState.ACTIVE


@pytest.mark.parametrize(
    ("value", "validator"),
    [
        ("invalid", validate_entity_type),
        ("invalid", validate_entity_state),
    ],
)
def test_validation_errors(value: str, validator) -> None:
    with pytest.raises(EntityValidationError):
        validator(value)


def test_is_valid_entity_type() -> None:
    assert is_valid_entity_type("organization")
    assert not is_valid_entity_type("invalid")


def test_is_valid_entity_state() -> None:
    assert is_valid_entity_state("archived")
    assert not is_valid_entity_state("invalid")
