"""
Constants for the ai_monitoring.tracing module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Trace operations
# ---------------------------------------------------------------------------

START: Final[str] = "start"
SPAN: Final[str] = "span"
END: Final[str] = "end"
GET: Final[str] = "get"
LIST: Final[str] = "list"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    START,
    SPAN,
    END,
    GET,
    LIST,
)

# ---------------------------------------------------------------------------
# Span types
# ---------------------------------------------------------------------------

LLM: Final[str] = "llm"
TOOL: Final[str] = "tool"
WORKFLOW: Final[str] = "workflow"
DATABASE: Final[str] = "database"

SUPPORTED_SPAN_TYPES: Final[tuple[str, ...]] = (
    LLM,
    TOOL,
    WORKFLOW,
    DATABASE,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_TRACE_ID: Final[str] = "trace_id"
METADATA_SPAN_ID: Final[str] = "span_id"
METADATA_PARENT_ID: Final[str] = "parent_id"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"