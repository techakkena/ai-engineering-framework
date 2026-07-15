"""
Exceptions for ai_runtime.utils.
"""

from __future__ import annotations


class RuntimeUtilityError(Exception):
    """
    Base runtime utility exception.
    """

    def __init__(
        self,
        message: str = (
            "A runtime utility error occurred."
        ),
    ) -> None:
        super().__init__(message)


class InvalidEncodingError(RuntimeUtilityError):
    """
    Raised when an unsupported encoding is supplied.
    """

    def __init__(
        self,
        encoding: str,
    ) -> None:
        self.encoding = encoding

        super().__init__(
            f"Invalid encoding: '{encoding}'."
        )


class InvalidUtilityOperationError(
    RuntimeUtilityError,
):
    """
    Raised when a utility operation fails.
    """

    def __init__(
        self,
        operation: str,
    ) -> None:
        self.operation = operation

        super().__init__(
            f"Invalid utility operation: '{operation}'."
        )


class UtilityConfigurationError(
    RuntimeUtilityError,
):
    """
    Raised when utility configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            f"Invalid utility configuration: '{configuration}'."
        )