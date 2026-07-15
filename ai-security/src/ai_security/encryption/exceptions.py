"""
Exceptions for ai_security.encryption.
"""

from __future__ import annotations


class EncryptionError(Exception):
    """
    Base encryption exception.
    """

    def __init__(
        self,
        message: str = (
            "An encryption error occurred."
        ),
    ) -> None:
        super().__init__(message)


class InvalidEncryptionProviderError(
    EncryptionError,
):
    """
    Raised when an unsupported encryption
    provider is supplied.
    """

    def __init__(
        self,
        provider: str,
    ) -> None:
        self.provider = provider

        super().__init__(
            (
                "Invalid encryption "
                f"provider: '{provider}'."
            )
        )


class EncryptionConfigurationError(
    EncryptionError,
):
    """
    Raised when encryption configuration
    is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            (
                "Invalid encryption "
                f"configuration: "
                f"'{configuration}'."
            )
        )


class EncryptionValidationError(
    EncryptionError,
):
    """
    Raised when encryption validation
    fails.
    """

    def __init__(
        self,
        algorithm: str,
        reason: str,
    ) -> None:
        self.algorithm = algorithm
        self.reason = reason

        super().__init__(
            (
                f"Encryption algorithm "
                f"'{algorithm}' "
                f"validation failed: "
                f"{reason}."
            )
        )


class InvalidKeySizeError(
    EncryptionError,
):
    """
    Raised when an unsupported key size
    is supplied.
    """

    def __init__(
        self,
        key_size: int,
    ) -> None:
        self.key_size = key_size

        super().__init__(
            (
                "Invalid encryption "
               f"key size: {key_size}."
            )
        )


class InvalidAlgorithmError(
    EncryptionError,
):
    """
    Raised when an unsupported encryption
    algorithm is supplied.
    """

    def __init__(
        self,
        algorithm: str,
    ) -> None:
        self.algorithm = algorithm

        super().__init__(
            (
                "Invalid encryption "
               f"algorithm: '{algorithm}'."
            )
        )