"""
Unit tests for ai_security.encryption.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_security.encryption.exceptions import (
    InvalidEncryptionProviderError,
)
from ai_security.encryption.operations import (
    build_encryption_id,
    is_supported_encryption_provider,
    normalize_encryption_provider,
    validate_encryption_id,
    validate_encryption_provider,
)


# ============================================================================
# normalize_encryption_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        (
            "Cryptography",
            "cryptography",
        ),
        (" OpenSSL ", "openssl"),
        (
            "PyCryptodome",
            "pycryptodome",
        ),
        ("AWS-KMS", "aws-kms"),
        (
            "Azure-Key-Vault",
            "azure-key-vault",
        ),
        ("Google-KMS", "google-kms"),
    ],
)
def test_normalize_encryption_provider(
    provider: str,
    expected: str,
) -> None:
    """Test provider normalization."""
    assert (
        normalize_encryption_provider(
            provider,
        )
        == expected
    )


# ============================================================================
# validate_encryption_provider
# ============================================================================


@pytest.mark.parametrize(
    "provider",
    [
        "cryptography",
        "openssl",
        "pycryptodome",
        "aws-kms",
        "azure-key-vault",
        "google-kms",
    ],
)
def test_validate_encryption_provider(
    provider: str,
) -> None:
    """Test valid providers."""
    assert (
        validate_encryption_provider(
            provider,
        )
        == provider
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "vault",
        "kms",
        "custom",
    ],
)
def test_validate_encryption_provider_invalid(
    provider: str,
) -> None:
    """Invalid providers should raise."""
    with pytest.raises(
        InvalidEncryptionProviderError,
    ):
        validate_encryption_provider(
            provider,
        )


# ============================================================================
# is_supported_encryption_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("cryptography", True),
        ("openssl", True),
        ("pycryptodome", True),
        ("aws-kms", True),
        ("azure-key-vault", True),
        ("google-kms", True),
        ("vault", False),
        ("kms", False),
    ],
)
def test_is_supported_encryption_provider(
    provider: str,
    expected: bool,
) -> None:
    """Test provider support detection."""
    assert (
        is_supported_encryption_provider(
            provider,
        )
        is expected
    )


# ============================================================================
# validate_encryption_id
# ============================================================================


@pytest.mark.parametrize(
    "encryption_id",
    [
        "encryption",
        "encryption_01",
        "encryption-01",
        "runtime123",
    ],
)
def test_validate_encryption_id(
    encryption_id: str,
) -> None:
    """Test valid identifiers."""
    assert (
        validate_encryption_id(
            encryption_id,
        )
        == encryption_id.lower()
    )


@pytest.mark.parametrize(
    "encryption_id",
    [
        "",
        "123encryption",
        "encryption name",
        "@encryption",
    ],
)
def test_validate_encryption_id_invalid(
    encryption_id: str,
) -> None:
    """Invalid identifiers should raise."""
    with pytest.raises(ValueError):
        validate_encryption_id(
            encryption_id,
        )


# ============================================================================
# build_encryption_id
# ============================================================================


def test_build_encryption_id() -> None:
    """Test encryption ID generation."""
    encryption_id = (
        build_encryption_id()
    )

    assert encryption_id.startswith(
        "encryption-",
    )

    pattern = re.compile(
        (
            r"^encryption-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert (
        pattern.fullmatch(
            encryption_id,
        )
        is not None
    )