"""Operations for the ai_cloud.secrets module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_cloud.secrets.constants import (
    DEFAULT_ENABLED,
    DEFAULT_SECRET_TYPE,
    MAX_SECRET_NAME_LENGTH,
    MIN_SECRET_NAME_LENGTH,
    SUPPORTED_SECRET_TYPES,
)
from ai_cloud.secrets.exceptions import (
    DuplicateSecretError,
    SecretNotFoundError,
    SecretValidationError,
    UnsupportedSecretTypeError,
)


@dataclass(slots=True, frozen=True)
class SecretDefinition:
    """Represents a cloud secret."""

    name: str
    value: str
    secret_type: str = DEFAULT_SECRET_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the secret definition."""
        normalized_name = self.name.strip()
        normalized_value = self.value.strip()

        if not (
            MIN_SECRET_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_SECRET_NAME_LENGTH
        ):
            raise SecretValidationError(
                "Secret name length is outside the allowed range."
            )

        if not normalized_value:
            raise SecretValidationError(
                "Secret value cannot be empty."
            )

        if (
            self.secret_type
            not in SUPPORTED_SECRET_TYPES
        ):
            raise UnsupportedSecretTypeError(
                f"Unsupported secret type: "
                f"{self.secret_type!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized_name,
        )
        object.__setattr__(
            self,
            "value",
            normalized_value,
        )


class SecretRegistry:
    """Registry for secret definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        self._definitions: dict[
            str,
            SecretDefinition,
        ] = {}

    def register(
        self,
        secret: SecretDefinition,
    ) -> None:
        if secret.name in self._definitions:
            raise DuplicateSecretError(
                f"Secret {secret.name!r} is already registered."
            )

        self._definitions[secret.name] = secret

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._definitions:
            raise SecretNotFoundError(
                f"Secret {name!r} is not registered."
            )

        del self._definitions[name]

    def get(
        self,
        name: str,
    ) -> SecretDefinition:
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise SecretNotFoundError(
                f"Secret {name!r} is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._definitions

    def clear(self) -> None:
        self._definitions.clear()

    def list(
        self,
    ) -> tuple[
        SecretDefinition,
        ...,
    ]:
        return tuple(
            self._definitions.values()
        )

    def __len__(self) -> int:
        return len(self._definitions)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_secret(
    *,
    name: str,
    value: str,
    secret_type: str = DEFAULT_SECRET_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> SecretDefinition:
    """Build a validated secret."""

    return SecretDefinition(
        name=name,
        value=value,
        secret_type=secret_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "SecretDefinition",
    "SecretRegistry",
    "build_secret",
]