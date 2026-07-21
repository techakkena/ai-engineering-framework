from __future__ import annotations

"""Operations for document handling."""

from pathlib import Path

from .constants import (
    DEFAULT_DOCUMENT_ID,
    DEFAULT_DOCUMENT_SOURCE,
    SUPPORTED_DOCUMENT_TYPES,
)


def default_document_id() -> str:
    """Return the default document identifier."""

    return DEFAULT_DOCUMENT_ID


def default_document_source() -> str:
    """Return the default document source."""

    return DEFAULT_DOCUMENT_SOURCE


def document_type(path: str) -> str:
    """Return the document type."""

    return Path(path).suffix.lower().lstrip(".")


def supported_document_type(document_type_name: str) -> bool:
    """Return True if the document type is supported."""

    return document_type_name.lower() in SUPPORTED_DOCUMENT_TYPES
