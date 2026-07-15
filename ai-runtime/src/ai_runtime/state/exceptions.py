"""
Exceptions for ai_runtime.state.
"""

from __future__ import annotations


class StateError(Exception):
    """
    Base state exception.
    """

    def __init__(
        self,
        message: str = "A state error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidStateStatusError(StateError):
    """
    Raised when an invalid state status is supplied.
    """

    def __init__(
        self,
        status: str,
    ) -> None:
        self.status = status

        super().__init__(
            f"Invalid state status: '{status}'."
        )


class StateConfigurationError(StateError):
    """
    Raised when state configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            f"Invalid state configuration: '{configuration}'."
        )


class StateValidationError(StateError):
    """
    Raised when state validation fails.
    """

    def __init__(
        self,
        state: str,
        reason: str,
    ) -> None:
        self.state = state
        self.reason = reason

        super().__init__(
            f"State '{state}' validation failed: {reason}."
        )