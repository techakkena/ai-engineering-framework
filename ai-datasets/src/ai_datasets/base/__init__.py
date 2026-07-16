"""
ai_datasets.base

Enterprise base abstractions for the AI Engineering Framework dataset package.

This package defines the provider-independent interfaces, result models,
and foundational types used throughout the ai_datasets package.

Modules
-------
constants
    Shared constants for dataset operations.

exceptions
    Dataset-specific exception hierarchy.

operations
    Base dataset operations and abstractions.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.base.operations import (
    DatasetInfo,
    DatasetResult,
    create_dataset,
    load_dataset,
    save_dataset,
    validate_dataset,
)

__all__ = [
    "DatasetInfo",
    "DatasetResult",
    "create_dataset",
    "load_dataset",
    "save_dataset",
    "validate_dataset",
]