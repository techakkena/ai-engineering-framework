"""Tests for ai_analytics.dashboards.exceptions."""

from __future__ import annotations

import pytest

from ai_analytics.dashboards.exceptions import (
    DashboardError,
    DashboardNotFoundError,
    DashboardRegistrationError,
    DashboardValidationError,
    DuplicateDashboardError,
    UnsupportedLayoutError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(DashboardValidationError, DashboardError)
    assert issubclass(
        DashboardRegistrationError,
        DashboardError,
    )
    assert issubclass(
        DashboardNotFoundError,
        DashboardRegistrationError,
    )
    assert issubclass(
        DuplicateDashboardError,
        DashboardRegistrationError,
    )
    assert issubclass(
        UnsupportedLayoutError,
        DashboardValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (DashboardError, "base"),
        (DashboardValidationError, "validation"),
        (DashboardRegistrationError, "registration"),
        (DashboardNotFoundError, "missing"),
        (DuplicateDashboardError, "duplicate"),
        (UnsupportedLayoutError, "layout"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)