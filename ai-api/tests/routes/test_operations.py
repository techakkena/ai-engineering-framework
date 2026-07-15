"""
Unit tests for ai_api.routes.operations.
"""

from __future__ import annotations

import pytest

from ai_api.routes.constants import MAX_ROUTE_LENGTH
from ai_api.routes.exceptions import (
    InvalidRouteNameError,
    InvalidRouteParameterError,
    InvalidRoutePathError,
    ReservedRouteNameError,
    RouteLengthExceededError,
)
from ai_api.routes.operations import (
    build_route_name,
    extract_route_parameters,
    is_dynamic_route,
    is_reserved_route_name,
    normalize_route_path,
    validate_route_name,
    validate_route_parameter,
    validate_route_path,
)


# ============================================================================
# normalize_route_path
# ============================================================================


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("", "/"),
        ("/", "/"),
        ("users", "/users"),
        ("/users", "/users"),
        ("//users//", "/users"),
        ("users/profile", "/users/profile"),
        ("/users/profile/", "/users/profile"),
        ("///users///profile///", "/users/profile"),
    ],
)
def test_normalize_route_path(
    path: str,
    expected: str,
) -> None:
    """Test route path normalization."""
    assert normalize_route_path(path) == expected


# ============================================================================
# validate_route_path
# ============================================================================


def test_validate_route_path() -> None:
    """Test valid route path."""
    assert validate_route_path("/users") == "/users"


def test_validate_route_path_with_spaces() -> None:
    """Route containing spaces should fail."""
    with pytest.raises(InvalidRoutePathError):
        validate_route_path("/user profile")


def test_validate_route_path_length() -> None:
    """Route exceeding maximum length should fail."""
    path = "/" + ("a" * MAX_ROUTE_LENGTH)

    with pytest.raises(RouteLengthExceededError):
        validate_route_path(path)


# ============================================================================
# validate_route_name
# ============================================================================


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("users", "users"),
        ("Users", "users"),
        ("get_users", "get_users"),
        ("USER123", "user123"),
    ],
)
def test_validate_route_name(
    name: str,
    expected: str,
) -> None:
    """Test valid route names."""
    assert validate_route_name(name) == expected


@pytest.mark.parametrize(
    "name",
    [
        "",
        "123users",
        "user-name",
        "user name",
        "@users",
    ],
)
def test_validate_route_name_invalid(
    name: str,
) -> None:
    """Invalid route names should raise."""
    with pytest.raises(InvalidRouteNameError):
        validate_route_name(name)


def test_validate_route_name_reserved() -> None:
    """Reserved route names should fail."""
    with pytest.raises(ReservedRouteNameError):
        validate_route_name("docs")


# ============================================================================
# build_route_name
# ============================================================================


@pytest.mark.parametrize(
    ("method", "path", "expected"),
    [
        ("GET", "/users", "get_users"),
        ("POST", "/users/profile", "post_users_profile"),
        ("DELETE", "/", "delete"),
        ("PATCH", "/users/{id}", "patch_users_{id}"),
    ],
)
def test_build_route_name(
    method: str,
    path: str,
    expected: str,
) -> None:
    """Test route name generation."""
    assert build_route_name(method, path) == expected


# ============================================================================
# extract_route_parameters
# ============================================================================


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("/users", []),
        ("/users/{id}", ["id"]),
        (
            "/users/{user_id}/posts/{post_id}",
            ["user_id", "post_id"],
        ),
        (
            "/{version}/users/{id}",
            ["version", "id"],
        ),
    ],
)
def test_extract_route_parameters(
    path: str,
    expected: list[str],
) -> None:
    """Test parameter extraction."""
    assert extract_route_parameters(path) == expected


# ============================================================================
# is_dynamic_route
# ============================================================================


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("/users", False),
        ("/users/{id}", True),
        ("/users/{user_id}/posts/{post_id}", True),
    ],
)
def test_is_dynamic_route(
    path: str,
    expected: bool,
) -> None:
    """Test dynamic route detection."""
    assert is_dynamic_route(path) is expected


# ============================================================================
# is_reserved_route_name
# ============================================================================


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("docs", True),
        ("redoc", True),
        ("openapi", True),
        ("health", True),
        ("users", False),
        ("profile", False),
    ],
)
def test_is_reserved_route_name(
    name: str,
    expected: bool,
) -> None:
    """Test reserved route detection."""
    assert is_reserved_route_name(name) is expected


# ============================================================================
# validate_route_parameter
# ============================================================================


@pytest.mark.parametrize(
    ("parameter", "expected"),
    [
        ("id", "id"),
        ("user_id", "user_id"),
        ("_value", "_value"),
        ("User123", "User123"),
    ],
)
def test_validate_route_parameter(
    parameter: str,
    expected: str,
) -> None:
    """Test valid route parameters."""
    assert validate_route_parameter(parameter) == expected


@pytest.mark.parametrize(
    "parameter",
    [
        "",
        "123",
        "user-id",
        "user id",
        "@id",
    ],
)
def test_validate_route_parameter_invalid(
    parameter: str,
) -> None:
    """Invalid parameters should raise."""
    with pytest.raises(InvalidRouteParameterError):
        validate_route_parameter(parameter)