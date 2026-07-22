"""
Unit tests for ai_monitoring.health.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.health.exceptions import (
    HealthCheckError,
    HealthCheckNotFoundError,
    HealthConfigurationError,
    HealthError,
    HealthProviderError,
    HealthValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        HealthValidationError,
        HealthCheckNotFoundError,
        HealthCheckError,
        HealthConfigurationError,
        HealthProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[HealthError],
) -> None:
    """Every custom exception should inherit from HealthError."""
    assert issubclass(
        exception_class,
        HealthError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        HealthError,
        match="health failure",
    ):
        raise HealthError(
            "health failure",
        )