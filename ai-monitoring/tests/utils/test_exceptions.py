"""
Unit tests for ai_monitoring.utils.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.utils.exceptions import (
    DurationFormatError,
    IdentifierValidationError,
    MetadataBuildError,
    MonitoringUtilsConfigurationError,
    MonitoringUtilsError,
    TimestampFormatError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        IdentifierValidationError,
        MetadataBuildError,
        TimestampFormatError,
        DurationFormatError,
        MonitoringUtilsConfigurationError,
    ],
)
def test_exception_inheritance(
    exception_class: type[MonitoringUtilsError],
) -> None:
    """Every custom exception should inherit from MonitoringUtilsError."""
    assert issubclass(
        exception_class,
        MonitoringUtilsError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        MonitoringUtilsError,
        match="utility failure",
    ):
        raise MonitoringUtilsError(
            "utility failure",
        )