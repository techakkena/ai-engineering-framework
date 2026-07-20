from __future__ import annotations

"""Authentication service."""

from uuid import UUID

from app.auth.jwt import (
    create_access_token,
    decode_access_token,
)
from app.auth.password import verify_password
from app.core.exceptions import (
    AuthenticationException,
    ResourceNotFoundException,
)
from app.models.user import User
from app.repositories.user import UserRepository
from jwt import InvalidTokenError


class AuthenticationService:
    """Authentication business logic."""

    def __init__(
        self,
        repository: UserRepository,
    ) -> None:
        """Initialize the authentication service.

        Args:
            repository: User repository.
        """
        self._repository = repository

    def authenticate(
        self,
        email: str,
        password: str,
    ) -> User:
        """Authenticate a user.

        Args:
            email: User email.
            password: Plain-text password.

        Returns:
            Authenticated user.

        Raises:
            AuthenticationException: If credentials are invalid.
        """
        user = self._repository.get_by_email(email)

        if user is None:
            raise AuthenticationException("Invalid email or password.")

        if not user.is_active:
            raise AuthenticationException("User account is inactive.")

        if not verify_password(password, user.password_hash):
            raise AuthenticationException("Invalid email or password.")

        return user

    def create_token(self, user: User) -> str:
        """Create an access token.

        Args:
            user: Authenticated user.

        Returns:
            JWT access token.
        """
        return create_access_token(
            subject=str(user.id),
            additional_claims={
                "email": user.email,
                "username": user.username,
                "is_superuser": user.is_superuser,
            },
        )

    def get_current_user(
        self,
        token: str,
    ) -> User:
        """Retrieve the authenticated user.

        Args:
            token: JWT access token.

        Returns:
            Authenticated user.

        Raises:
            AuthenticationException: If the token is invalid.
            ResourceNotFoundException: If the user no longer exists.
        """
        try:
            payload = decode_access_token(token)
        except InvalidTokenError as exc:
            raise AuthenticationException("Invalid access token.") from exc

        user_id = UUID(payload["sub"])

        user = self._repository.get_by_id(user_id)

        if user is None:
            raise ResourceNotFoundException("User")

        return user