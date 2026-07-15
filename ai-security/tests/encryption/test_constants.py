"""
Unit tests for ai_security.encryption.constants.
"""

from __future__ import annotations

from ai_security.encryption.constants import (
    AES_128_GCM,
    AES_192_GCM,
    AES_256_GCM,
    AWS_KMS,
    AZURE_KEY_VAULT,
    CHACHA20_POLY1305,
    CRYPTOGRAPHY,
    DEFAULT_ENCRYPTION_ALGORITHM,
    DEFAULT_IV_SIZE,
    DEFAULT_KEY_SIZE,
    DEFAULT_NONCE_SIZE,
    DEFAULT_PROVIDER,
    DEFAULT_RETRIES,
    DEFAULT_TIMEOUT,
    GOOGLE_KMS,
    KEY_SIZE_128,
    KEY_SIZE_192,
    KEY_SIZE_256,
    OPENSSL,
    PYCRYPTODOME,
    SUPPORTED_ENCRYPTION_ALGORITHMS,
    SUPPORTED_ENCRYPTION_PROVIDERS,
    SUPPORTED_KEY_SIZES,
)


def test_encryption_defaults() -> None:
    """Test encryption default configuration."""
    assert DEFAULT_PROVIDER == CRYPTOGRAPHY
    assert DEFAULT_ENCRYPTION_ALGORITHM == AES_256_GCM
    assert DEFAULT_KEY_SIZE == 256


def test_supported_encryption_providers() -> None:
    """Test supported encryption providers."""
    expected = {
        CRYPTOGRAPHY,
        OPENSSL,
        PYCRYPTODOME,
        AWS_KMS,
        AZURE_KEY_VAULT,
        GOOGLE_KMS,
    }

    assert (
        SUPPORTED_ENCRYPTION_PROVIDERS
        == expected
    )


def test_supported_encryption_providers_are_immutable() -> None:
    """Supported providers should be immutable."""
    assert isinstance(
        SUPPORTED_ENCRYPTION_PROVIDERS,
        frozenset,
    )


def test_supported_algorithms() -> None:
    """Test supported encryption algorithms."""
    expected = {
        AES_128_GCM,
        AES_192_GCM,
        AES_256_GCM,
        CHACHA20_POLY1305,
    }

    assert (
        SUPPORTED_ENCRYPTION_ALGORITHMS
        == expected
    )


def test_supported_algorithms_are_immutable() -> None:
    """Supported algorithms should be immutable."""
    assert isinstance(
        SUPPORTED_ENCRYPTION_ALGORITHMS,
        frozenset,
    )


def test_supported_key_sizes() -> None:
    """Test supported key sizes."""
    expected = {
        KEY_SIZE_128,
        KEY_SIZE_192,
        KEY_SIZE_256,
    }

    assert SUPPORTED_KEY_SIZES == expected


def test_supported_key_sizes_are_immutable() -> None:
    """Supported key sizes should be immutable."""
    assert isinstance(
        SUPPORTED_KEY_SIZES,
        frozenset,
    )


def test_nonce_and_iv_sizes() -> None:
    """Test nonce and IV defaults."""
    assert DEFAULT_NONCE_SIZE == 12
    assert DEFAULT_IV_SIZE == 16


def test_encryption_configuration_defaults() -> None:
    """Test configuration defaults."""
    assert DEFAULT_TIMEOUT == 30
    assert DEFAULT_RETRIES == 3