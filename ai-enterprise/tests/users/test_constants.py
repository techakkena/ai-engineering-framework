"""Operations for the ai_enterprise.users module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_enterprise.users.constants import (
    DEFAULT_ENABLED,
    DEFAULT_USER_ROLE,
    MAX_USERNAME_LENGTH,
    MIN_USERNAME_LENGTH,
    SUPPORTED_USER_ROLES,
)
from ai_enterprise.users.exceptions import (
    DuplicateUserError,
    UnsupportedUserRoleError,
    UserNotFoundError,
    UserValidationError,
)


@dataclass(slots=True, frozen=True)
class EnterpriseUser:
    """Represents an enterprise user."""

    username: str
    email: str
    role: str = DEFAULT_USER_ROLE
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the user."""
        username = self.username.strip()
        email = self.email.strip()

        if not (
            MIN_USERNAME_LENGTH
            <= len(username)
            <= MAX_USERNAME_LENGTH
        ):
            raise UserValidationError(
                "Username length is outside the allowed range."
            )

        if "@" not in email:
            raise UserValidationError(
                "Invalid email address."
            )

        if self.role not in SUPPORTED_USER_ROLES:
            raise UnsupportedUserRoleError(
                f"Unsupported role: {self.role!r}."
            )

        object.__setattr__(self, "username", username)
        object.__setattr__(self, "email", email)


class UserRegistry:
    """Registry for enterprise users."""

    __slots__ = ("_users",)

    def __init__(self) -> None:
        self._users: dict[str, EnterpriseUser] = {}

    def register(
        self,
        user: EnterpriseUser,
    ) -> None:
        if user.username in self._users:
            raise DuplicateUserError(
                f"User {user.username!r} is already registered."
            )

        self._users[user.username] = user

    def unregister(
        self,
        username: str,
    ) -> None:
        if username not in self._users:
            raise UserNotFoundError(
                f"User {username!r} is not registered."
            )

        del self._users[username]

    def get(
        self,
        username: str,
    ) -> EnterpriseUser:
        try:
            return self._users[username]
        except KeyError as exc:
            raise UserNotFoundError(
                f"User {username!r} is not registered."
            ) from exc

    def exists(
        self,
        username: str,
    ) -> bool:
        return username in self._users

    def clear(self) -> None:
        self._users.clear()

    def list(self) -> tuple[EnterpriseUser, ...]:
        return tuple(self._users.values())

    def __len__(self) -> int:
        return len(self._users)

    def __contains__(
        self,
        username: object,
    ) -> bool:
        return (
            isinstance(username, str)
            and username in self._users
        )


def build_user(
    *,
    username: str,
    email: str,
    role: str = DEFAULT_USER_ROLE,
    enabled: bool = DEFAULT_ENABLED,
) -> EnterpriseUser:
    """Build a validated enterprise user."""

    return EnterpriseUser(
        username=username,
        email=email,
        role=role,
        enabled=enabled,
    )


__all__ = [
    "EnterpriseUser",
    "UserRegistry",
    "build_user",
]