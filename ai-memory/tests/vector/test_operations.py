"""Tests for ai_memory.vector.operations."""

import pytest

from ai_memory.vector.constants import (
    VectorMetric,
    VectorState,
    VectorType,
)
from ai_memory.vector.exceptions import VectorValidationError
from ai_memory.vector.operations import (
    is_valid_vector_metric,
    is_valid_vector_state,
    is_valid_vector_type,
    validate_vector_metric,
    validate_vector_state,
    validate_vector_type,
)


def test_validate_vector_type() -> None:
    assert validate_vector_type("dense") is VectorType.DENSE


def test_validate_vector_metric() -> None:
    assert validate_vector_metric("cosine") is VectorMetric.COSINE


def test_validate_vector_state() -> None:
    assert validate_vector_state("active") is VectorState.ACTIVE


@pytest.mark.parametrize(
    ("value", "validator"),
    [
        ("invalid", validate_vector_type),
        ("invalid", validate_vector_metric),
        ("invalid", validate_vector_state),
    ],
)
def test_validation_errors(value: str, validator) -> None:
    with pytest.raises(VectorValidationError):
        validator(value)


def test_is_valid_vector_type() -> None:
    assert is_valid_vector_type("hybrid")
    assert not is_valid_vector_type("invalid")


def test_is_valid_vector_metric() -> None:
    assert is_valid_vector_metric("dot_product")
    assert not is_valid_vector_metric("invalid")


def test_is_valid_vector_state() -> None:
    assert is_valid_vector_state("archived")
    assert not is_valid_vector_state("invalid")