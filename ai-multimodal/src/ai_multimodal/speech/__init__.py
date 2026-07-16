"""
ai_multimodal.speech

Enterprise speech synthesis module for the AI Engineering Framework.

This package provides provider-independent abstractions for speech synthesis,
voice generation, streaming speech, voice cloning, speech configuration, and
speech metadata management.

Modules
-------
constants
    Speech-related constants and defaults.

exceptions
    Speech-specific exception hierarchy.

operations
    High-level speech operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_multimodal.speech.operations import (
    clone_voice,
    generate_speech,
    list_available_voices,
    stream_speech,
    synthesize_ssml,
)

__all__ = [
    "generate_speech",
    "stream_speech",
    "clone_voice",
    "synthesize_ssml",
    "list_available_voices",
]