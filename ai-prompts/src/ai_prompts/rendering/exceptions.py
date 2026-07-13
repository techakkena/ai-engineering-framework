"""Exceptions for prompt rendering."""


class RenderingError(Exception):
    """Base rendering exception."""


class MissingVariableError(RenderingError):
    """Raised when a required variable is missing."""


class InvalidTemplateSyntaxError(RenderingError):
    """Raised when template syntax is invalid."""


__all__ = [
    "RenderingError",
    "MissingVariableError",
    "InvalidTemplateSyntaxError",
]
