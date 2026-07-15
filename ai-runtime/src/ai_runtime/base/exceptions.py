"""
Exceptions for the ai_runtime.base module.
"""

from __future__ import annotations


class RuntimeError(Exception):
    """
    Base runtime exception.
    """

    def __init__(
        self,
        message: str = "A runtime error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidRuntimeError(RuntimeError):
    """
    Raised when an invalid runtime is encountered.
    """

    def __init__(
        self,
        runtime: str,
    ) -> None:
        self.runtime = runtime
        super().__init__(
            f"Invalid runtime: '{runtime}'."
        )


class RuntimeValidationError(RuntimeError):
    """
    Raised when runtime validation fails.
    """

    def __init__(
        self,
        runtime: str,
        reason: str,
    ) -> None:
        self.runtime = runtime
        self.reason = reason
        super().__init__(
            f"Runtime '{runtime}' validation failed: {reason}."
        )


class RuntimeConfigurationError(RuntimeError):
    """
    Raised when runtime configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration
        super().__init__(
            f"Invalid runtime configuration: '{configuration}'."
        )