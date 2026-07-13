"""Exceptions for prompt validation."""


class ValidationError(Exception):
    """Base validation exception."""


class InvalidTemplateError(ValidationError):
    """Raised when a template is invalid."""


class InvalidVariablesError(ValidationError):
    """Raised when variables are invalid."""


__all__ = [
    "ValidationError",
    "InvalidTemplateError",
    "InvalidVariablesError",
]
