"""Tests for ai_cloud.monitoring.exceptions."""

from __future__ import annotations

import pytest

from ai_cloud.monitoring.exceptions import (
    DuplicateMonitoringError,
    MonitoringError,
    MonitoringNotFoundError,
    MonitoringRegistrationError,
    MonitoringValidationError,
    UnsupportedMonitorTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        MonitoringValidationError,
        MonitoringError,
    )
    assert issubclass(
        MonitoringRegistrationError,
        MonitoringError,
    )
    assert issubclass(
        MonitoringNotFoundError,
        MonitoringRegistrationError,
    )
    assert issubclass(
        DuplicateMonitoringError,
        MonitoringRegistrationError,
    )
    assert issubclass(
        UnsupportedMonitorTypeError,
        MonitoringValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (MonitoringError, "base"),
        (MonitoringValidationError, "validation"),
        (MonitoringRegistrationError, "registration"),
        (MonitoringNotFoundError, "missing"),
        (DuplicateMonitoringError, "duplicate"),
        (UnsupportedMonitorTypeError, "monitor"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(
        exception_class,
        match=message,
    ):
        raise exception_class(message)