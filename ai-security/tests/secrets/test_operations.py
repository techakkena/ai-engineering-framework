"""
Tests for ai_security.secrets.operations.
"""

import pytest

from ai_security.secrets.exceptions import (
    SecretConfigurationError,
    SecretNotFoundError,
)
from ai_security.secrets.operations import (
    Secret,
    SecretManager,
)


def test_create_secret() -> None:
    """A secret should be created and stored."""
    manager = SecretManager()

    secret = manager.create_secret("api-key")

    assert isinstance(secret, Secret)
    assert secret.name == "api-key"
    assert isinstance(secret.value, str)
    assert manager.count == 1


def test_create_secret_invalid_length() -> None:
    """Creating a secret with an invalid length should fail."""
    manager = SecretManager()

    with pytest.raises(SecretConfigurationError):
        manager.create_secret("invalid", length=0)


def test_store_secret() -> None:
    """An existing secret should be stored."""
    manager = SecretManager()

    secret = manager.store_secret("db-password", "super-secret")

    assert secret.name == "db-password"
    assert secret.value == "super-secret"
    assert manager.count == 1


def test_get_secret() -> None:
    """A stored secret should be retrievable."""
    manager = SecretManager()

    manager.store_secret("token", "abc123")

    secret = manager.get_secret("token")

    assert secret.name == "token"
    assert secret.value == "abc123"


def test_get_secret_not_found() -> None:
    """Getting a missing secret should raise an exception."""
    manager = SecretManager()

    with pytest.raises(SecretNotFoundError):
        manager.get_secret("missing")


def test_delete_secret() -> None:
    """A stored secret should be deleted."""
    manager = SecretManager()

    manager.store_secret("secret", "value")

    assert manager.delete_secret("secret") is True
    assert manager.count == 0


def test_delete_secret_not_found() -> None:
    """Deleting a missing secret should raise an exception."""
    manager = SecretManager()

    with pytest.raises(SecretNotFoundError):
        manager.delete_secret("missing")


def test_generate_token() -> None:
    """A secure token should be generated."""
    token = SecretManager.generate_token()

    assert isinstance(token, str)
    assert len(token) > 0


def test_generate_tokens_are_unique() -> None:
    """Generated tokens should be unique."""
    token1 = SecretManager.generate_token()
    token2 = SecretManager.generate_token()

    assert token1 != token2


def test_secret_count() -> None:
    """The secret count should reflect stored secrets."""
    manager = SecretManager()

    assert manager.count == 0

    manager.store_secret("one", "1")
    manager.store_secret("two", "2")

    assert manager.count == 2