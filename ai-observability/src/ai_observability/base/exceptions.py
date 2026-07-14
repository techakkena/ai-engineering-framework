"""Exceptions for ai_observability."""


class ObservationError(Exception):
    """Base observation exception."""


class ObservationConfigurationError(
    ObservationError,
):
    """Raised for invalid observer configuration."""
