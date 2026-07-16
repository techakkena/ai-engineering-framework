"""
Unit tests for ai_datasets.utils.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.utils.exceptions import (
    UtilityValidationError,
)
from ai_datasets.utils.operations import (
    UtilityResult,
    dataset_statistics,
    dataset_summary,
    infer_schema,
    validate_dataset,
    validate_record,
)


def _dataset() -> list[dict[str, object]]:
    """Return a sample dataset."""
    return [
        {
            "id": 1,
            "name": "Alice",
            "age": 30,
        },
        {
            "id": 2,
            "name": "Bob",
            "age": 25,
        },
    ]


def test_dataset_statistics_success() -> None:
    """Dataset statistics should succeed."""
    result = dataset_statistics(_dataset())

    assert isinstance(result, UtilityResult)
    assert result.success is True
    assert result.task == "statistics"


def test_dataset_summary_success() -> None:
    """Dataset summary should succeed."""
    result = dataset_summary(_dataset())

    assert result.success is True
    assert result.task == "summary"


def test_infer_schema_success() -> None:
    """Schema inference should succeed."""
    result = infer_schema(_dataset())

    assert result.success is True
    assert result.task == "schema"
    assert "schema" in result.data


def test_validate_dataset_success() -> None:
    """Dataset validation should succeed."""
    result = validate_dataset(_dataset())

    assert result.success is True
    assert result.task == "validate_dataset"


def test_validate_record_success() -> None:
    """Record validation should succeed."""
    result = validate_record(
        {
            "id": 1,
            "name": "Alice",
        },
    )

    assert result.success is True
    assert result.task == "validate_record"


def test_empty_dataset_validation() -> None:
    """Empty datasets should raise."""
    with pytest.raises(UtilityValidationError):
        dataset_statistics([])


@pytest.mark.parametrize(
    "operation",
    [
        dataset_statistics,
        dataset_summary,
        infer_schema,
        validate_dataset,
    ],
)
def test_dataset_operations_empty_dataset(
    operation,
) -> None:
    """All dataset operations should reject empty datasets."""
    with pytest.raises(UtilityValidationError):
        operation([])


def test_validate_record_empty() -> None:
    """Empty records should raise."""
    with pytest.raises(UtilityValidationError):
        validate_record({})