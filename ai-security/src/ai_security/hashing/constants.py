"""
Constants for the hashing module.
"""

from __future__ import annotations

DEFAULT_HASH_ALGORITHM: str = "sha256"
DEFAULT_ENCODING: str = "utf-8"

DEFAULT_SALT_LENGTH: int = 16
DEFAULT_KEY_LENGTH: int = 32
DEFAULT_ITERATIONS: int = 100_000

SUPPORTED_HASH_ALGORITHMS: frozenset[str] = frozenset(
    {
        "md5",
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512",
        "sha3_224",
        "sha3_256",
        "sha3_384",
        "sha3_512",
        "blake2b",
        "blake2s",
    }
)