"""Exceptions for prompt variables."""


class VariableError(Exception):
    """Base variable exception."""


class InvalidVariableError(VariableError):
    """Raised when a variable name is invalid."""


class DuplicateVariableError(VariableError):
    """Raised when duplicate variables are detected."""


__all__ = [
    "VariableError",
    "InvalidVariableError",
    "DuplicateVariableError",
]
