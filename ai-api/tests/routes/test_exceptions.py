"""
Unit tests for ai_api.routes.exceptions.
"""

from __future__ import annotations

import pytest

from ai_api.routes.exceptions import (
    DuplicateRouteNameError,
    DuplicateRoutePathError,
    InvalidRouteNameError,
    InvalidRouteParameterError,
    InvalidRoutePathError,
    ReservedRouteNameError,
    RouteError,
    RouteLengthExceededError,
)


def test_route_error_default_message() -> None:
    """Test RouteError with the default message."""
    error = RouteError()

    assert str(error) == "A route error occurred."


def test_route_error_custom_message() -> None:
    """Test RouteError with a custom message."""
    error = RouteError("Custom route error.")

    assert str(error) == "Custom route error."


@pytest.mark.parametrize(
    "name",
    [
        "",
        "123route",
        "Invalid Route",
        "route-name",
    ],
)
def test_invalid_route_name_error(name: str) -> None:
    """Test InvalidRouteNameError."""
    error = InvalidRouteNameError(name)

    assert isinstance(error, RouteError)
    assert error.name == name
    assert str(error) == f"Invalid route name: '{name}'."


def test_duplicate_route_name_error() -> None:
    """Test DuplicateRouteNameError."""
    name = "users"

    error = DuplicateRouteNameError(name)

    assert isinstance(error, RouteError)
    assert error.name == name
    assert str(error) == f"Route name already exists: '{name}'."


def test_duplicate_route_path_error() -> None:
    """Test DuplicateRoutePathError."""
    path = "/users"

    error = DuplicateRoutePathError(path)

    assert isinstance(error, RouteError)
    assert error.path == path
    assert str(error) == f"Route path already exists: '{path}'."


@pytest.mark.parametrize(
    "parameter",
    [
        "",
        "123",
        "user-id",
        "user id",
    ],
)
def test_invalid_route_parameter_error(
    parameter: str,
) -> None:
    """Test InvalidRouteParameterError."""
    error = InvalidRouteParameterError(parameter)

    assert isinstance(error, RouteError)
    assert error.parameter == parameter
    assert (
        str(error)
        == f"Invalid route parameter: '{parameter}'."
    )


def test_invalid_route_path_error() -> None:
    """Test InvalidRoutePathError."""
    path = "/invalid path"

    error = InvalidRoutePathError(path)

    assert isinstance(error, RouteError)
    assert error.path == path
    assert str(error) == f"Invalid route path: '{path}'."


def test_reserved_route_name_error() -> None:
    """Test ReservedRouteNameError."""
    name = "docs"

    error = ReservedRouteNameError(name)

    assert isinstance(error, RouteError)
    assert error.name == name
    assert (
        str(error)
        == f"Reserved route name cannot be used: '{name}'."
    )


def test_route_length_exceeded_error() -> None:
    """Test RouteLengthExceededError."""
    error = RouteLengthExceededError(300, 256)

    assert isinstance(error, RouteError)
    assert error.length == 300
    assert error.maximum == 256
    assert (
        str(error)
        == "Route length (300) exceeds maximum allowed (256)."
    )