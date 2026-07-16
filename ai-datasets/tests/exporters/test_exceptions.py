"""
Unit tests for ai_datasets.exporters.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.exporters.exceptions import (
    CSVExportError,
    DatasetExportError,
    DatasetExporterError,
    ExcelExportError,
    ExportProviderError,
    ExportValidationError,
    JSONExportError,
    ParquetExportError,
    UnsupportedExportFormatError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        ExportValidationError,
        UnsupportedExportFormatError,
        DatasetExportError,
        CSVExportError,
        JSONExportError,
        ParquetExportError,
        ExcelExportError,
        ExportProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetExporterError],
) -> None:
    """Every custom exception should inherit from DatasetExporterError."""
    assert issubclass(
        exception_class,
        DatasetExporterError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetExporterError,
        match="export failure",
    ):
        raise DatasetExporterError(
            "export failure",
        )