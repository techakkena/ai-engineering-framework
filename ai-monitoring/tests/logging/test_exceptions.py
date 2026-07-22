"""
Unit tests for ai_monitoring.logging.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.logging.exceptions import (
    LoggingError,
    LoggingConfigurationError,
    LoggingProviderError,
    LogNotFoundError,
    LogReadError,
    LogValidationError,
    LogWriteError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        LogValidationError,
        LogNotFoundError,
        LogWriteError,
        LogReadError,
        LoggingConfigurationError,
        LoggingProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[LoggingError],
) -> None:
    """Every custom exception should inherit from LoggingError."""
    assert issubclass(
        exception_class,
        LoggingError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        LoggingError,
        match="logging failure",
    ):
        raise LoggingError(
            "logging failure",
        )