"""
Framework-independent security utility functions.
"""

from __future__ import annotations

import re

from ai_security.utils.constants import (
    DEFAULT_ENCODING,
    MASK_CHARACTER,
)


class SecurityUtils:
    """Collection of framework-independent security helper methods."""

    @staticmethod
    def mask_secret(
            value: str,
            *,
            visible: int = 4,
        ) -> str:
            """
            Mask a secret while leaving the last ``visible`` characters exposed.
            """
            if visible < 0:
                raise ValueError(
                    "visible must be greater than or equal to zero."
                )

            if len(value) <= visible:
                return value

            if visible == 0:
                return MASK_CHARACTER * len(value)

            return (
                MASK_CHARACTER * (len(value) - visible)
                + value[-visible:]
            )

    @staticmethod
    def constant_time_compare(
        left: str,
        right: str,
    ) -> bool:
        """
        Compare two strings using constant-time comparison.
        """
        from hmac import compare_digest

        return compare_digest(left, right)

    @staticmethod
    def is_strong_password(password: str) -> bool:
        """
        Validate password strength.

        Requirements:
        - Minimum 8 characters
        - One uppercase letter
        - One lowercase letter
        - One digit
        - One special character
        """
        pattern = (
            r"^(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*\d)"
            r"(?=.*[@$!%*?&#])"
            r"[A-Za-z\d@$!%*?&#]{8,}$"
        )

        return re.fullmatch(pattern, password) is not None

    @staticmethod
    def encode(value: str) -> bytes:
        """Encode a string."""
        return value.encode(DEFAULT_ENCODING)

    @staticmethod
    def decode(value: bytes) -> str:
        """Decode bytes."""
        return value.decode(DEFAULT_ENCODING)