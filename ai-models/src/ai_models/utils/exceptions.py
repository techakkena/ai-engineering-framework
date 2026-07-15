"""
Exceptions for ai_models.utils.
"""

from __future__ import annotations


class UtilityError(Exception):
    """
    Base utility exception.
    """

    def __init__(
        self,
        message: str = (
            "A utility error occurred."
        ),
    ) -> None:
        super().__init__(message)


class InvalidEncodingError(
    UtilityError,
):
    """
    Raised when an unsupported encoding
    is supplied.
    """

    def __init__(
        self,
        encoding: str,
    ) -> None:
        self.encoding = encoding

        super().__init__(
            (
                "Invalid encoding: "
                f"'{encoding}'."
            )
        )


class UtilityConfigurationError(
    UtilityError,
):
    """
    Raised when utility configuration
    is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            (
                "Invalid utility "
                "configuration: "
                f"'{configuration}'."
            )
        )


class UtilityValidationError(
    UtilityError,
):
    """
    Raised when utility validation fails.
    """

    def __init__(
        self,
        value: str,
        reason: str,
    ) -> None:
        self.value = value
        self.reason = reason

        super().__init__(
            (
                f"'{value}' "
                f"validation failed: "
                f"{reason}."
            )
        )