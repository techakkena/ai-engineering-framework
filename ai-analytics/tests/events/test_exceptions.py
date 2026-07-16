"""Tests for ai_analytics.events.exceptions."""

from __future__ import annotations

import pytest

from ai_analytics.events.exceptions import (
    DuplicateEventError,
    EventError,
    EventNotFoundError,
    EventRegistrationError,
    EventValidationError,
    UnsupportedEventTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(EventValidationError, EventError)
    assert issubclass(EventRegistrationError, EventError)
    assert issubclass(EventNotFoundError, EventRegistrationError)
    assert issubclass(DuplicateEventError, EventRegistrationError)
    assert issubclass(
        UnsupportedEventTypeError,
        EventValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (EventError, "base"),
        (EventValidationError, "validation"),
        (EventRegistrationError, "registration"),
        (EventNotFoundError, "missing"),
        (DuplicateEventError, "duplicate"),
        (UnsupportedEventTypeError, "type"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)