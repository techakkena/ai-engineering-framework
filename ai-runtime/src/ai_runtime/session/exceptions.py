"""
Exceptions for ai_runtime.session.
"""

from __future__ import annotations


class SessionError(Exception):
    """
    Base session exception.
    """

    def __init__(
        self,
        message: str = "A session error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidSessionStateError(SessionError):
    """
    Raised when an invalid session state is supplied.
    """

    def __init__(
        self,
        state: str,
    ) -> None:
        self.state = state

        super().__init__(
            f"Invalid session state: '{state}'."
        )


class SessionConfigurationError(SessionError):
    """
    Raised when session configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            f"Invalid session configuration: '{configuration}'."
        )


class SessionValidationError(SessionError):
    """
    Raised when session validation fails.
    """

    def __init__(
        self,
        session: str,
        reason: str,
    ) -> None:
        self.session = session
        self.reason = reason

        super().__init__(
            f"Session '{session}' validation failed: {reason}."
        )