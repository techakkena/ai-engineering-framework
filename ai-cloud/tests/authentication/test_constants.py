"""Operations for the ai_cloud.authentication module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_cloud.authentication.constants import (
    DEFAULT_AUTHENTICATION_TYPE,
    DEFAULT_ENABLED,
    MAX_AUTHENTICATION_NAME_LENGTH,
    MIN_AUTHENTICATION_NAME_LENGTH,
    SUPPORTED_AUTHENTICATION_TYPES,
)
from ai_cloud.authentication.exceptions import (
    AuthenticationNotFoundError,
    AuthenticationValidationError,
    DuplicateAuthenticationError,
    UnsupportedAuthenticationTypeError,
)


@dataclass(slots=True, frozen=True)
class AuthenticationDefinition:
    """Represents an authentication configuration."""

    name: str
    credential: str
    authentication_type: str = DEFAULT_AUTHENTICATION_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the authentication definition."""
        normalized_name = self.name.strip()
        normalized_credential = self.credential.strip()

        if not (
            MIN_AUTHENTICATION_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_AUTHENTICATION_NAME_LENGTH
        ):
            raise AuthenticationValidationError(
                "Authentication name length is outside the allowed range."
            )

        if not normalized_credential:
            raise AuthenticationValidationError(
                "Credential cannot be empty."
            )

        if (
            self.authentication_type
            not in SUPPORTED_AUTHENTICATION_TYPES
        ):
            raise UnsupportedAuthenticationTypeError(
                f"Unsupported authentication type: "
                f"{self.authentication_type!r}."
            )

        object.__setattr__(self, "name", normalized_name)
        object.__setattr__(
            self,
            "credential",
            normalized_credential,
        )


class AuthenticationRegistry:
    """Registry for authentication definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        self._definitions: dict[
            str,
            AuthenticationDefinition,
        ] = {}

    def register(
        self,
        authentication: AuthenticationDefinition,
    ) -> None:
        if authentication.name in self._definitions:
            raise DuplicateAuthenticationError(
                f"Authentication "
                f"{authentication.name!r} "
                "is already registered."
            )

        self._definitions[
            authentication.name
        ] = authentication

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._definitions:
            raise AuthenticationNotFoundError(
                f"Authentication {name!r} "
                "is not registered."
            )

        del self._definitions[name]

    def get(
        self,
        name: str,
    ) -> AuthenticationDefinition:
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise AuthenticationNotFoundError(
                f"Authentication {name!r} "
                "is not registered."
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
        AuthenticationDefinition,
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


def build_authentication(
    *,
    name: str,
    credential: str,
    authentication_type: str = DEFAULT_AUTHENTICATION_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> AuthenticationDefinition:
    """Build a validated authentication definition."""

    return AuthenticationDefinition(
        name=name,
        credential=credential,
        authentication_type=authentication_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "AuthenticationDefinition",
    "AuthenticationRegistry",
    "build_authentication",
]