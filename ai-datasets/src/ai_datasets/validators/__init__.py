"""
ai_datasets.validators

Enterprise dataset validation module for the AI Engineering Framework.

This package provides provider-independent dataset validation capabilities
including schema validation, quality checks, integrity verification,
constraint validation, and metadata validation.

Modules
-------
constants
    Validator-specific constants.

exceptions
    Validator-specific exception hierarchy.

operations
    High-level dataset validation operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.validators.operations import (
    validate_constraints,
    validate_dataset,
    validate_integrity,
    validate_metadata,
    validate_schema,
)

__all__ = [
    "validate_dataset",
    "validate_schema",
    "validate_integrity",
    "validate_constraints",
    "validate_metadata",
]