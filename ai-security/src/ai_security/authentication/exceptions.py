"""
Exceptions for ai_security.authentication.
"""

from __future__ import annotations


class AuthenticationError(Exception):
    """
    Base authentication exception.
    """

    def __init__(
        self,
        message: str = (
            "An authentication error occurred."
        ),
    ) -> None:
        super().__init__(message)


class InvalidAuthenticationProviderError(
    AuthenticationError,
):
    """
    Raised when an unsupported authentication
    provider is supplied.
    """

    def __init__(
        self,
        provider: str,
    ) -> None:
        self.provider = provider

        super().__init__(
            (
                "Invalid authentication "
                f"provider: '{provider}'."
            )
        )


class AuthenticationConfigurationError(
    AuthenticationError,
):
    """
    Raised when authentication configuration
    is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            (
                "Invalid authentication "
                f"configuration: "
                f"'{configuration}'."
            )
        )


class AuthenticationValidationError(
    AuthenticationError,
):
    """
    Raised when authentication validation
    fails.
    """

    def __init__(
        self,
        identity: str,
        reason: str,
    ) -> None:
        self.identity = identity
        self.reason = reason

        super().__init__(
            (
                f"Authentication for "
                f"'{identity}' failed: "
                f"{reason}."
            )
        )