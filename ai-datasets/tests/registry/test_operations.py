"""
Unit tests for ai_datasets.registry.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.registry.exceptions import (
    RegistryValidationError,
)
from ai_datasets.registry.operations import (
    RegistryResult,
    delete_dataset,
    get_dataset,
    list_datasets,
    register_dataset,
    update_dataset,
)


def test_register_dataset_success() -> None:
    """Dataset registration should succeed."""
    result = register_dataset("customers")

    assert isinstance(result, RegistryResult)
    assert result.success is True
    assert result.task == "register_dataset"


def test_register_dataset_empty_name() -> None:
    """Empty dataset names should raise."""
    with pytest.raises(RegistryValidationError):
        register_dataset("")


def test_update_dataset_success() -> None:
    """Dataset update should succeed."""
    result = update_dataset("customers")

    assert result.success is True
    assert result.task == "update_dataset"


def test_delete_dataset_success() -> None:
    """Dataset deletion should succeed."""
    result = delete_dataset("customers")

    assert result.success is True
    assert result.task == "delete_dataset"


def test_get_dataset_success() -> None:
    """Dataset lookup should succeed."""
    result = get_dataset("customers")

    assert result.success is True
    assert result.task == "get_dataset"


def test_list_datasets_success() -> None:
    """Listing datasets should succeed."""
    result = list_datasets()

    assert result.success is True
    assert result.task == "list_datasets"
    assert isinstance(result.data["datasets"], list)


@pytest.mark.parametrize(
    "operation",
    [
        register_dataset,
        update_dataset,
        delete_dataset,
        get_dataset,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """All name-based operations should reject empty names."""
    with pytest.raises(RegistryValidationError):
        operation("")