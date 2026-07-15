"""
Exceptions for ai_runtime.context.
"""

from __future__ import annotations


class ContextError(Exception):
    """
    Base context exception.
    """

    def __init__(
        self,
        message: str = "A context error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidContextScopeError(ContextError):
    """
    Raised when an invalid context scope is supplied.
    """

    def __init__(
        self,
        scope: str,
    ) -> None:
        self.scope = scope

        super().__init__(
            f"Invalid context scope: '{scope}'."
        )


class ContextConfigurationError(ContextError):
    """
    Raised when context configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            f"Invalid context configuration: '{configuration}'."
        )


class ContextValidationError(ContextError):
    """
    Raised when context validation fails.
    """

    def __init__(
        self,
        context: str,
        reason: str,
    ) -> None:
        self.context = context
        self.reason = reason

        super().__init__(
            f"Context '{context}' validation failed: {reason}."
        )