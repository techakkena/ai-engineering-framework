"""Document utilities."""

from .constants import (
    DEFAULT_DOCUMENT_ID,
    DEFAULT_DOCUMENT_SOURCE,
    SUPPORTED_DOCUMENT_TYPES,
)
from .exceptions import (
    DocumentError,
    InvalidDocumentError,
    UnsupportedDocumentTypeError,
)
from .operations import (
    default_document_id,
    default_document_source,
    document_type,
    supported_document_type,
)

__all__ = [
    "DEFAULT_DOCUMENT_ID",
    "DEFAULT_DOCUMENT_SOURCE",
    "SUPPORTED_DOCUMENT_TYPES",
    "DocumentError",
    "InvalidDocumentError",
    "UnsupportedDocumentTypeError",
    "default_document_id",
    "default_document_source",
    "document_type",
    "supported_document_type",
]