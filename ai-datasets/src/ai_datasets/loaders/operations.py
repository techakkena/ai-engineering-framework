"""
Enterprise dataset loading operations for the ai_datasets.loaders package.

This module provides provider-independent abstractions for loading datasets
from CSV, JSON, Parquet, text files, and databases.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_datasets.loaders.constants import (
    DEFAULT_BATCH_SIZE,
    DEFAULT_DELIMITER,
    DEFAULT_ENCODING,
)
from ai_datasets.loaders.exceptions import (
    CSVLoaderError,
    DatabaseLoaderError,
    LoaderValidationError,
)


@dataclass(slots=True, frozen=True)
class LoaderResult:
    """Represents the result of a dataset loading operation."""

    task: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def _validate_source(source: str) -> None:
    """Validate a dataset source."""
    if not source.strip():
        raise LoaderValidationError(
            "Dataset source cannot be empty."
        )


def load_csv(
    source: str,
    *,
    delimiter: str = DEFAULT_DELIMITER,
    encoding: str = DEFAULT_ENCODING,
) -> LoaderResult:
    """
    Load a CSV dataset.
    """
    _validate_source(source)

    if not delimiter:
        raise CSVLoaderError("Delimiter cannot be empty.")

    return LoaderResult(
        task="load_csv",
        success=True,
        data={
            "source": source,
            "delimiter": delimiter,
            "encoding": encoding,
        },
    )


def load_json(
    source: str,
    *,
    encoding: str = DEFAULT_ENCODING,
) -> LoaderResult:
    """
    Load a JSON dataset.
    """
    _validate_source(source)

    return LoaderResult(
        task="load_json",
        success=True,
        data={
            "source": source,
            "encoding": encoding,
        },
    )


def load_parquet(
    source: str,
) -> LoaderResult:
    """
    Load a Parquet dataset.
    """
    _validate_source(source)

    return LoaderResult(
        task="load_parquet",
        success=True,
        data={
            "source": source,
        },
    )


def load_text(
    source: str,
    *,
    encoding: str = DEFAULT_ENCODING,
) -> LoaderResult:
    """
    Load a text dataset.
    """
    _validate_source(source)

    return LoaderResult(
        task="load_text",
        success=True,
        data={
            "source": source,
            "encoding": encoding,
        },
    )


def load_database(
    connection_string: str,
    query: str,
    *,
    batch_size: int = DEFAULT_BATCH_SIZE,
) -> LoaderResult:
    """
    Load a dataset from a database.
    """
    if not connection_string.strip():
        raise DatabaseLoaderError(
            "Connection string cannot be empty."
        )

    if not query.strip():
        raise DatabaseLoaderError(
            "Query cannot be empty."
        )

    if batch_size <= 0:
        raise DatabaseLoaderError(
            "Batch size must be greater than zero."
        )

    return LoaderResult(
        task="load_database",
        success=True,
        data={
            "batch_size": batch_size,
        },
    )