"""
Unit tests for ai_api.middleware.operations.
"""

from __future__ import annotations

import pytest

from ai_api.middleware.exceptions import (
    InvalidMiddlewareConfigurationError,
    InvalidMiddlewareTypeError,
    MiddlewarePriorityError,
)
from ai_api.middleware.operations import (
    build_middleware_name,
    get_middleware_priority,
    is_supported_middleware,
    normalize_middleware_name,
    sort_middlewares,
    validate_configuration,
    validate_middleware_name,
    validate_middleware_type,
)


# ============================================================================
# normalize_middleware_name
# ============================================================================


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Logging", "logging"),
        ("Request ID", "request_id"),
        ("request-id", "request_id"),
        (" Authentication ", "authentication"),
        ("rate_limit", "rate_limit"),
    ],
)
def test_normalize_middleware_name(
    name: str,
    expected: str,
) -> None:
    """Test middleware name normalization."""
    assert normalize_middleware_name(name) == expected


# ============================================================================
# validate_middleware_name
# ============================================================================


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("logging", "logging"),
        ("Request ID", "request_id"),
        ("authentication", "authentication"),
    ],
)
def test_validate_middleware_name(
    name: str,
    expected: str,
) -> None:
    """Test valid middleware names."""
    assert validate_middleware_name(name) == expected


@pytest.mark.parametrize(
    "name",
    [
        "",
        " ",
        "@middleware",
        "middleware!",
        "logging#1",
    ],
)
def test_validate_middleware_name_invalid(
    name: str,
) -> None:
    """Invalid middleware names should raise."""
    with pytest.raises(
        InvalidMiddlewareConfigurationError,
    ):
        validate_middleware_name(name)


# ============================================================================
# validate_middleware_type
# ============================================================================


@pytest.mark.parametrize(
    "middleware_type",
    [
        "logging",
        "authentication",
        "authorization",
        "cors",
        "metrics",
        "compression",
    ],
)
def test_validate_middleware_type(
    middleware_type: str,
) -> None:
    """Test valid middleware types."""
    assert (
        validate_middleware_type(
            middleware_type,
        )
        == middleware_type
    )


@pytest.mark.parametrize(
    "middleware_type",
    [
        "",
        "graphql",
        "soap",
        "invalid",
    ],
)
def test_validate_middleware_type_invalid(
    middleware_type: str,
) -> None:
    """Invalid middleware types should raise."""
    with pytest.raises(
        InvalidMiddlewareTypeError,
    ):
        validate_middleware_type(
            middleware_type,
        )


# ============================================================================
# get_middleware_priority
# ============================================================================


def test_get_middleware_priority() -> None:
    """Test middleware priorities."""
    assert get_middleware_priority("cors") == 10
    assert get_middleware_priority("logging") == 50
    assert get_middleware_priority("authentication") == 70


def test_get_middleware_priority_invalid() -> None:
    """Unknown middleware should raise."""
    with pytest.raises(
        MiddlewarePriorityError,
    ):
        get_middleware_priority("graphql")


# ============================================================================
# build_middleware_name
# ============================================================================


@pytest.mark.parametrize(
    ("middleware_type", "name", "expected"),
    [
        (
            "logging",
            "request",
            "logging_request",
        ),
        (
            "authentication",
            "jwt",
            "authentication_jwt",
        ),
        (
            "cors",
            "default",
            "cors_default",
        ),
    ],
)
def test_build_middleware_name(
    middleware_type: str,
    name: str,
    expected: str,
) -> None:
    """Test middleware name generation."""
    assert (
        build_middleware_name(
            middleware_type,
            name,
        )
        == expected
    )


# ============================================================================
# is_supported_middleware
# ============================================================================


@pytest.mark.parametrize(
    ("middleware_type", "expected"),
    [
        ("logging", True),
        ("cors", True),
        ("metrics", True),
        ("authentication", True),
        ("graphql", False),
        ("soap", False),
    ],
)
def test_is_supported_middleware(
    middleware_type: str,
    expected: bool,
) -> None:
    """Test supported middleware detection."""
    assert (
        is_supported_middleware(
            middleware_type,
        )
        is expected
    )


# ============================================================================
# sort_middlewares
# ============================================================================


def test_sort_middlewares() -> None:
    """Middleware should be sorted by priority."""
    middlewares = [
        "authentication",
        "logging",
        "cors",
    ]

    assert sort_middlewares(
        middlewares,
    ) == [
        "cors",
        "logging",
        "authentication",
    ]


# ============================================================================
# validate_configuration
# ============================================================================


def test_validate_configuration() -> None:
    """Test valid configuration."""
    configuration = {
        "enabled": True,
        "timeout": 30,
    }

    assert (
        validate_configuration(
            configuration,
        )
        == configuration
    )


def test_validate_configuration_invalid() -> None:
    """Empty configuration should raise."""
    with pytest.raises(
        InvalidMiddlewareConfigurationError,
    ):
        validate_configuration({})