"""
ai_datasets.loaders

Enterprise dataset loader module for the AI Engineering Framework.

This package provides provider-independent dataset loading capabilities
for local files, cloud storage, databases, APIs, and external dataset
repositories.

Modules
-------
constants
    Loader-specific constants.

exceptions
    Loader-specific exception hierarchy.

operations
    High-level dataset loading operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.loaders.operations import (
    load_csv,
    load_database,
    load_json,
    load_parquet,
    load_text,
)

__all__ = [
    "load_csv",
    "load_json",
    "load_parquet",
    "load_text",
    "load_database",
]