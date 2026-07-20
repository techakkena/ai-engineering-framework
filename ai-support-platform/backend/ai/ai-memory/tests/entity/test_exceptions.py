from __future__ import annotations

"""Tests for ai_memory.entity.exceptions."""

from ai_memory.entity.exceptions import (
    EntityError,
    EntityNotFoundError,
    EntityStateError,
    EntityValidationError,
)


def test_exception_inheritance() -> None:
    assert issubclass(EntityNotFoundError, EntityError)
    assert issubclass(EntityValidationError, EntityError)
    assert issubclass(EntityStateError, EntityError)


def test_raise_entity_not_found_error() -> None:
    try:
        raise EntityNotFoundError("not found")
    except EntityNotFoundError as exc:
        assert str(exc) == "not found"


def test_raise_entity_validation_error() -> None:
    try:
        raise EntityValidationError("validation")
    except EntityValidationError as exc:
        assert str(exc) == "validation"


def test_raise_entity_state_error() -> None:
    try:
        raise EntityStateError("state")
    except EntityStateError as exc:
        assert str(exc) == "state"
