"""
Tests for ai_security.hashing.constants.
"""

from ai_security.hashing.constants import (
    DEFAULT_ENCODING,
    DEFAULT_HASH_ALGORITHM,
    DEFAULT_ITERATIONS,
    DEFAULT_KEY_LENGTH,
    DEFAULT_SALT_LENGTH,
    SUPPORTED_HASH_ALGORITHMS,
)


def test_default_hash_algorithm() -> None:
    """Default algorithm should be sha256."""
    assert DEFAULT_HASH_ALGORITHM == "sha256"


def test_default_encoding() -> None:
    """Default encoding should be utf-8."""
    assert DEFAULT_ENCODING == "utf-8"


def test_default_salt_length() -> None:
    """Salt length should be positive."""
    assert DEFAULT_SALT_LENGTH > 0


def test_default_key_length() -> None:
    """Derived key length should be positive."""
    assert DEFAULT_KEY_LENGTH > 0


def test_default_iterations() -> None:
    """Iteration count should be sufficiently large."""
    assert DEFAULT_ITERATIONS >= 100_000


def test_supported_algorithms() -> None:
    """Supported algorithms should contain common hashes."""
    assert "sha256" in SUPPORTED_HASH_ALGORITHMS
    assert "sha512" in SUPPORTED_HASH_ALGORITHMS
    assert "blake2b" in SUPPORTED_HASH_ALGORITHMS