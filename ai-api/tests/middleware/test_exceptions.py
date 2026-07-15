"""
Unit tests for ai_api.middleware.exceptions.
"""

from __future__ import annotations

import pytest

from ai_api.middleware.exceptions import (
    DuplicateMiddlewareError,
    InvalidMiddlewareConfigurationError,
    InvalidMiddlewareTypeError,
    MiddlewareError,
    MiddlewareExecutionError,
    MiddlewareNotFoundError,
    MiddlewarePriorityError,
)


def test_middleware_error_default_message() -> None:
    """Test MiddlewareError with the default message."""
    error = MiddlewareError()

    assert str(error) == "A middleware error occurred."


def test_middleware_error_custom_message() -> None:
    """Test MiddlewareError with a custom message."""
    error = MiddlewareError("Custom middleware error.")

    assert str(error) == "Custom middleware error."


@pytest.mark.parametrize(
    "configuration",
    [
        "",
        "missing_config",
        "invalid_timeout",
    ],
)
def test_invalid_middleware_configuration_error(
    configuration: str,
) -> None:
    """Test InvalidMiddlewareConfigurationError."""
    error = InvalidMiddlewareConfigurationError(configuration)

    assert isinstance(error, MiddlewareError)
    assert error.configuration == configuration
    assert (
        str(error)
        == f"Invalid middleware configuration: '{configuration}'."
    )


@pytest.mark.parametrize(
    "middleware_type",
    [
        "unknown",
        "invalid",
        "unsupported",
    ],
)
def test_invalid_middleware_type_error(
    middleware_type: str,
) -> None:
    """Test InvalidMiddlewareTypeError."""
    error = InvalidMiddlewareTypeError(middleware_type)

    assert isinstance(error, MiddlewareError)
    assert error.middleware_type == middleware_type
    assert (
        str(error)
        == f"Unsupported middleware type: '{middleware_type}'."
    )


def test_duplicate_middleware_error() -> None:
    """Test DuplicateMiddlewareError."""
    name = "logging"

    error = DuplicateMiddlewareError(name)

    assert isinstance(error, MiddlewareError)
    assert error.name == name
    assert (
        str(error)
        == f"Middleware '{name}' is already registered."
    )


def test_middleware_not_found_error() -> None:
    """Test MiddlewareNotFoundError."""
    name = "authentication"

    error = MiddlewareNotFoundError(name)

    assert isinstance(error, MiddlewareError)
    assert error.name == name
    assert (
        str(error)
        == f"Middleware '{name}' was not found."
    )


def test_middleware_execution_error() -> None:
    """Test MiddlewareExecutionError."""
    name = "logging"
    reason = "Unhandled exception"

    error = MiddlewareExecutionError(name, reason)

    assert isinstance(error, MiddlewareError)
    assert error.name == name
    assert error.reason == reason
    assert (
        str(error)
        == f"Middleware '{name}' execution failed: {reason}."
    )


@pytest.mark.parametrize(
    "priority",
    [
        -1,
        -10,
        999,
    ],
)
def test_middleware_priority_error(
    priority: int,
) -> None:
    """Test MiddlewarePriorityError."""
    error = MiddlewarePriorityError(priority)

    assert isinstance(error, MiddlewareError)
    assert error.priority == priority
    assert (
        str(error)
        == f"Invalid middleware priority: {priority}."
    )