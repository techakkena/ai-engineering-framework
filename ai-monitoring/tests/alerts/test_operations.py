"""
Unit tests for ai_monitoring.alerts.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.alerts.constants import (
    OPEN,
    WARNING,
)
from ai_monitoring.alerts.exceptions import (
    AlertValidationError,
)
from ai_monitoring.alerts.operations import (
    AlertResult,
    acknowledge_alert,
    create_alert,
    get_alert,
    list_alerts,
    resolve_alert,
)


def test_create_alert_success() -> None:
    """Creating an alert should succeed."""
    result = create_alert("High CPU usage")

    assert isinstance(result, AlertResult)
    assert result.success is True
    assert result.task == "create_alert"
    assert result.data["severity"] == WARNING
    assert result.data["status"] == OPEN


def test_create_alert_empty_title() -> None:
    """Empty alert titles should raise."""
    with pytest.raises(AlertValidationError):
        create_alert("")


def test_acknowledge_alert_success() -> None:
    """Acknowledging an alert should succeed."""
    result = acknowledge_alert("alert-001")

    assert result.success is True
    assert result.task == "acknowledge_alert"


def test_resolve_alert_success() -> None:
    """Resolving an alert should succeed."""
    result = resolve_alert("alert-001")

    assert result.success is True
    assert result.task == "resolve_alert"


def test_get_alert_success() -> None:
    """Retrieving an alert should succeed."""
    result = get_alert("alert-001")

    assert result.success is True
    assert result.task == "get_alert"


def test_list_alerts_success() -> None:
    """Listing alerts should succeed."""
    result = list_alerts()

    assert result.success is True
    assert result.task == "list_alerts"
    assert isinstance(result.data["alerts"], list)


@pytest.mark.parametrize(
    "operation",
    [
        acknowledge_alert,
        resolve_alert,
        get_alert,
    ],
)
def test_alert_id_validation(
    operation,
) -> None:
    """Operations requiring an alert ID should reject empty values."""
    with pytest.raises(AlertValidationError):
        operation("")