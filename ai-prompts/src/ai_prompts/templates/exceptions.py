"""Exceptions for prompt templates."""


class TemplateError(Exception):
    """Base template exception."""


class InvalidTemplateError(TemplateError):
    """Raised when a template is invalid."""


class TemplateNotFoundError(TemplateError):
    """Raised when a template cannot be found."""


__all__ = [
    "TemplateError",
    "InvalidTemplateError",
    "TemplateNotFoundError",
]
