"""
Unit tests for ai_datasets.catalog.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.catalog.exceptions import (
    CatalogValidationError,
)
from ai_datasets.catalog.operations import (
    CatalogResult,
    get_dataset,
    list_datasets,
    register_dataset,
    search_datasets,
    unregister_dataset,
)


def test_register_dataset_success() -> None:
    """Dataset registration should succeed."""
    result = register_dataset("customers")

    assert isinstance(result, CatalogResult)
    assert result.success is True
    assert result.task == "register_dataset"


def test_register_dataset_empty_name() -> None:
    """Empty dataset names should raise."""
    with pytest.raises(CatalogValidationError):
        register_dataset("")


def test_unregister_dataset_success() -> None:
    """Dataset unregistration should succeed."""
    result = unregister_dataset("customers")

    assert result.success is True
    assert result.task == "unregister_dataset"


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


def test_search_datasets_success() -> None:
    """Dataset search should succeed."""
    result = search_datasets("customer")

    assert result.success is True
    assert result.task == "search_datasets"


def test_search_datasets_empty_query() -> None:
    """Empty search queries should raise."""
    with pytest.raises(CatalogValidationError):
        search_datasets("")


@pytest.mark.parametrize(
    "operation",
    [
        register_dataset,
        unregister_dataset,
        get_dataset,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """All name-based operations should reject empty names."""
    with pytest.raises(CatalogValidationError):
        operation("")