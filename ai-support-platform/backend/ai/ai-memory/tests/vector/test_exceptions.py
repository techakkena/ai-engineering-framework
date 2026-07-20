from __future__ import annotations

"""Tests for ai_memory.vector.exceptions."""

from ai_memory.vector.exceptions import (
    VectorError,
    VectorNotFoundError,
    VectorStateError,
    VectorValidationError,
)


def test_exception_inheritance() -> None:
    assert issubclass(VectorNotFoundError, VectorError)
    assert issubclass(VectorValidationError, VectorError)
    assert issubclass(VectorStateError, VectorError)


def test_raise_vector_not_found_error() -> None:
    try:
        raise VectorNotFoundError("not found")
    except VectorNotFoundError as exc:
        assert str(exc) == "not found"


def test_raise_vector_validation_error() -> None:
    try:
        raise VectorValidationError("validation")
    except VectorValidationError as exc:
        assert str(exc) == "validation"


def test_raise_vector_state_error() -> None:
    try:
        raise VectorStateError("state")
    except VectorStateError as exc:
        assert str(exc) == "state"
