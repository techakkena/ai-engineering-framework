"""
Exceptions for ai_runtime.scheduler.
"""

from __future__ import annotations


class SchedulerError(Exception):
    """
    Base scheduler exception.
    """

    def __init__(
        self,
        message: str = "A scheduler error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidSchedulerModeError(SchedulerError):
    """
    Raised when an invalid scheduler mode is supplied.
    """

    def __init__(
        self,
        mode: str,
    ) -> None:
        self.mode = mode

        super().__init__(
            f"Invalid scheduler mode: '{mode}'."
        )


class SchedulerConfigurationError(SchedulerError):
    """
    Raised when scheduler configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            f"Invalid scheduler configuration: '{configuration}'."
        )


class SchedulerValidationError(SchedulerError):
    """
    Raised when scheduler validation fails.
    """

    def __init__(
        self,
        scheduler: str,
        reason: str,
    ) -> None:
        self.scheduler = scheduler
        self.reason = reason

        super().__init__(
            f"Scheduler '{scheduler}' validation failed: {reason}."
        )