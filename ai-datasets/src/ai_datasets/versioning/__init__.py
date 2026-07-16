"""
ai_datasets.versioning

Enterprise dataset versioning module for the AI Engineering Framework.

This package provides provider-independent dataset version management,
tracking, comparison, rollback, and history operations.

Modules
-------
constants
    Versioning-specific constants.

exceptions
    Versioning-specific exception hierarchy.

operations
    High-level dataset versioning operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.versioning.operations import (
    compare_versions,
    create_version,
    get_version,
    list_versions,
    rollback_version,
)

__all__ = [
    "create_version",
    "get_version",
    "list_versions",
    "compare_versions",
    "rollback_version",
]