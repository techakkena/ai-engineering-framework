"""
Unit tests for ai_runtime.lifecycle.exceptions.
"""

from __future__ import annotations

import pytest

from ai_runtime.lifecycle.exceptions import (
    InvalidLifecyclePhaseError,
    LifecycleConfigurationError,
    LifecycleError,
    LifecycleValidationError,
)


def test_lifecycle_error_default_message() -> None:
    """Test LifecycleError default message."""
    error = LifecycleError()

    assert str(error) == "A lifecycle error occurred."


def test_lifecycle_error_custom_message() -> None:
    """Test LifecycleError custom message."""
    error = LifecycleError(
        "Custom lifecycle error.",
    )

    assert str(error) == "Custom lifecycle error."


@pytest.mark.parametrize(
    "phase",
    [
        "",
        "booting",
        "restarting",
    ],
)
def test_invalid_lifecycle_phase_error(
    phase: str,
) -> None:
    """Test InvalidLifecyclePhaseError."""
    error = InvalidLifecyclePhaseError(
        phase,
    )

    assert isinstance(
        error,
        LifecycleError,
    )

    assert error.phase == phase

    assert (
        str(error)
        == f"Invalid lifecycle phase: '{phase}'."
    )


def test_lifecycle_configuration_error() -> None:
    """Test LifecycleConfigurationError."""
    configuration = "startup_timeout"

    error = LifecycleConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        LifecycleError,
    )

    assert error.configuration == configuration

    assert (
        str(error)
        == (
            "Invalid lifecycle configuration: "
            f"'{configuration}'."
        )
    )


def test_lifecycle_validation_error() -> None:
    """Test LifecycleValidationError."""
    lifecycle = "runtime"
    reason = "already terminated"

    error = LifecycleValidationError(
        lifecycle,
        reason,
    )

    assert isinstance(
        error,
        LifecycleError,
    )

    assert error.lifecycle == lifecycle
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Lifecycle '{lifecycle}' "
            f"validation failed: {reason}."
        )
    )