"""
Unit tests for ai_datasets.exporters.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.exporters.exceptions import (
    ExportValidationError,
)
from ai_datasets.exporters.operations import (
    ExportResult,
    export_csv,
    export_dataset,
    export_excel,
    export_json,
    export_parquet,
)


def _dataset() -> list[dict[str, object]]:
    """Return a sample dataset."""
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]


def test_export_dataset_success() -> None:
    """Generic export should succeed."""
    result = export_dataset(
        _dataset(),
        "output.csv",
    )

    assert isinstance(result, ExportResult)
    assert result.success is True
    assert result.task == "export_dataset"


def test_export_dataset_empty_dataset() -> None:
    """Empty datasets should raise."""
    with pytest.raises(ExportValidationError):
        export_dataset(
            [],
            "output.csv",
        )


def test_export_dataset_empty_output_path() -> None:
    """Empty output paths should raise."""
    with pytest.raises(ExportValidationError):
        export_dataset(
            _dataset(),
            "",
        )


def test_export_csv_success() -> None:
    """CSV export should succeed."""
    result = export_csv(
        _dataset(),
        "output.csv",
    )

    assert result.success is True
    assert result.task == "export_csv"


def test_export_json_success() -> None:
    """JSON export should succeed."""
    result = export_json(
        _dataset(),
        "output.json",
    )

    assert result.success is True
    assert result.task == "export_json"


def test_export_parquet_success() -> None:
    """Parquet export should succeed."""
    result = export_parquet(
        _dataset(),
        "output.parquet",
    )

    assert result.success is True
    assert result.task == "export_parquet"


def test_export_excel_success() -> None:
    """Excel export should succeed."""
    result = export_excel(
        _dataset(),
        "output.xlsx",
    )

    assert result.success is True
    assert result.task == "export_excel"


@pytest.mark.parametrize(
    "operation,path",
    [
        (export_csv, "output.csv"),
        (export_json, "output.json"),
        (export_parquet, "output.parquet"),
        (export_excel, "output.xlsx"),
    ],
)
def test_export_operations_empty_dataset(
    operation,
    path,
) -> None:
    """All exporters should reject empty datasets."""
    with pytest.raises(ExportValidationError):
        operation([], path)


@pytest.mark.parametrize(
    "operation",
    [
        export_csv,
        export_json,
        export_parquet,
        export_excel,
    ],
)
def test_export_operations_empty_output_path(
    operation,
) -> None:
    """All exporters should reject empty output paths."""
    with pytest.raises(ExportValidationError):
        operation(
            _dataset(),
            "",
        )