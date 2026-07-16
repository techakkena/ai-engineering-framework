"""
ai_multimodal.vision

Enterprise computer vision module for the AI Engineering Framework.

This package provides provider-independent abstractions for computer vision
tasks including image understanding, object detection, OCR, classification,
caption generation, scene analysis, and visual question answering.

Modules
-------
constants
    Vision-specific constants.

exceptions
    Vision exception hierarchy.

operations
    High-level vision operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_multimodal.vision.operations import (
    classify_image,
    describe_image,
    detect_objects,
    extract_text,
    visual_question_answering,
)

__all__ = [
    "classify_image",
    "describe_image",
    "detect_objects",
    "extract_text",
    "visual_question_answering",
]