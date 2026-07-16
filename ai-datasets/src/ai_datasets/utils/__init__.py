"""
ai_datasets.utils

Enterprise utility module for the AI Engineering Framework.

This package provides provider-independent utility functions for
dataset inspection, statistics, validation helpers, and common
operations used across the ai_datasets package.

Modules
-------
constants
    Utility-specific constants.

exceptions
    Utility-specific exception hierarchy.

operations
    High-level utility operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.utils.operations import (
    dataset_statistics,
    dataset_summary,
    infer_schema,
    validate_dataset,
    validate_record,
)

__all__ = [
    "dataset_statistics",
    "dataset_summary",
    "infer_schema",
    "validate_dataset",
    "validate_record",
]