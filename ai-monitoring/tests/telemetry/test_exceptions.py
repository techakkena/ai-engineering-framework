"""
Unit tests for ai_monitoring.telemetry.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.telemetry.exceptions import (
    TelemetryCollectionError,
    TelemetryConfigurationError,
    TelemetryError,
    TelemetryExportError,
    TelemetryNotFoundError,
    TelemetryProviderError,
    TelemetryValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        TelemetryValidationError,
        TelemetryNotFoundError,
        TelemetryCollectionError,
        TelemetryExportError,
        TelemetryConfigurationError,
        TelemetryProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[TelemetryError],
) -> None:
    """Every custom exception should inherit from TelemetryError."""
    assert issubclass(
        exception_class,
        TelemetryError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        TelemetryError,
        match="telemetry failure",
    ):
        raise TelemetryError(
            "telemetry failure",
        )