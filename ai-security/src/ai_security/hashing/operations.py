"""
Enterprise hashing operations.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
import secrets

from ai_security.hashing.constants import (
    DEFAULT_ENCODING,
    DEFAULT_HASH_ALGORITHM,
    DEFAULT_ITERATIONS,
    DEFAULT_KEY_LENGTH,
    DEFAULT_SALT_LENGTH,
    SUPPORTED_HASH_ALGORITHMS,
)
from ai_security.hashing.exceptions import (
    HashingAlgorithmError,
    HashVerificationError,
)


@dataclass(frozen=True, slots=True)
class HashResult:
    """Represents a hashing result."""

    algorithm: str
    digest: str
    salt: str | None = None


class HashingService:
    """Framework-independent hashing service."""

    def __init__(
        self,
        algorithm: str = DEFAULT_HASH_ALGORITHM,
        encoding: str = DEFAULT_ENCODING,
    ) -> None:
        if algorithm not in SUPPORTED_HASH_ALGORITHMS:
            raise HashingAlgorithmError(
                f"Unsupported hashing algorithm: {algorithm}"
            )

        self._algorithm = algorithm
        self._encoding = encoding

    @property
    def algorithm(self) -> str:
        """Return the configured algorithm."""
        return self._algorithm

    def hash_text(self, value: str) -> HashResult:
        """Create a deterministic hash of a string."""
        digest = hashlib.new(
            self._algorithm,
            value.encode(self._encoding),
        ).hexdigest()

        return HashResult(
            algorithm=self._algorithm,
            digest=digest,
        )

    def hash_password(
        self,
        password: str,
        *,
        salt: str | None = None,
        iterations: int = DEFAULT_ITERATIONS,
        key_length: int = DEFAULT_KEY_LENGTH,
    ) -> HashResult:
        """Hash a password using PBKDF2-HMAC."""
        salt = salt or secrets.token_hex(DEFAULT_SALT_LENGTH)

        digest = hashlib.pbkdf2_hmac(
            self._algorithm,
            password.encode(self._encoding),
            bytes.fromhex(salt),
            iterations,
            dklen=key_length,
        ).hex()

        return HashResult(
            algorithm=self._algorithm,
            digest=digest,
            salt=salt,
        )

    def verify_hash(self, value: str, expected_digest: str) -> bool:
        """Verify a deterministic hash."""
        actual = self.hash_text(value).digest

        if not hmac.compare_digest(actual, expected_digest):
            raise HashVerificationError("Hash verification failed.")

        return True

    def verify_password(
        self,
        password: str,
        digest: str,
        salt: str,
        *,
        iterations: int = DEFAULT_ITERATIONS,
        key_length: int = DEFAULT_KEY_LENGTH,
    ) -> bool:
        """Verify a PBKDF2 password hash."""
        candidate = self.hash_password(
            password=password,
            salt=salt,
            iterations=iterations,
            key_length=key_length,
        ).digest

        if not hmac.compare_digest(candidate, digest):
            raise HashVerificationError("Password verification failed.")

        return True