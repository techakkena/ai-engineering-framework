from __future__ import annotations

"""Exceptions for the tickets module."""


class TicketException(Exception):
    """Base exception for ticket errors."""


class TicketNotFoundException(TicketException):
    """Raised when a ticket cannot be found."""


class TicketAlreadyExistsException(TicketException):
    """Raised when a duplicate ticket exists."""


class TicketValidationException(TicketException):
    """Raised when ticket validation fails."""


class TicketAssignmentException(TicketException):
    """Raised when ticket assignment fails."""
