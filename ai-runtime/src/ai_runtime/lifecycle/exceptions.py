"""
Exceptions for ai_runtime.lifecycle.
"""

from __future__ import annotations


class LifecycleError(Exception):
    """
    Base lifecycle exception.
    """

    def __init__(
        self,
        message: str = "A lifecycle error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidLifecyclePhaseError(LifecycleError):
    """
    Raised when an invalid lifecycle phase is supplied.
    """

    def __init__(
        self,
        phase: str,
    ) -> None:
        self.phase = phase

        super().__init__(
            f"Invalid lifecycle phase: '{phase}'."
        )


class LifecycleConfigurationError(LifecycleError):
    """
    Raised when lifecycle configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            f"Invalid lifecycle configuration: '{configuration}'."
        )


class LifecycleValidationError(LifecycleError):
    """
    Raised when lifecycle validation fails.
    """

    def __init__(
        self,
        lifecycle: str,
        reason: str,
    ) -> None:
        self.lifecycle = lifecycle
        self.reason = reason

        super().__init__(
            f"Lifecycle '{lifecycle}' validation failed: {reason}."
        )