from ai_observability.tracing.operations import (
    Span,
    TraceManager,
)


def test_create_trace() -> None:
    manager = TraceManager()

    trace = manager.create_trace(
        "trace-1",
    )

    assert trace.trace_id == "trace-1"
    assert manager.trace_count == 1


def test_add_span() -> None:
    manager = TraceManager()

    manager.create_trace(
        "trace-1",
    )

    manager.add_span(
        "trace-1",
        Span(
            name="llm_call",
        ),
    )

    trace = manager.get_trace(
        "trace-1",
    )

    assert trace is not None
    assert len(trace.spans) == 1
    assert trace.spans[0].name == "llm_call"


def test_unknown_trace() -> None:
    manager = TraceManager()

    assert (
        manager.get_trace(
            "missing",
        )
        is None
    )
