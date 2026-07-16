"""
Unit tests for ai_datasets.validators.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.validators.exceptions import (
    DatasetValidationError,
    MetadataValidationError,
)
from ai_datasets.validators.operations import (
    ValidationResult,
    validate_constraints,
    validate_dataset,
    validate_integrity,
    validate_metadata,
    validate_schema,
)


def _dataset() -> list[dict[str, object]]:
    """Return a sample dataset."""
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]


def test_validate_dataset_success() -> None:
    """Dataset validation should succeed."""
    result = validate_dataset(_dataset())

    assert isinstance(result, ValidationResult)
    assert result.success is True
    assert result.task == "validate_dataset"


def test_validate_dataset_empty() -> None:
    """Empty datasets should raise."""
    with pytest.raises(DatasetValidationError):
        validate_dataset([])


def test_validate_schema_success() -> None:
    """Schema validation should succeed."""
    result = validate_schema(_dataset())

    assert result.success is True
    assert result.task == "validate_schema"


def test_validate_integrity_success() -> None:
    """Integrity validation should succeed."""
    result = validate_integrity(_dataset())

    assert result.success is True
    assert result.task == "validate_integrity"


def test_validate_constraints_success() -> None:
    """Constraint validation should succeed."""
    result = validate_constraints(_dataset())

    assert result.success is True
    assert result.task == "validate_constraints"


def test_validate_metadata_success() -> None:
    """Metadata validation should succeed."""
    result = validate_metadata({"name": "sample"})

    assert result.success is True
    assert result.task == "validate_metadata"


def test_validate_metadata_empty() -> None:
    """Empty metadata should raise."""
    with pytest.raises(MetadataValidationError):
        validate_metadata({})