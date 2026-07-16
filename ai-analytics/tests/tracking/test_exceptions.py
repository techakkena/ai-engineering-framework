"""Tests for ai_analytics.tracking.exceptions."""

from __future__ import annotations

import pytest

from ai_analytics.tracking.exceptions import (
    DuplicateTrackingError,
    TrackingError,
    TrackingNotFoundError,
    TrackingRegistrationError,
    TrackingValidationError,
    UnsupportedTrackingTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(TrackingValidationError, TrackingError)
    assert issubclass(TrackingRegistrationError, TrackingError)
    assert issubclass(
        TrackingNotFoundError,
        TrackingRegistrationError,
    )
    assert issubclass(
        DuplicateTrackingError,
        TrackingRegistrationError,
    )
    assert issubclass(
        UnsupportedTrackingTypeError,
        TrackingValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (TrackingError, "base"),
        (TrackingValidationError, "validation"),
        (TrackingRegistrationError, "registration"),
        (TrackingNotFoundError, "missing"),
        (DuplicateTrackingError, "duplicate"),
        (UnsupportedTrackingTypeError, "type"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)