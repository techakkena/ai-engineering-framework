"""
ai_multimodal.utils

Enterprise utility module for the AI Engineering Framework.

This package provides shared, provider-independent utility functions used
across all multimodal components including validation, MIME type detection,
file inspection, metadata helpers, and common multimodal abstractions.

Modules
-------
constants
    Shared utility constants.

exceptions
    Utility-specific exception hierarchy.

operations
    Common utility operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_multimodal.utils.operations import (
    detect_content_type,
    detect_file_format,
    generate_content_identifier,
    get_file_metadata,
    validate_file_path,
)

__all__ = [
    "validate_file_path",
    "detect_file_format",
    "detect_content_type",
    "get_file_metadata",
    "generate_content_identifier",
]