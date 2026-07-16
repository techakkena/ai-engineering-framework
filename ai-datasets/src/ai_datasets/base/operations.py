"""
Enterprise base dataset operations for the ai_datasets.base package.

This module provides provider-independent abstractions for creating,
loading, saving, and validating datasets.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_datasets.base.constants import (
    DATASET_TYPE_TABULAR,
    DEFAULT_ENCODING,
    SUPPORTED_DATASET_TYPES,
)
from ai_datasets.base.exceptions import (
    DatasetCreationError,
    DatasetLoadingError,
    DatasetSavingError,
    DatasetValidationError,
    UnsupportedDatasetTypeError,
)


@dataclass(slots=True, frozen=True)
class DatasetInfo:
    """Represents dataset metadata."""

    name: str
    dataset_type: str
    version: str = "1.0.0"
    record_count: int = 0


@dataclass(slots=True, frozen=True)
class DatasetResult:
    """Represents the result of a dataset operation."""

    task: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def create_dataset(
    name: str,
    *,
    dataset_type: str = DATASET_TYPE_TABULAR,
) -> DatasetResult:
    """
    Create a dataset definition.
    """
    if not name.strip():
        raise DatasetCreationError(
            "Dataset name cannot be empty."
        )

    if dataset_type not in SUPPORTED_DATASET_TYPES:
        raise UnsupportedDatasetTypeError(
            f"Unsupported dataset type: {dataset_type!r}."
        )

    return DatasetResult(
        task="create",
        success=True,
        data={
            "name": name,
            "dataset_type": dataset_type,
        },
    )


def load_dataset(
    dataset_path: str,
    *,
    encoding: str = DEFAULT_ENCODING,
) -> DatasetResult:
    """
    Load a dataset.
    """
    if not dataset_path.strip():
        raise DatasetLoadingError(
            "Dataset path cannot be empty."
        )

    return DatasetResult(
        task="load",
        success=True,
        data={
            "dataset_path": dataset_path,
            "encoding": encoding,
        },
    )


def save_dataset(
    dataset: DatasetInfo,
    output_path: str,
) -> DatasetResult:
    """
    Save a dataset.
    """
    if not output_path.strip():
        raise DatasetSavingError(
            "Output path cannot be empty."
        )

    return DatasetResult(
        task="save",
        success=True,
        data={
            "dataset": dataset,
            "output_path": output_path,
        },
    )


def validate_dataset(
    dataset: DatasetInfo,
) -> DatasetResult:
    """
    Validate dataset metadata.
    """
    if not dataset.name.strip():
        raise DatasetValidationError(
            "Dataset name cannot be empty."
        )

    if dataset.dataset_type not in SUPPORTED_DATASET_TYPES:
        raise UnsupportedDatasetTypeError(
            f"Unsupported dataset type: {dataset.dataset_type!r}."
        )

    return DatasetResult(
        task="validate",
        success=True,
        data={
            "dataset": dataset,
        },
    )