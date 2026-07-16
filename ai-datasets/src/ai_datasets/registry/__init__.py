"""
ai_datasets.registry

Enterprise dataset registry module for the AI Engineering Framework.

This package provides provider-independent dataset registry capabilities
including registration, lookup, version management, lifecycle operations,
and metadata management.

Modules
-------
constants
    Registry-specific constants.

exceptions
    Registry-specific exception hierarchy.

operations
    High-level dataset registry operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.registry.operations import (
    delete_dataset,
    get_dataset,
    list_datasets,
    register_dataset,
    update_dataset,
)

__all__ = [
    "register_dataset",
    "update_dataset",
    "delete_dataset",
    "get_dataset",
    "list_datasets",
]