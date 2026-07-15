"""
Exceptions for ai_runtime.executor.
"""

from __future__ import annotations


class ExecutorError(Exception):
    """
    Base executor exception.
    """

    def __init__(
        self,
        message: str = "An executor error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidExecutorModeError(ExecutorError):
    """
    Raised when an invalid executor mode is supplied.
    """

    def __init__(
        self,
        mode: str,
    ) -> None:
        self.mode = mode

        super().__init__(
            f"Invalid executor mode: '{mode}'."
        )


class ExecutorConfigurationError(ExecutorError):
    """
    Raised when executor configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            f"Invalid executor configuration: '{configuration}'."
        )


class ExecutorValidationError(ExecutorError):
    """
    Raised when executor validation fails.
    """

    def __init__(
        self,
        executor: str,
        reason: str,
    ) -> None:
        self.executor = executor
        self.reason = reason

        super().__init__(
            f"Executor '{executor}' validation failed: {reason}."
        )