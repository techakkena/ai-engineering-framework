"""
Constants for the ai_monitoring.exporters module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

REGISTER: Final[str] = "register"
EXPORT: Final[str] = "export"
GET: Final[str] = "get"
LIST: Final[str] = "list"
REMOVE: Final[str] = "remove"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    REGISTER,
    EXPORT,
    GET,
    LIST,
    REMOVE,
)

# ---------------------------------------------------------------------------
# Exporter types
# ---------------------------------------------------------------------------

PROMETHEUS: Final[str] = "prometheus"
OPENTELEMETRY: Final[str] = "opentelemetry"
JSON: Final[str] = "json"
CSV: Final[str] = "csv"

SUPPORTED_EXPORTERS: Final[tuple[str, ...]] = (
    PROMETHEUS,
    OPENTELEMETRY,
    JSON,
    CSV,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_EXPORTER_ID: Final[str] = "exporter_id"
METADATA_EXPORTER_TYPE: Final[str] = "exporter_type"
METADATA_STATUS: Final[str] = "status"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_TIMESTAMP: Final[str] = "timestamp"