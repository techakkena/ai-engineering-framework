"""Tests for ai_memory.store.exceptions."""

from ai_memory.store.exceptions import (
    StoreError,
    StoreNotFoundError,
    StoreStateError,
    StoreValidationError,
)


def test_exception_inheritance() -> None:
    assert issubclass(StoreNotFoundError, StoreError)
    assert issubclass(StoreValidationError, StoreError)
    assert issubclass(StoreStateError, StoreError)


def test_raise_store_not_found_error() -> None:
    try:
        raise StoreNotFoundError("not found")
    except StoreNotFoundError as exc:
        assert str(exc) == "not found"


def test_raise_store_validation_error() -> None:
    try:
        raise StoreValidationError("validation")
    except StoreValidationError as exc:
        assert str(exc) == "validation"


def test_raise_store_state_error() -> None:
    try:
        raise StoreStateError("state")
    except StoreStateError as exc:
        assert str(exc) == "state"