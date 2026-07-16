"""
ai_datasets.catalog

Enterprise dataset catalog module for the AI Engineering Framework.

This package provides provider-independent dataset catalog capabilities
for registering, discovering, querying, versioning, and managing datasets.

Modules
-------
constants
    Catalog-specific constants.

exceptions
    Catalog-specific exception hierarchy.

operations
    High-level dataset catalog operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.catalog.operations import (
    get_dataset,
    list_datasets,
    register_dataset,
    search_datasets,
    unregister_dataset,
)

__all__ = [
    "register_dataset",
    "unregister_dataset",
    "get_dataset",
    "list_datasets",
    "search_datasets",
]