"""Exceptions for utility functions."""


class UtilityError(Exception):
    """Base utility exception."""


class InvalidInputError(UtilityError):
    """Raised when an invalid input is provided."""


class EmptyValueError(UtilityError):
    """Raised when a required value is empty."""