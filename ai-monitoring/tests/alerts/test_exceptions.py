"""
Unit tests for ai_monitoring.alerts.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.alerts.exceptions import (
    AlertConfigurationError,
    AlertCreationError,
    AlertError,
    AlertNotFoundError,
    AlertProviderError,
    AlertResolutionError,
    AlertValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        AlertValidationError,
        AlertNotFoundError,
        AlertCreationError,
        AlertResolutionError,
        AlertConfigurationError,
        AlertProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[AlertError],
) -> None:
    """Every custom exception should inherit from AlertError."""
    assert issubclass(
        exception_class,
        AlertError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        AlertError,
        match="alert failure",
    ):
        raise AlertError(
            "alert failure",
        )