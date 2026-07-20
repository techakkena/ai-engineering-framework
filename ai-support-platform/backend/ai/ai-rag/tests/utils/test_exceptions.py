from __future__ import annotations

from ai_rag.utils.exceptions import (
    EmptyValueError,
    InvalidInputError,
    UtilityError,
)


def test_utility_error():
    assert issubclass(
        UtilityError,
        Exception,
    )


def test_invalid_input_error():
    assert issubclass(
        InvalidInputError,
        UtilityError,
    )


def test_empty_value_error():
    assert issubclass(
        EmptyValueError,
        UtilityError,
    )
