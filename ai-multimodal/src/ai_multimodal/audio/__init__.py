"""
ai_multimodal.audio

Enterprise audio processing module for the AI Engineering Framework.

This package provides provider-independent abstractions for audio processing,
including transcription, translation, classification, enhancement, analysis,
and metadata extraction.

Modules
-------
constants
    Audio-related constants and defaults.

exceptions
    Audio-specific exception hierarchy.

operations
    High-level audio operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_multimodal.audio.operations import (
    analyze_audio,
    classify_audio,
    extract_audio_metadata,
    transcribe_audio,
    translate_audio,
)

__all__ = [
    "transcribe_audio",
    "translate_audio",
    "classify_audio",
    "analyze_audio",
    "extract_audio_metadata",
]