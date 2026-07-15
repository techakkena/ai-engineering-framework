"""
Constants for ai_security.encryption.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_PROVIDER: Final[str] = "cryptography"

DEFAULT_ENCRYPTION_ALGORITHM: Final[str] = "aes-256-gcm"

DEFAULT_KEY_SIZE: Final[int] = 256

# ============================================================================
# Providers
# ============================================================================

CRYPTOGRAPHY: Final[str] = "cryptography"

OPENSSL: Final[str] = "openssl"

PYCRYPTODOME: Final[str] = "pycryptodome"

AWS_KMS: Final[str] = "aws-kms"

AZURE_KEY_VAULT: Final[str] = "azure-key-vault"

GOOGLE_KMS: Final[str] = "google-kms"

SUPPORTED_ENCRYPTION_PROVIDERS: Final[
    frozenset[str]
] = frozenset(
    {
        CRYPTOGRAPHY,
        OPENSSL,
        PYCRYPTODOME,
        AWS_KMS,
        AZURE_KEY_VAULT,
        GOOGLE_KMS,
    }
)

# ============================================================================
# Algorithms
# ============================================================================

AES_128_GCM: Final[str] = "aes-128-gcm"

AES_192_GCM: Final[str] = "aes-192-gcm"

AES_256_GCM: Final[str] = "aes-256-gcm"

CHACHA20_POLY1305: Final[str] = (
    "chacha20-poly1305"
)

SUPPORTED_ENCRYPTION_ALGORITHMS: Final[
    frozenset[str]
] = frozenset(
    {
        AES_128_GCM,
        AES_192_GCM,
        AES_256_GCM,
        CHACHA20_POLY1305,
    }
)

# ============================================================================
# Key Sizes
# ============================================================================

KEY_SIZE_128: Final[int] = 128

KEY_SIZE_192: Final[int] = 192

KEY_SIZE_256: Final[int] = 256

SUPPORTED_KEY_SIZES: Final[
    frozenset[int]
] = frozenset(
    {
        KEY_SIZE_128,
        KEY_SIZE_192,
        KEY_SIZE_256,
    }
)

# ============================================================================
# Nonce / IV
# ============================================================================

DEFAULT_NONCE_SIZE: Final[int] = 12

DEFAULT_IV_SIZE: Final[int] = 16

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 30

DEFAULT_RETRIES: Final[int] = 3