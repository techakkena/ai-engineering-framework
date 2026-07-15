"""
Unit tests for ai_api.base.exceptions.
"""

from __future__ import annotations

from ai_api.base.exceptions import (
    APIError,
    ConfigurationError,
    InvalidAPIVersionError,
    InvalidRouteError,
    RouteAlreadyExistsError,
    UnsupportedHTTPMethodError,
)


def test_api_error() -> None:
    error = APIError("Something went wrong")

    assert str(error) == "Something went wrong"


def test_configuration_error() -> None:
    error = ConfigurationError("Invalid configuration")

    assert isinstance(error, APIError)
    assert str(error) == "Invalid configuration"


def test_invalid_route_error() -> None:
    error = InvalidRouteError("/users")

    assert isinstance(error, APIError)
    assert "/users" in str(error)


def test_route_already_exists_error() -> None:
    error = RouteAlreadyExistsError("/users")

    assert isinstance(error, APIError)
    assert "/users" in str(error)


def test_invalid_api_version_error() -> None:
    error = InvalidAPIVersionError("vX")

    assert isinstance(error, APIError)
    assert "vX" in str(error)


def test_unsupported_http_method_error() -> None:
    error = UnsupportedHTTPMethodError("TRACE")

    assert isinstance(error, APIError)
    assert "TRACE" in str(error)
