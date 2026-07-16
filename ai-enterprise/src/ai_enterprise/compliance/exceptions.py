"""Exceptions for the ai_enterprise.compliance module."""

from __future__ import annotations


class ComplianceError(Exception):
    """Base exception for compliance operations."""


class ComplianceValidationError(
    ComplianceError,
):
    """Raised when compliance validation fails."""


class ComplianceRegistrationError(
    ComplianceError,
):
    """Raised when compliance registration fails."""


class ComplianceNotFoundError(
    ComplianceRegistrationError,
):
    """Raised when a compliance definition cannot be found."""


class DuplicateComplianceError(
    ComplianceRegistrationError,
):
    """Raised when attempting to register a duplicate compliance."""


class UnsupportedComplianceStandardError(
    ComplianceValidationError,
):
    """Raised when an unsupported compliance standard is specified."""


__all__ = [
    "ComplianceError",
    "ComplianceValidationError",
    "ComplianceRegistrationError",
    "ComplianceNotFoundError",
    "DuplicateComplianceError",
    "UnsupportedComplianceStandardError",
]