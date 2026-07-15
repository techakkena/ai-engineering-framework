"""
Exceptions for the ai_security.utils module.
"""

from __future__ import annotations


class SecurityUtilityError(Exception):
    """Base exception for security utility operations."""


class ValidationError(SecurityUtilityError):
    """Raised when validation fails."""