"""Tests for ai_analytics.aggregation.exceptions."""

from __future__ import annotations

import pytest

from ai_analytics.aggregation.exceptions import (
    AggregationError,
    AggregationNotFoundError,
    AggregationRegistrationError,
    AggregationValidationError,
    DuplicateAggregationError,
    UnsupportedAggregationTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(AggregationValidationError, AggregationError)
    assert issubclass(
        AggregationRegistrationError,
        AggregationError,
    )
    assert issubclass(
        AggregationNotFoundError,
        AggregationRegistrationError,
    )
    assert issubclass(
        DuplicateAggregationError,
        AggregationRegistrationError,
    )
    assert issubclass(
        UnsupportedAggregationTypeError,
        AggregationValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (AggregationError, "base"),
        (AggregationValidationError, "validation"),
        (AggregationRegistrationError, "registration"),
        (AggregationNotFoundError, "missing"),
        (DuplicateAggregationError, "duplicate"),
        (UnsupportedAggregationTypeError, "type"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)