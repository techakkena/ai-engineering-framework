"""
Unit tests for ai_monitoring.dashboards.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.dashboards.constants import CUSTOM
from ai_monitoring.dashboards.exceptions import (
    DashboardValidationError,
)
from ai_monitoring.dashboards.operations import (
    DashboardResult,
    create_dashboard,
    delete_dashboard,
    get_dashboard,
    list_dashboards,
    update_dashboard,
)


def test_create_dashboard_success() -> None:
    """Creating a dashboard should succeed."""
    result = create_dashboard("Operations Dashboard")

    assert isinstance(result, DashboardResult)
    assert result.success is True
    assert result.task == "create_dashboard"
    assert result.data["type"] == CUSTOM


def test_create_dashboard_empty_name() -> None:
    """Empty dashboard names should raise."""
    with pytest.raises(DashboardValidationError):
        create_dashboard("")


def test_get_dashboard_success() -> None:
    """Getting a dashboard should succeed."""
    result = get_dashboard("Operations Dashboard")

    assert result.success is True
    assert result.task == "get_dashboard"


def test_update_dashboard_success() -> None:
    """Updating a dashboard should succeed."""
    result = update_dashboard("Operations Dashboard")

    assert result.success is True
    assert result.task == "update_dashboard"


def test_delete_dashboard_success() -> None:
    """Deleting a dashboard should succeed."""
    result = delete_dashboard("Operations Dashboard")

    assert result.success is True
    assert result.task == "delete_dashboard"


def test_list_dashboards_success() -> None:
    """Listing dashboards should succeed."""
    result = list_dashboards()

    assert result.success is True
    assert result.task == "list_dashboards"
    assert isinstance(result.data["dashboards"], list)


@pytest.mark.parametrize(
    "operation",
    [
        get_dashboard,
        update_dashboard,
        delete_dashboard,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """Operations requiring a dashboard name should reject empty values."""
    with pytest.raises(DashboardValidationError):
        operation("")