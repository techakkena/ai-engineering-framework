"""
Unit tests for ai_datasets.base.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.base.exceptions import (
    DatasetCreationError,
    DatasetLoadingError,
    DatasetSavingError,
    DatasetValidationError,
    UnsupportedDatasetTypeError,
)
from ai_datasets.base.operations import (
    DatasetInfo,
    DatasetResult,
    create_dataset,
    load_dataset,
    save_dataset,
    validate_dataset,
)


def test_create_dataset_success() -> None:
    """Dataset creation should succeed."""
    result = create_dataset("sample")

    assert isinstance(result, DatasetResult)
    assert result.success is True
    assert result.task == "create"


def test_create_dataset_empty_name() -> None:
    """Empty dataset names should raise."""
    with pytest.raises(DatasetCreationError):
        create_dataset("")


def test_create_dataset_invalid_type() -> None:
    """Unsupported dataset types should raise."""
    with pytest.raises(UnsupportedDatasetTypeError):
        create_dataset(
            "sample",
            dataset_type="custom",
        )


def test_load_dataset_success() -> None:
    """Dataset loading should succeed."""
    result = load_dataset("dataset.csv")

    assert result.success is True
    assert result.task == "load"


def test_load_dataset_empty_path() -> None:
    """Empty dataset paths should raise."""
    with pytest.raises(DatasetLoadingError):
        load_dataset("")


def test_save_dataset_success() -> None:
    """Dataset saving should succeed."""
    dataset = DatasetInfo(
        name="sample",
        dataset_type="tabular",
    )

    result = save_dataset(
        dataset,
        "output.csv",
    )

    assert result.success is True
    assert result.task == "save"


def test_save_dataset_empty_output_path() -> None:
    """Empty output paths should raise."""
    dataset = DatasetInfo(
        name="sample",
        dataset_type="tabular",
    )

    with pytest.raises(DatasetSavingError):
        save_dataset(dataset, "")


def test_validate_dataset_success() -> None:
    """Dataset validation should succeed."""
    dataset = DatasetInfo(
        name="sample",
        dataset_type="tabular",
    )

    result = validate_dataset(dataset)

    assert result.success is True
    assert result.task == "validate"


def test_validate_dataset_empty_name() -> None:
    """Datasets with empty names should raise."""
    dataset = DatasetInfo(
        name="",
        dataset_type="tabular",
    )

    with pytest.raises(DatasetValidationError):
        validate_dataset(dataset)


def test_validate_dataset_invalid_type() -> None:
    """Unsupported dataset types should raise."""
    dataset = DatasetInfo(
        name="sample",
        dataset_type="unsupported",
    )

    with pytest.raises(UnsupportedDatasetTypeError):
        validate_dataset(dataset)