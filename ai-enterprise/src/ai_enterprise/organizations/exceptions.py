"""Exceptions for the ai_enterprise.organizations module."""

from __future__ import annotations


class OrganizationError(Exception):
    """Base exception for organization operations."""


class OrganizationValidationError(
    OrganizationError,
):
    """Raised when organization validation fails."""


class OrganizationRegistrationError(
    OrganizationError,
):
    """Raised when organization registration fails."""


class OrganizationNotFoundError(
    OrganizationRegistrationError,
):
    """Raised when an organization cannot be found."""


class DuplicateOrganizationError(
    OrganizationRegistrationError,
):
    """Raised when attempting to register a duplicate organization."""


class UnsupportedOrganizationTypeError(
    OrganizationValidationError,
):
    """Raised when an unsupported organization type is specified."""


__all__ = [
    "DuplicateOrganizationError",
    "OrganizationError",
    "OrganizationNotFoundError",
    "OrganizationRegistrationError",
    "OrganizationValidationError",
    "UnsupportedOrganizationTypeError",
]