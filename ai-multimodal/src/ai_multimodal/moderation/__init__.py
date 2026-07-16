"""
ai_multimodal.moderation

Enterprise AI moderation module for the AI Engineering Framework.

This package provides provider-independent abstractions for moderating
multimodal content including text, images, audio, video, and documents.
It offers a consistent interface for safety classification, policy
evaluation, risk scoring, and moderation metadata.

Modules
-------
constants
    Moderation-related constants and defaults.

exceptions
    Moderation-specific exception hierarchy.

operations
    High-level moderation operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_multimodal.moderation.operations import (
    get_moderation_metadata,
    moderate_audio,
    moderate_image,
    moderate_text,
    moderate_video,
)

__all__ = [
    "moderate_text",
    "moderate_image",
    "moderate_audio",
    "moderate_video",
    "get_moderation_metadata",
]