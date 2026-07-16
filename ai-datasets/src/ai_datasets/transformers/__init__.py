"""
ai_datasets.transformers

Enterprise dataset transformation module for the AI Engineering Framework.

This package provides provider-independent dataset transformation
capabilities including filtering, mapping, normalization, feature
engineering, batching, and preprocessing pipelines.

Modules
-------
constants
    Transformer-specific constants.

exceptions
    Transformer-specific exception hierarchy.

operations
    High-level dataset transformation operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.transformers.operations import (
    batch_dataset,
    filter_dataset,
    map_dataset,
    normalize_dataset,
    transform_dataset,
)

__all__ = [
    "transform_dataset",
    "filter_dataset",
    "map_dataset",
    "normalize_dataset",
    "batch_dataset",
]