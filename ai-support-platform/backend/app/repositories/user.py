from __future__ import annotations

"""User repository."""

from uuid import UUID

from app.models.user import User
from app.repositories.base import BaseRepository
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import func

class UserRepository(BaseRepository[User]):
    """Repository for user entities."""

    def __init__(
        self,
        session: Session,
    ) -> None:
        """Initialize the repository.

        Args:
            session: Active database session.
        """
        super().__init__(
            session=session,
            model=User,
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        """Return a user by email.

        Args:
            email: User email address.

        Returns:
            User if found; otherwise None.
        """
        statement = (
            select(User)
            .where(
                User.email == email,
                User.is_deleted.is_(False),
            )
        )

        return self.session.scalar(statement)

    def get_by_username(
        self,
        username: str,
    ) -> User | None:
        """Return a user by username.

        Args:
            username: Username.

        Returns:
            User if found; otherwise None.
        """
        statement = (
            select(User)
            .where(
                User.username == username,
                User.is_deleted.is_(False),
            )
        )

        return self.session.scalar(statement)

    def exists_by_email(
        self,
        email: str,
    ) -> bool:
        """Return whether a user exists for the given email.

        Args:
            email: User email.

        Returns:
            True if the user exists; otherwise False.
        """
        return self.get_by_email(email) is not None

    def exists_by_username(
        self,
        username: str,
    ) -> bool:
        """Return whether a user exists for the given username.

        Args:
            username: Username.

        Returns:
            True if the user exists; otherwise False.
        """
        return self.get_by_username(username) is not None

    def create(
        self,
        email: str,
        username: str,
        full_name: str | None,
        password_hash: str,
        organization_id: UUID,
    ) -> User:
        print(f"repository.create() organization_id = {organization_id!r}")
        """Create a new user."""

        user = User(
            email=email,
            username=username,
            full_name=full_name,
            password_hash=password_hash,
            organization_id=organization_id,
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user

    def list(
        self,
        skip: int = 0,
        limit: int = 100,
    ) -> list[User]:
        """Return users."""

        statement = (
            select(User)
            .where(User.is_deleted.is_(False))
            .offset(skip)
            .limit(limit)
        )

        return list(self.session.scalars(statement).all())


    def get(
        self,
        user_id: UUID,
    ) -> User | None:
        """Return user by id."""

        statement = (
            select(User)
            .where(
                User.id == user_id,
                User.is_deleted.is_(False),
            )
        )

        return self.session.scalar(statement)


    def update(
        self,
        user: User,
    ) -> User:
        """Persist user updates."""

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user


    def delete(
        self,
        user: User,
    ) -> None:
        """Soft delete user."""

        user.is_deleted = True

        self.session.add(user)
        self.session.commit()


    def count(
        self,
    ) -> int:
        """Return total active users."""

        statement = (
            select(func.count())
            .select_from(User)
            .where(User.is_deleted.is_(False))
        )

        return self.session.scalar(statement) or 0