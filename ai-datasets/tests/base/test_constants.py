"""
Unit tests for ai_datasets.base.constants.
"""

from __future__ import annotations

from ai_datasets.base import constants


def test_supported_dataset_types() -> None:
    """Supported dataset types should contain all expected types."""
    assert constants.DATASET_TYPE_TEXT in constants.SUPPORTED_DATASET_TYPES
    assert constants.DATASET_TYPE_IMAGE in constants.SUPPORTED_DATASET_TYPES
    assert constants.DATASET_TYPE_AUDIO in constants.SUPPORTED_DATASET_TYPES
    assert constants.DATASET_TYPE_VIDEO in constants.SUPPORTED_DATASET_TYPES
    assert (
        constants.DATASET_TYPE_DOCUMENT
        in constants.SUPPORTED_DATASET_TYPES
    )
    assert (
        constants.DATASET_TYPE_TABULAR
        in constants.SUPPORTED_DATASET_TYPES
    )


def test_supported_tasks() -> None:
    """Supported tasks should contain all operations."""
    assert constants.TASK_CREATE in constants.SUPPORTED_TASKS
    assert constants.TASK_LOAD in constants.SUPPORTED_TASKS
    assert constants.TASK_SAVE in constants.SUPPORTED_TASKS
    assert constants.TASK_VALIDATE in constants.SUPPORTED_TASKS


def test_default_values() -> None:
    """Default configuration values should be valid."""
    assert constants.DEFAULT_ENCODING == "utf-8"
    assert constants.DEFAULT_BATCH_SIZE > 0
    assert constants.DEFAULT_CACHE_ENABLED is True


def test_dataset_limits() -> None:
    """Dataset limits should be positive."""
    assert constants.MAX_DATASET_SIZE_GB > 0
    assert constants.MAX_DATASET_NAME_LENGTH > 0


def test_metadata_keys() -> None:
    """Metadata keys should match expected values."""
    assert constants.METADATA_NAME == "name"
    assert constants.METADATA_VERSION == "version"
    assert constants.METADATA_TYPE == "dataset_type"
    assert constants.METADATA_RECORD_COUNT == "record_count"
    assert constants.METADATA_CREATED_AT == "created_at"
    assert constants.METADATA_UPDATED_AT == "updated_at"