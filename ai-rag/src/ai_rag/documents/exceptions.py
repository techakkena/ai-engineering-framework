"""Exceptions for documents."""


class DocumentError(Exception):
    """Base document exception."""


class InvalidDocumentError(DocumentError):
    """Raised when a document is invalid."""


class UnsupportedDocumentTypeError(DocumentError):
    """Raised when the document type is unsupported."""