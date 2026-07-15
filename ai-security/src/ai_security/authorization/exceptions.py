"""
Exceptions for ai_security.authorization.
"""

from __future__ import annotations


class AuthorizationError(Exception):
    """
    Base authorization exception.
    """

    def __init__(
        self,
        message: str = (
            "An authorization error occurred."
        ),
    ) -> None:
        super().__init__(message)


class InvalidAuthorizationProviderError(
    AuthorizationError,
):
    """
    Raised when an unsupported authorization
    provider is supplied.
    """

    def __init__(
        self,
        provider: str,
    ) -> None:
        self.provider = provider

        super().__init__(
            (
                "Invalid authorization "
                f"provider: '{provider}'."
            )
        )


class AuthorizationConfigurationError(
    AuthorizationError,
):
    """
    Raised when authorization configuration
    is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            (
                "Invalid authorization "
                f"configuration: "
                f"'{configuration}'."
            )
        )


class AuthorizationValidationError(
    AuthorizationError,
):
    """
    Raised when authorization validation
    fails.
    """

    def __init__(
        self,
        subject: str,
        reason: str,
    ) -> None:
        self.subject = subject
        self.reason = reason

        super().__init__(
            (
                f"Authorization for "
                f"'{subject}' failed: "
                f"{reason}."
            )
        )