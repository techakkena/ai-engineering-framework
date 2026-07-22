"""
Unit tests for ai_monitoring.telemetry.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.telemetry.exceptions import (
    TelemetryValidationError,
)
from ai_monitoring.telemetry.operations import (
    TelemetryResult,
    collect_telemetry,
    export_telemetry,
    get_telemetry,
    list_telemetry,
    reset_telemetry,
)


def test_collect_telemetry_success() -> None:
    """Collecting telemetry should succeed."""
    result = collect_telemetry("request-001")

    assert isinstance(result, TelemetryResult)
    assert result.success is True
    assert result.task == "collect_telemetry"


def test_collect_telemetry_empty_name() -> None:
    """Empty telemetry identifiers should raise."""
    with pytest.raises(TelemetryValidationError):
        collect_telemetry("")


def test_get_telemetry_success() -> None:
    """Retrieving telemetry should succeed."""
    result = get_telemetry("request-001")

    assert result.success is True
    assert result.task == "get_telemetry"


def test_export_telemetry_success() -> None:
    """Exporting telemetry should succeed."""
    result = export_telemetry("request-001")

    assert result.success is True
    assert result.task == "export_telemetry"


def test_list_telemetry_success() -> None:
    """Listing telemetry should succeed."""
    result = list_telemetry()

    assert result.success is True
    assert result.task == "list_telemetry"
    assert isinstance(result.data["telemetry"], list)


def test_reset_telemetry_success() -> None:
    """Resetting telemetry should succeed."""
    result = reset_telemetry()

    assert result.success is True
    assert result.task == "reset_telemetry"
    assert result.data["reset"] is True


@pytest.mark.parametrize(
    "operation",
    [
        collect_telemetry,
        get_telemetry,
        export_telemetry,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """Operations requiring a telemetry identifier should reject empty values."""
    with pytest.raises(TelemetryValidationError):
        operation("")