"""
Tests for ai_security.hashing.operations.
"""

import pytest

from ai_security.hashing.exceptions import (
    HashVerificationError,
    HashingAlgorithmError,
)
from ai_security.hashing.operations import HashResult, HashingService


def test_service_default_algorithm() -> None:
    """Default algorithm should be sha256."""
    service = HashingService()
    assert service.algorithm == "sha256"


def test_invalid_algorithm() -> None:
    """Unsupported algorithms should raise an error."""
    with pytest.raises(HashingAlgorithmError):
        HashingService("invalid")


def test_hash_text() -> None:
    """Text hashing should be deterministic."""
    service = HashingService()

    result = service.hash_text("hello")

    assert isinstance(result, HashResult)
    assert result.algorithm == "sha256"
    assert result.salt is None
    assert len(result.digest) == 64


def test_hash_text_same_input_same_digest() -> None:
    """Hashing the same text twice should produce identical digests."""
    service = HashingService()

    first = service.hash_text("framework")
    second = service.hash_text("framework")

    assert first.digest == second.digest


def test_hash_password() -> None:
    """Password hashing should generate a salt."""
    service = HashingService()

    result = service.hash_password("secret123")

    assert isinstance(result, HashResult)
    assert result.salt is not None
    assert len(result.salt) == 32
    assert len(result.digest) == 64


def test_verify_hash_success() -> None:
    """Hash verification should succeed."""
    service = HashingService()

    digest = service.hash_text("hello").digest

    assert service.verify_hash("hello", digest)


def test_verify_hash_failure() -> None:
    """Hash verification should fail."""
    service = HashingService()

    digest = service.hash_text("hello").digest

    with pytest.raises(HashVerificationError):
        service.verify_hash("world", digest)


def test_verify_password_success() -> None:
    """Password verification should succeed."""
    service = HashingService()

    result = service.hash_password("password123")

    assert result.salt is not None

    assert service.verify_password(
        "password123",
        result.digest,
        result.salt,
    )


def test_verify_password_failure() -> None:
    """Password verification should fail."""
    service = HashingService()

    result = service.hash_password("password123")

    assert result.salt is not None

    with pytest.raises(HashVerificationError):
        service.verify_password(
            "wrong-password",
            result.digest,
            result.salt,
        )


def test_different_passwords_generate_different_hashes() -> None:
    """Different passwords should produce different hashes."""
    service = HashingService()

    first = service.hash_password("password-one")
    second = service.hash_password("password-two")

    assert first.digest != second.digest