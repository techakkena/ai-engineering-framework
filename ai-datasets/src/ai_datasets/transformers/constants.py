"""
Constants for the ai_datasets.transformers module.

This module defines framework-independent constants used by dataset
transformation operations.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Transformer operations
# ---------------------------------------------------------------------------

TRANSFORM: Final[str] = "transform"
FILTER: Final[str] = "filter"
MAP: Final[str] = "map"
NORMALIZE: Final[str] = "normalize"
BATCH: Final[str] = "batch"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    TRANSFORM,
    FILTER,
    MAP,
    NORMALIZE,
    BATCH,
)

# ---------------------------------------------------------------------------
# Normalization methods
# ---------------------------------------------------------------------------

NORMALIZATION_MIN_MAX: Final[str] = "min_max"
NORMALIZATION_Z_SCORE: Final[str] = "z_score"
NORMALIZATION_L2: Final[str] = "l2"

SUPPORTED_NORMALIZATION_METHODS: Final[tuple[str, ...]] = (
    NORMALIZATION_MIN_MAX,
    NORMALIZATION_Z_SCORE,
    NORMALIZATION_L2,
)

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_BATCH_SIZE: Final[int] = 1000
DEFAULT_SHUFFLE: Final[bool] = False
DEFAULT_DROP_LAST: Final[bool] = False

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_OPERATION: Final[str] = "operation"
METADATA_RECORD_COUNT: Final[str] = "record_count"
METADATA_BATCH_SIZE: Final[str] = "batch_size"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"