"""
Constants for the ai_datasets.base module.

This module defines framework-independent constants used throughout the
ai_datasets package.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Dataset types
# ---------------------------------------------------------------------------

DATASET_TYPE_TEXT: Final[str] = "text"
DATASET_TYPE_IMAGE: Final[str] = "image"
DATASET_TYPE_AUDIO: Final[str] = "audio"
DATASET_TYPE_VIDEO: Final[str] = "video"
DATASET_TYPE_DOCUMENT: Final[str] = "document"
DATASET_TYPE_TABULAR: Final[str] = "tabular"
DATASET_TYPE_JSON: Final[str] = "json"
DATASET_TYPE_PARQUET: Final[str] = "parquet"

SUPPORTED_DATASET_TYPES: Final[tuple[str, ...]] = (
    DATASET_TYPE_TEXT,
    DATASET_TYPE_IMAGE,
    DATASET_TYPE_AUDIO,
    DATASET_TYPE_VIDEO,
    DATASET_TYPE_DOCUMENT,
    DATASET_TYPE_TABULAR,
    DATASET_TYPE_JSON,
    DATASET_TYPE_PARQUET,
)

# ---------------------------------------------------------------------------
# Dataset operations
# ---------------------------------------------------------------------------

TASK_CREATE: Final[str] = "create"
TASK_LOAD: Final[str] = "load"
TASK_SAVE: Final[str] = "save"
TASK_VALIDATE: Final[str] = "validate"

SUPPORTED_TASKS: Final[tuple[str, ...]] = (
    TASK_CREATE,
    TASK_LOAD,
    TASK_SAVE,
    TASK_VALIDATE,
)

# ---------------------------------------------------------------------------
# Dataset defaults
# ---------------------------------------------------------------------------

DEFAULT_ENCODING: Final[str] = "utf-8"
DEFAULT_BATCH_SIZE: Final[int] = 1000
DEFAULT_CACHE_ENABLED: Final[bool] = True

# ---------------------------------------------------------------------------
# Dataset limits
# ---------------------------------------------------------------------------

MAX_DATASET_SIZE_GB: Final[int] = 100
MAX_DATASET_NAME_LENGTH: Final[int] = 255

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_NAME: Final[str] = "name"
METADATA_VERSION: Final[str] = "version"
METADATA_TYPE: Final[str] = "dataset_type"
METADATA_RECORD_COUNT: Final[str] = "record_count"
METADATA_CREATED_AT: Final[str] = "created_at"
METADATA_UPDATED_AT: Final[str] = "updated_at"