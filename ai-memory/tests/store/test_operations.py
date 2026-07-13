"""Tests for ai_memory.store.operations."""

import pytest

from ai_memory.store.constants import StoreState, StoreType
from ai_memory.store.exceptions import StoreValidationError
from ai_memory.store.operations import (
    is_valid_store_state,
    is_valid_store_type,
    validate_store_state,
    validate_store_type,
)


def test_validate_store_type() -> None:
    assert validate_store_type("memory") is StoreType.MEMORY


def test_validate_store_state() -> None:
    assert validate_store_state("active") is StoreState.ACTIVE


@pytest.mark.parametrize(
    ("value", "validator"),
    [
        ("invalid", validate_store_type),
        ("invalid", validate_store_state),
    ],
)
def test_validation_errors(value: str, validator) -> None:
    with pytest.raises(StoreValidationError):
        validator(value)


def test_is_valid_store_type() -> None:
    assert is_valid_store_type("redis")
    assert not is_valid_store_type("invalid")


def test_is_valid_store_state() -> None:
    assert is_valid_store_state("archived")
    assert not is_valid_store_state("invalid")