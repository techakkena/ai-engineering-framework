"""
Unit tests for ai_monitoring.analyzers.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.analyzers.constants import PERFORMANCE
from ai_monitoring.analyzers.exceptions import (
    AnalyzerValidationError,
)
from ai_monitoring.analyzers.operations import (
    AnalysisResult,
    analyze_data,
    compare_analysis,
    get_analysis,
    list_analyses,
    run_analysis,
)


def test_run_analysis_success() -> None:
    """Running an analysis should succeed."""
    result = run_analysis("system-performance")

    assert isinstance(result, AnalysisResult)
    assert result.success is True
    assert result.task == "run_analysis"
    assert result.data["type"] == PERFORMANCE


def test_run_analysis_empty_name() -> None:
    """Empty analysis names should raise."""
    with pytest.raises(AnalyzerValidationError):
        run_analysis("")


def test_analyze_data_success() -> None:
    """Analyzing monitoring data should succeed."""
    result = analyze_data("system-performance")

    assert result.success is True
    assert result.task == "analyze_data"


def test_get_analysis_success() -> None:
    """Getting an analysis should succeed."""
    result = get_analysis("system-performance")

    assert result.success is True
    assert result.task == "get_analysis"


def test_compare_analysis_success() -> None:
    """Comparing analyses should succeed."""
    result = compare_analysis("system-performance")

    assert result.success is True
    assert result.task == "compare_analysis"


def test_list_analyses_success() -> None:
    """Listing analyses should succeed."""
    result = list_analyses()

    assert result.success is True
    assert result.task == "list_analyses"
    assert isinstance(result.data["analyses"], list)


@pytest.mark.parametrize(
    "operation",
    [
        analyze_data,
        get_analysis,
        compare_analysis,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """Operations requiring an analysis name should reject empty values."""
    with pytest.raises(AnalyzerValidationError):
        operation("")