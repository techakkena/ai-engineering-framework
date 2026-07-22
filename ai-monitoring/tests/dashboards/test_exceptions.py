"""
Unit tests for ai_monitoring.dashboards.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.dashboards.exceptions import (
    DashboardConfigurationError,
    DashboardCreationError,
    DashboardError,
    DashboardNotFoundError,
    DashboardProviderError,
    DashboardUpdateError,
    DashboardValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        DashboardValidationError,
        DashboardNotFoundError,
        DashboardCreationError,
        DashboardUpdateError,
        DashboardConfigurationError,
        DashboardProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DashboardError],
) -> None:
    """Every custom exception should inherit from DashboardError."""
    assert issubclass(
        exception_class,
        DashboardError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DashboardError,
        match="dashboard failure",
    ):
        raise DashboardError(
            "dashboard failure",
        )