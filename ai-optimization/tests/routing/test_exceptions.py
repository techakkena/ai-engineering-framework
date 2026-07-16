"""Tests for ai_optimization.routing.exceptions."""

from __future__ import annotations

import pytest

from ai_optimization.routing.exceptions import (
    DuplicateRouteError,
    RouteError,
    RouteNotFoundError,
    RouteRegistrationError,
    RouteValidationError,
    UnsupportedRoutingStrategyError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(RouteValidationError, RouteError)
    assert issubclass(RouteRegistrationError, RouteError)
    assert issubclass(
        RouteNotFoundError,
        RouteRegistrationError,
    )
    assert issubclass(
        DuplicateRouteError,
        RouteRegistrationError,
    )
    assert issubclass(
        UnsupportedRoutingStrategyError,
        RouteValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (RouteError, "base"),
        (RouteValidationError, "validation"),
        (RouteRegistrationError, "registration"),
        (RouteNotFoundError, "missing"),
        (DuplicateRouteError, "duplicate"),
        (UnsupportedRoutingStrategyError, "strategy"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)