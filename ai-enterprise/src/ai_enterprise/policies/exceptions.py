"""Exceptions for the ai_enterprise.policies module."""

from __future__ import annotations


class PolicyError(Exception):
    """Base exception for policy operations."""


class PolicyValidationError(PolicyError):
    """Raised when policy validation fails."""


class PolicyRegistrationError(PolicyError):
    """Raised when policy registration fails."""


class PolicyNotFoundError(
    PolicyRegistrationError,
):
    """Raised when a policy cannot be found."""


class DuplicatePolicyError(
    PolicyRegistrationError,
):
    """Raised when attempting to register a duplicate policy."""


class UnsupportedPolicyTypeError(
    PolicyValidationError,
):
    """Raised when an unsupported policy type is specified."""


__all__ = [
    "DuplicatePolicyError",
    "PolicyError",
    "PolicyNotFoundError",
    "PolicyRegistrationError",
    "PolicyValidationError",
    "UnsupportedPolicyTypeError",
]