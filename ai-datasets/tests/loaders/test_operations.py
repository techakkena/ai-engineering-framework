"""
Unit tests for ai_datasets.loaders.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.loaders.exceptions import (
    CSVLoaderError,
    DatabaseLoaderError,
    LoaderValidationError,
)
from ai_datasets.loaders.operations import (
    LoaderResult,
    load_csv,
    load_database,
    load_json,
    load_parquet,
    load_text,
)


def test_load_csv_success() -> None:
    """CSV loading should succeed."""
    result = load_csv("dataset.csv")

    assert isinstance(result, LoaderResult)
    assert result.success is True
    assert result.task == "load_csv"


def test_load_csv_invalid_delimiter() -> None:
    """Empty delimiters should raise."""
    with pytest.raises(CSVLoaderError):
        load_csv(
            "dataset.csv",
            delimiter="",
        )


def test_load_csv_empty_source() -> None:
    """Empty sources should raise."""
    with pytest.raises(LoaderValidationError):
        load_csv("")


def test_load_json_success() -> None:
    """JSON loading should succeed."""
    result = load_json("dataset.json")

    assert result.success is True
    assert result.task == "load_json"


def test_load_parquet_success() -> None:
    """Parquet loading should succeed."""
    result = load_parquet("dataset.parquet")

    assert result.success is True
    assert result.task == "load_parquet"


def test_load_text_success() -> None:
    """Text loading should succeed."""
    result = load_text("dataset.txt")

    assert result.success is True
    assert result.task == "load_text"


def test_load_database_success() -> None:
    """Database loading should succeed."""
    result = load_database(
        "sqlite:///db.sqlite",
        "SELECT * FROM users",
    )

    assert result.success is True
    assert result.task == "load_database"


def test_load_database_empty_connection() -> None:
    """Empty connection strings should raise."""
    with pytest.raises(DatabaseLoaderError):
        load_database(
            "",
            "SELECT 1",
        )


def test_load_database_empty_query() -> None:
    """Empty queries should raise."""
    with pytest.raises(DatabaseLoaderError):
        load_database(
            "sqlite:///db.sqlite",
            "",
        )


def test_load_database_invalid_batch_size() -> None:
    """Invalid batch sizes should raise."""
    with pytest.raises(DatabaseLoaderError):
        load_database(
            "sqlite:///db.sqlite",
            "SELECT * FROM users",
            batch_size=0,
        )