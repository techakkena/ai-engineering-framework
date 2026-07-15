"""
Exceptions for ai_runtime.runtime.
"""

from __future__ import annotations


class RuntimeExecutionError(Exception):
    """
    Base runtime execution exception.
    """

    def __init__(
        self,
        message: str = "A runtime execution error occurred.",
    ) -> None:
        super().__init__(message)


class RuntimeInitializationError(RuntimeExecutionError):
    """
    Raised when runtime initialization fails.
    """

    def __init__(
        self,
        runtime: str,
    ) -> None:
        self.runtime = runtime
        super().__init__(
            f"Runtime initialization failed: '{runtime}'."
        )


class RuntimeStateError(RuntimeExecutionError):
    """
    Raised when an invalid runtime state is encountered.
    """

    def __init__(
        self,
        state: str,
    ) -> None:
        self.state = state
        super().__init__(
            f"Invalid runtime state: '{state}'."
        )


class InvalidRuntimeModeError(RuntimeExecutionError):
    """
    Raised when an unsupported runtime mode is supplied.
    """

    def __init__(
        self,
        mode: str,
    ) -> None:
        self.mode = mode
        super().__init__(
            f"Invalid runtime mode: '{mode}'."
        )