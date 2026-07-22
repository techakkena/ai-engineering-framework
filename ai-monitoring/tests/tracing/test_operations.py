"""
Unit tests for ai_monitoring.tracing.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.tracing.exceptions import (
    TraceValidationError,
)
from ai_monitoring.tracing.operations import (
    TraceResult,
    end_trace,
    get_trace,
    list_traces,
    record_span,
    start_trace,
)


def test_start_trace_success() -> None:
    """Starting a trace should succeed."""
    result = start_trace("trace-001")

    assert isinstance(result, TraceResult)
    assert result.success is True
    assert result.task == "start_trace"


def test_start_trace_empty_trace_id() -> None:
    """Empty trace identifiers should raise."""
    with pytest.raises(TraceValidationError):
        start_trace("")


def test_record_span_success() -> None:
    """Recording a span should succeed."""
    result = record_span(
        "trace-001",
        "llm-call",
    )

    assert result.success is True
    assert result.task == "record_span"


def test_record_span_empty_span_name() -> None:
    """Empty span names should raise."""
    with pytest.raises(TraceValidationError):
        record_span(
            "trace-001",
            "",
        )


def test_end_trace_success() -> None:
    """Ending a trace should succeed."""
    result = end_trace("trace-001")

    assert result.success is True
    assert result.task == "end_trace"


def test_get_trace_success() -> None:
    """Retrieving a trace should succeed."""
    result = get_trace("trace-001")

    assert result.success is True
    assert result.task == "get_trace"


def test_list_traces_success() -> None:
    """Listing traces should succeed."""
    result = list_traces()

    assert result.success is True
    assert result.task == "list_traces"
    assert isinstance(
        result.data["traces"],
        list,
    )


@pytest.mark.parametrize(
    "operation",
    [
        start_trace,
        end_trace,
        get_trace,
    ],
)
def test_trace_id_validation(
    operation,
) -> None:
    """Operations requiring a trace identifier should reject empty values."""
    with pytest.raises(TraceValidationError):
        operation("")


def test_record_span_empty_trace_id() -> None:
    """Recording a span with an empty trace identifier should raise."""
    with pytest.raises(TraceValidationError):
        record_span(
            "",
            "llm-call",
        )