"""
Unit tests for ai_api.base.exceptions.
"""

from __future__ import annotations

import pytest

from ai_api.base.exceptions import (
    APIError,
    ConfigurationError,
    InvalidAPIVersionError,
    InvalidRouteError,
    RouteAlreadyExistsError,
    UnsupportedHTTPMethodError,
)


def test_api_error_default_message() -> None:
    """Test APIError with the default message."""
    error = APIError()

    assert str(error) == "An API error occurred."


def test_api_error_custom_message() -> None:
    """Test APIError with a custom message."""
    error = APIError("Custom API error.")

    assert str(error) == "Custom API error."


def test_configuration_error_default_message() -> None:
    """Test ConfigurationError with the default message."""
    error = ConfigurationError()

    assert isinstance(error, APIError)
    assert str(error) == "Invalid API configuration."


def test_configuration_error_custom_message() -> None:
    """Test ConfigurationError with a custom message."""
    error = ConfigurationError("Configuration file missing.")

    assert isinstance(error, APIError)
    assert str(error) == "Configuration file missing."


def test_invalid_route_error() -> None:
    """Test InvalidRouteError."""
    route = "/users"

    error = InvalidRouteError(route)

    assert isinstance(error, APIError)
    assert error.route == route
    assert str(error) == f"Invalid API route: '{route}'."


def test_route_already_exists_error() -> None:
    """Test RouteAlreadyExistsError."""
    route = "/users"

    error = RouteAlreadyExistsError(route)

    assert isinstance(error, APIError)
    assert error.route == route
    assert str(error) == f"Route already exists: '{route}'."


@pytest.mark.parametrize(
    ("method", "expected"),
    [
        ("GET", "GET"),
        ("get", "GET"),
        ("Post", "POST"),
    ],
)
def test_unsupported_http_method_error(
    method: str,
    expected: str,
) -> None:
    """Test UnsupportedHTTPMethodError."""
    error = UnsupportedHTTPMethodError(method)

    assert isinstance(error, APIError)
    assert error.method == expected
    assert str(error) == f"Unsupported HTTP method: '{expected}'."


def test_invalid_api_version_error_default() -> None:
    """Test InvalidAPIVersionError with the default message."""
    error = InvalidAPIVersionError()

    assert isinstance(error, APIError)
    assert error.version == ""
    assert str(error) == "API version cannot be empty."


@pytest.mark.parametrize(
    "version",
    [
        "v0",
        "v1",
        "v2",
        "v10",
        "invalid",
    ],
)
def test_invalid_api_version_error(version: str) -> None:
    """Test InvalidAPIVersionError with a supplied version."""
    error = InvalidAPIVersionError(version)

    assert isinstance(error, APIError)
    assert error.version == version
    assert str(error) == f"Invalid API version: '{version}'."
