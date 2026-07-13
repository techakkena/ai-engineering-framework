"""Utility exceptions."""


class UtilityError(Exception):
    """Base utility exception."""


class InvalidTextError(UtilityError):
    """Raised when text is invalid."""


class EmptyTextError(UtilityError):
    """Raised when text is empty."""


__all__ = [
    "UtilityError",
    "InvalidTextError",
    "EmptyTextError",
]
