"""
Unit tests for ai_runtime.context.exceptions.
"""

from __future__ import annotations

import pytest

from ai_runtime.context.exceptions import (
    ContextConfigurationError,
    ContextError,
    ContextValidationError,
    InvalidContextScopeError,
)


def test_context_error_default_message() -> None:
    """Test ContextError default message."""
    error = ContextError()

    assert str(error) == "A context error occurred."


def test_context_error_custom_message() -> None:
    """Test ContextError custom message."""
    error = ContextError("Custom context error.")

    assert str(error) == "Custom context error."


@pytest.mark.parametrize(
    "scope",
    [
        "",
        "runtime",
        "thread",
    ],
)
def test_invalid_context_scope_error(
    scope: str,
) -> None:
    """Test InvalidContextScopeError."""
    error = InvalidContextScopeError(scope)

    assert isinstance(error, ContextError)
    assert error.scope == scope
    assert (
        str(error)
        == f"Invalid context scope: '{scope}'."
    )


def test_context_configuration_error() -> None:
    """Test ContextConfigurationError."""
    configuration = "timeout"

    error = ContextConfigurationError(
        configuration,
    )

    assert isinstance(error, ContextError)
    assert error.configuration == configuration
    assert (
        str(error)
        == (
            "Invalid context configuration: "
            f"'{configuration}'."
        )
    )


def test_context_validation_error() -> None:
    """Test ContextValidationError."""
    context = "request-context"
    reason = "expired"

    error = ContextValidationError(
        context,
        reason,
    )

    assert isinstance(error, ContextError)
    assert error.context == context
    assert error.reason == reason
    assert (
        str(error)
        == (
            f"Context '{context}' "
            f"validation failed: {reason}."
        )
    )