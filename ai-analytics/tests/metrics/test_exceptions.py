"""Tests for ai_analytics.metrics.exceptions."""

from __future__ import annotations

import pytest

from ai_analytics.metrics.exceptions import (
    DuplicateMetricError,
    MetricError,
    MetricNotFoundError,
    MetricRegistrationError,
    MetricValidationError,
    UnsupportedMetricTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(MetricValidationError, MetricError)
    assert issubclass(MetricRegistrationError, MetricError)
    assert issubclass(MetricNotFoundError, MetricRegistrationError)
    assert issubclass(DuplicateMetricError, MetricRegistrationError)
    assert issubclass(
        UnsupportedMetricTypeError,
        MetricValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (MetricError, "base"),
        (MetricValidationError, "validation"),
        (MetricRegistrationError, "registration"),
        (MetricNotFoundError, "missing"),
        (DuplicateMetricError, "duplicate"),
        (UnsupportedMetricTypeError, "type"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)