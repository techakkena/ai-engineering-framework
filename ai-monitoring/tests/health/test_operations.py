"""
Unit tests for ai_monitoring.health.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.health.constants import HEALTHY
from ai_monitoring.health.exceptions import (
    HealthValidationError,
)
from ai_monitoring.health.operations import (
    HealthResult,
    check_health,
    get_health_status,
    list_health_checks,
    register_health_check,
    run_health_checks,
)


def test_register_health_check_success() -> None:
    """Health check registration should succeed."""
    result = register_health_check("database")

    assert isinstance(result, HealthResult)
    assert result.success is True
    assert result.task == "register_health_check"


def test_register_health_check_empty_name() -> None:
    """Empty health check names should raise."""
    with pytest.raises(HealthValidationError):
        register_health_check("")


def test_check_health_success() -> None:
    """Running a health check should succeed."""
    result = check_health("database")

    assert result.success is True
    assert result.task == "check_health"
    assert result.data["status"] == HEALTHY


def test_get_health_status_success() -> None:
    """Getting health status should succeed."""
    result = get_health_status("database")

    assert result.success is True
    assert result.task == "get_health_status"
    assert result.data["status"] == HEALTHY


def test_run_health_checks_success() -> None:
    """Running all health checks should succeed."""
    result = run_health_checks()

    assert result.success is True
    assert result.task == "run_health_checks"
    assert isinstance(result.data["checks"], list)


def test_list_health_checks_success() -> None:
    """Listing health checks should succeed."""
    result = list_health_checks()

    assert result.success is True
    assert result.task == "list_health_checks"
    assert isinstance(result.data["checks"], list)


@pytest.mark.parametrize(
    "operation",
    [
        register_health_check,
        check_health,
        get_health_status,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """Operations requiring a health check name should reject empty values."""
    with pytest.raises(HealthValidationError):
        operation("")