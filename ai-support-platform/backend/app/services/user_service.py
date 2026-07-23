"""User service."""

from __future__ import annotations

from uuid import UUID

from app.auth.password import hash_password
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    """Service for user management."""

    def __init__(
        self,
        repository: UserRepository,
    ) -> None:
        """Initialize the service.

        Args:
            repository: User repository.
        """
        self._repository = repository

    def list_users(
        self,
        offset: int = 0,
        limit: int = 100,
    ) -> list[User]:
        """Return a paginated list of users.

        Args:
            offset: Number of users to skip before returning results.
            limit: Maximum number of users to return.

        Returns:
            A list of users.
        """
        return self._repository.list(
            offset=offset,
            limit=limit,
        )

    def get_user(
        self,
        user_id: UUID,
    ) -> User:
        """Return a user by identifier.

        Args:
            user_id: User identifier.

        Raises:
            ValueError: If the user does not exist.

        Returns:
            User instance.
        """
        user = self._repository.get(user_id)

        if user is None:
            raise ValueError("User not found.")

        return user

    def create_user(
        self,
        data: UserCreate,
        organization_id: UUID,
    ) -> User:
        """Create a new user.

        Args:
            data: User payload.
            organization_id: Organization identifier.

        Raises:
            ValueError: Duplicate email or username.

        Returns:
            Created user.
        """
        if self._repository.exists_by_email(data.email):
            raise ValueError("Email already exists.")

        if self._repository.exists_by_username(data.username):
            raise ValueError("Username already exists.")

        password_hash = hash_password(data.password)

        user = User(
            email=data.email,
            username=data.username,
            full_name=data.full_name,
            password_hash=password_hash,
            organization_id=organization_id,
        )
        user = self._repository.create(user)
        self._repository.session.commit()
        self._repository.session.refresh(user)

        return user

    def update_user(
        self,
        user_id: UUID,
        data: UserUpdate,
    ) -> User:
        """Update an existing user.

        Args:
            user_id: User identifier.
            data: Update payload.

        Raises:
            ValueError: User not found or duplicate fields.

        Returns:
            Updated user.
        """
        user = self.get_user(user_id)

        if (
            data.email
            and data.email != user.email
            and self._repository.exists_by_email(data.email)
        ):
            raise ValueError("Email already exists.")

        if (
            data.username
            and data.username != user.username
            and self._repository.exists_by_username(data.username)
        ):
            raise ValueError("Username already exists.")

        update_data = data.model_dump(exclude_unset=True)

        password = update_data.pop("password", None)

        if password is not None:
            update_data["password_hash"] = hash_password(password)

        for field, value in update_data.items():
            setattr(user, field, value)

        return self._repository.update(user)

    def delete_user(
        self,
        user_id: UUID,
    ) -> None:
        """Delete a user.

        Args:
            user_id: User identifier.

        Raises:
            ValueError: If the user does not exist.
        """
        user = self.get_user(user_id)
        self._repository.delete(user)
