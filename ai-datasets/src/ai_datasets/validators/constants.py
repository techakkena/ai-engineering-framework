"""
Constants for the ai_datasets.validators module.

This module defines framework-independent constants used by dataset
validation operations.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Validation tasks
# ---------------------------------------------------------------------------

TASK_VALIDATE_DATASET: Final[str] = "validate_dataset"
TASK_VALIDATE_SCHEMA: Final[str] = "validate_schema"
TASK_VALIDATE_INTEGRITY: Final[str] = "validate_integrity"
TASK_VALIDATE_CONSTRAINTS: Final[str] = "validate_constraints"
TASK_VALIDATE_METADATA: Final[str] = "validate_metadata"

SUPPORTED_VALIDATIONS: Final[tuple[str, ...]] = (
    TASK_VALIDATE_DATASET,
    TASK_VALIDATE_SCHEMA,
    TASK_VALIDATE_INTEGRITY,
    TASK_VALIDATE_CONSTRAINTS,
    TASK_VALIDATE_METADATA,
)

# ---------------------------------------------------------------------------
# Validation severity
# ---------------------------------------------------------------------------

SEVERITY_INFO: Final[str] = "info"
SEVERITY_WARNING: Final[str] = "warning"
SEVERITY_ERROR: Final[str] = "error"

SUPPORTED_SEVERITIES: Final[tuple[str, ...]] = (
    SEVERITY_INFO,
    SEVERITY_WARNING,
    SEVERITY_ERROR,
)

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_STRICT_MODE: Final[bool] = True
DEFAULT_FAIL_FAST: Final[bool] = False
DEFAULT_MAX_ERRORS: Final[int] = 100

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_VALIDATION_TYPE: Final[str] = "validation_type"
METADATA_ERROR_COUNT: Final[str] = "error_count"
METADATA_WARNING_COUNT: Final[str] = "warning_count"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"