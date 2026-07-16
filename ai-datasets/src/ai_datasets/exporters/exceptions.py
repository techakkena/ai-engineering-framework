"""
Exceptions for the ai_datasets.exporters package.
"""

from __future__ import annotations


class DatasetExporterError(Exception):
    """Base exception for dataset exporter errors."""


class ExportValidationError(DatasetExporterError):
    """Raised when exporter validation fails."""


class UnsupportedExportFormatError(ExportValidationError):
    """Raised when an unsupported export format is requested."""


class DatasetExportError(DatasetExporterError):
    """Base exception for dataset export failures."""


class CSVExportError(DatasetExportError):
    """Raised when CSV export fails."""


class JSONExportError(DatasetExportError):
    """Raised when JSON export fails."""


class ParquetExportError(DatasetExportError):
    """Raised when Parquet export fails."""


class ExcelExportError(DatasetExportError):
    """Raised when Excel export fails."""


class ExportProviderError(DatasetExporterError):
    """Raised when an export provider fails."""