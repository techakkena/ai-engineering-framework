"""Exceptions for the ai_enterprise.tenants module."""

from __future__ import annotations


class TenantError(Exception):
    """Base exception for tenant operations."""


class TenantValidationError(TenantError):
    """Raised when tenant validation fails."""


class TenantRegistrationError(TenantError):
    """Raised when tenant registration fails."""


class TenantNotFoundError(
    TenantRegistrationError,
):
    """Raised when a tenant cannot be found."""


class DuplicateTenantError(
    TenantRegistrationError,
):
    """Raised when attempting to register a duplicate tenant."""


class UnsupportedTenantPlanError(
    TenantValidationError,
):
    """Raised when an unsupported tenant plan is specified."""


__all__ = [
    "DuplicateTenantError",
    "TenantError",
    "TenantNotFoundError",
    "TenantRegistrationError",
    "TenantValidationError",
    "UnsupportedTenantPlanError",
]