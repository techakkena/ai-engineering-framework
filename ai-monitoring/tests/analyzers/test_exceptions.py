"""
Unit tests for ai_monitoring.analyzers.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.analyzers.exceptions import (
    AnalysisExecutionError,
    AnalysisNotFoundError,
    AnalyzerConfigurationError,
    AnalyzerError,
    AnalyzerProviderError,
    AnalyzerValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        AnalyzerValidationError,
        AnalysisNotFoundError,
        AnalysisExecutionError,
        AnalyzerConfigurationError,
        AnalyzerProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[AnalyzerError],
) -> None:
    """Every custom exception should inherit from AnalyzerError."""
    assert issubclass(
        exception_class,
        AnalyzerError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        AnalyzerError,
        match="analysis failure",
    ):
        raise AnalyzerError(
            "analysis failure",
        )