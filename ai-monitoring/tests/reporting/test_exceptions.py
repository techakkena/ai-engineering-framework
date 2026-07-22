"""
Unit tests for ai_monitoring.reporting.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.reporting.exceptions import (
    ReportGenerationError,
    ReportNotFoundError,
    ReportValidationError,
    ReportingConfigurationError,
    ReportingError,
    ReportingProviderError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        ReportValidationError,
        ReportNotFoundError,
        ReportGenerationError,
        ReportingConfigurationError,
        ReportingProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[ReportingError],
) -> None:
    """Every custom exception should inherit from ReportingError."""
    assert issubclass(
        exception_class,
        ReportingError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        ReportingError,
        match="reporting failure",
    ):
        raise ReportingError(
            "reporting failure",
        )