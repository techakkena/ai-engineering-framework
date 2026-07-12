"""
Custom exceptions for the validators module.

Author: TECHAKKENA
"""


class ValidationError(Exception):
    """Base exception for validation operations."""


class RequiredFieldError(ValidationError):
    """Raised when a required value is missing."""


class TypeValidationError(ValidationError):
    """Raised when a value has an invalid type."""


class RangeValidationError(ValidationError):
    """Raised when a value is outside the allowed range."""


class LengthValidationError(ValidationError):
    """Raised when a value has an invalid length."""


class ChoiceValidationError(ValidationError):
    """Raised when a value is not one of the allowed choices."""


class RegexValidationError(ValidationError):
    """Raised when a value does not match the expected pattern."""
