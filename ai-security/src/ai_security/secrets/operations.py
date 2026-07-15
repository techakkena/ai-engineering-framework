"""
Framework-independent secret management.
"""

from __future__ import annotations

from dataclasses import dataclass
import secrets

from ai_security.secrets.constants import (
    DEFAULT_SECRET_LENGTH,
    DEFAULT_TOKEN_LENGTH,
)
from ai_security.secrets.exceptions import (
    SecretConfigurationError,
    SecretNotFoundError,
)


@dataclass(slots=True, frozen=True)
class Secret:
    """Represents a stored secret."""

    name: str
    value: str


class SecretManager:
    """
    Simple in-memory secret manager.

    This implementation is framework-independent and intended as a
    reference implementation. Production adapters can integrate with
    AWS Secrets Manager, Azure Key Vault, Google Secret Manager,
    HashiCorp Vault, etc.
    """

    def __init__(self) -> None:
        self._storage: dict[str, str] = {}

    def create_secret(
        self,
        name: str,
        *,
        length: int = DEFAULT_SECRET_LENGTH,
    ) -> Secret:
        """Generate and store a new secret."""
        if length <= 0:
            raise SecretConfigurationError(
                "Secret length must be greater than zero."
            )

        value = secrets.token_urlsafe(length)

        self._storage[name] = value

        return Secret(
            name=name,
            value=value,
        )

    def store_secret(
        self,
        name: str,
        value: str,
    ) -> Secret:
        """Store an existing secret."""
        self._storage[name] = value

        return Secret(
            name=name,
            value=value,
        )

    def get_secret(
        self,
        name: str,
    ) -> Secret:
        """Retrieve a stored secret."""
        if name not in self._storage:
            raise SecretNotFoundError(
                f"Secret '{name}' was not found."
            )

        return Secret(
            name=name,
            value=self._storage[name],
        )

    def delete_secret(
        self,
        name: str,
    ) -> bool:
        """Delete a stored secret."""
        if name not in self._storage:
            raise SecretNotFoundError(
                f"Secret '{name}' was not found."
            )

        del self._storage[name]

        return True

    @staticmethod
    def generate_token(
        *,
        length: int = DEFAULT_TOKEN_LENGTH,
    ) -> str:
        """Generate a secure random token."""
        return secrets.token_urlsafe(length)

    @property
    def count(self) -> int:
        """Return the number of stored secrets."""
        return len(self._storage)