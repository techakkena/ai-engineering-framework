"""
Unit tests for ai_api.routes.constants.
"""

from __future__ import annotations

from ai_api.routes.constants import (
    API_TAG,
    AUTH_TAG,
    DEFAULT_ROUTE_NAME,
    DEFAULT_ROUTE_PREFIX,
    DEFAULT_TAG,
    DYNAMIC_PARAMETER_END,
    DYNAMIC_PARAMETER_PATTERN,
    DYNAMIC_PARAMETER_START,
    HEALTH_TAG,
    MAX_ROUTE_LENGTH,
    MIN_ROUTE_LENGTH,
    NAME_SEPARATOR,
    PATH_SEPARATOR,
    RESERVED_ROUTE_NAMES,
)


def test_default_route_prefix() -> None:
    """Test the default route prefix."""
    assert DEFAULT_ROUTE_PREFIX == "/"


def test_default_route_name() -> None:
    """Test the default route name."""
    assert DEFAULT_ROUTE_NAME == "root"


def test_default_tag() -> None:
    """Test the default tag."""
    assert DEFAULT_TAG == "default"


def test_max_route_length() -> None:
    """Test the maximum route length."""
    assert MAX_ROUTE_LENGTH == 256


def test_min_route_length() -> None:
    """Test the minimum route length."""
    assert MIN_ROUTE_LENGTH == 1


def test_dynamic_parameter_start() -> None:
    """Test the dynamic parameter opening character."""
    assert DYNAMIC_PARAMETER_START == "{"


def test_dynamic_parameter_end() -> None:
    """Test the dynamic parameter closing character."""
    assert DYNAMIC_PARAMETER_END == "}"


def test_dynamic_parameter_pattern() -> None:
    """Test the dynamic parameter regex pattern."""
    assert DYNAMIC_PARAMETER_PATTERN == (
        r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}"
    )


def test_reserved_route_names() -> None:
    """Test reserved route names."""
    assert "docs" in RESERVED_ROUTE_NAMES
    assert "redoc" in RESERVED_ROUTE_NAMES
    assert "openapi" in RESERVED_ROUTE_NAMES
    assert "health" in RESERVED_ROUTE_NAMES


def test_reserved_route_names_is_frozenset() -> None:
    """Reserved route names should be immutable."""
    assert isinstance(
        RESERVED_ROUTE_NAMES,
        frozenset,
    )


def test_path_separator() -> None:
    """Test the path separator."""
    assert PATH_SEPARATOR == "/"


def test_name_separator() -> None:
    """Test the name separator."""
    assert NAME_SEPARATOR == "_"


def test_common_tags() -> None:
    """Test predefined tags."""
    assert API_TAG == "api"
    assert AUTH_TAG == "auth"
    assert HEALTH_TAG == "health"