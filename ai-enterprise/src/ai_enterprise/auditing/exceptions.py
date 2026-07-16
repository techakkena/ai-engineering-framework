"""Exceptions for the ai_enterprise.auditing module."""

from __future__ import annotations


class AuditError(Exception):
    """Base exception for auditing operations."""


class AuditValidationError(AuditError):
    """Raised when audit validation fails."""


class AuditRegistrationError(AuditError):
    """Raised when audit registration fails."""


class AuditNotFoundError(
    AuditRegistrationError,
):
    """Raised when an audit definition cannot be found."""


class DuplicateAuditError(
    AuditRegistrationError,
):
    """Raised when attempting to register a duplicate audit."""


class UnsupportedAuditLevelError(
    AuditValidationError,
):
    """Raised when an unsupported audit level is specified."""


__all__ = [
    "AuditError",
    "AuditNotFoundError",
    "AuditRegistrationError",
    "AuditValidationError",
    "DuplicateAuditError",
    "UnsupportedAuditLevelError",
]