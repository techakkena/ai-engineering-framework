"""
ai_multimodal.image

Enterprise image processing module for the AI Engineering Framework.

This package provides framework-independent abstractions and utilities for
image generation, editing, analysis, transformation, optimization, and
metadata handling. Implementations are provider-agnostic and intended to
integrate with multiple AI image platforms.

Modules
-------
constants
    Image-related constants and defaults.

exceptions
    Image-specific exception hierarchy.

operations
    High-level image operations.

Design Goals
------------
- Framework independent
- Fully typed
- SOLID compliant
- Production ready
- Enterprise documented
"""

from ai_multimodal.image.operations import (
    analyze_image,
    edit_image,
    generate_image,
    get_image_metadata,
    optimize_image,
)

__all__ = [
    "generate_image",
    "edit_image",
    "analyze_image",
    "optimize_image",
    "get_image_metadata",
]