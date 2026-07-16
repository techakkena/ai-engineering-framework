"""
Constants for the ai_multimodal.utils module.

This module defines framework-independent utility constants shared across
the ai_multimodal package.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Supported content types
# ---------------------------------------------------------------------------

CONTENT_TYPE_TEXT: Final[str] = "text"
CONTENT_TYPE_IMAGE: Final[str] = "image"
CONTENT_TYPE_AUDIO: Final[str] = "audio"
CONTENT_TYPE_VIDEO: Final[str] = "video"
CONTENT_TYPE_DOCUMENT: Final[str] = "document"
CONTENT_TYPE_UNKNOWN: Final[str] = "unknown"

SUPPORTED_CONTENT_TYPES: Final[tuple[str, ...]] = (
    CONTENT_TYPE_TEXT,
    CONTENT_TYPE_IMAGE,
    CONTENT_TYPE_AUDIO,
    CONTENT_TYPE_VIDEO,
    CONTENT_TYPE_DOCUMENT,
)

# ---------------------------------------------------------------------------
# Common file extensions
# ---------------------------------------------------------------------------

IMAGE_EXTENSIONS: Final[tuple[str, ...]] = (
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".bmp",
    ".gif",
)

AUDIO_EXTENSIONS: Final[tuple[str, ...]] = (
    ".mp3",
    ".wav",
    ".aac",
    ".ogg",
    ".flac",
)

VIDEO_EXTENSIONS: Final[tuple[str, ...]] = (
    ".mp4",
    ".mov",
    ".avi",
    ".mkv",
    ".webm",
)

DOCUMENT_EXTENSIONS: Final[tuple[str, ...]] = (
    ".pdf",
    ".docx",
    ".doc",
    ".txt",
    ".md",
    ".rtf",
)

# ---------------------------------------------------------------------------
# File constraints
# ---------------------------------------------------------------------------

MAX_FILE_SIZE_MB: Final[int] = 1024
MAX_FILENAME_LENGTH: Final[int] = 255

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_FILENAME: Final[str] = "filename"
METADATA_EXTENSION: Final[str] = "extension"
METADATA_SIZE: Final[str] = "size_bytes"
METADATA_CONTENT_TYPE: Final[str] = "content_type"
METADATA_CREATED_AT: Final[str] = "created_at"