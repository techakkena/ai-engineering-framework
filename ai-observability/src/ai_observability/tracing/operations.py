from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .constants import SpanStatus


@dataclass(slots=True)
class Span:
    """Execution span."""

    name: str

    status: SpanStatus = SpanStatus.CREATED

    attributes: dict[str, Any] = field(
        default_factory=dict,
    )


@dataclass(slots=True)
class Trace:
    """Execution trace."""

    trace_id: str

    spans: list[Span] = field(
        default_factory=list,
    )


class TraceManager:
    """Simple in-memory trace manager."""

    def __init__(self) -> None:
        self._traces: dict[str, Trace] = {}

    def create_trace(
        self,
        trace_id: str,
    ) -> Trace:
        trace = Trace(trace_id)

        self._traces[trace_id] = trace

        return trace

    def add_span(
        self,
        trace_id: str,
        span: Span,
    ) -> None:
        self._traces[trace_id].spans.append(
            span,
        )

    def get_trace(
        self,
        trace_id: str,
    ) -> Trace | None:
        return self._traces.get(trace_id)

    @property
    def trace_count(self) -> int:
        return len(self._traces)
