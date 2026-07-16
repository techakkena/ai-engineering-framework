"""
ai_multimodal.video

Enterprise video processing module for the AI Engineering Framework.

This package provides provider-independent abstractions for AI-powered
video processing including analysis, summarization, scene detection,
transcription, frame extraction, and metadata retrieval.

Modules
-------
constants
    Video-related constants and defaults.

exceptions
    Video-specific exception hierarchy.

operations
    High-level video operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_multimodal.video.operations import (
    analyze_video,
    extract_frames,
    generate_video_summary,
    get_video_metadata,
    transcribe_video,
)

__all__ = [
    "analyze_video",
    "extract_frames",
    "generate_video_summary",
    "get_video_metadata",
    "transcribe_video",
]