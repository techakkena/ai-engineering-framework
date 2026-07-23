"""Tests for UserService."""

from __future__ import annotations

from unittest.mock import MagicMock
from uuid import uuid4

import pytest

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.user_service import UserService


@pytest.fixture
def repository() -> MagicMock:
    """Return mocked repository."""
    return MagicMock()


@pytest.fixture
def service(repository: MagicMock) -> UserService:
    """Return service instance."""
    return UserService(repository)


def build_user() -> User:
    """Build a test user."""
    user = User(
        email="john@example.com",
        username="john",
        full_name="John Doe",
        password_hash="hashed",
        organization_id=uuid4(),
    )
    return user


def test_list_users(
    service: UserService,
    repository: MagicMock,
) -> None:
    """Test listing users."""
    users = [build_user()]

    repository.list.return_value = users

    result = service.list_users()

    assert result == users

    repository.list.assert_called_once_with(
        offset=0,
        limit=100,
    )


def test_get_user_not_found(
    service: UserService,
    repository: MagicMock,
) -> None:
    """Test missing user."""
    repository.get.return_value = None

    with pytest.raises(ValueError):
        service.get_user(uuid4())


def test_create_user_success(
    service: UserService,
    repository: MagicMock,
) -> None:
    """Test creating a user."""
    payload = UserCreate(
        email="john@example.com",
        username="john",
        full_name="John Doe",
        password="Password123!",
    )

    repository.exists_by_email.return_value = False
    repository.exists_by_username.return_value = False

    repository.create.return_value = build_user()

    user = service.create_user(
        payload,
        organization_id=uuid4(),
    )

    assert user.email == payload.email
    repository.create.assert_called_once()


def test_create_duplicate_email(
    service: UserService,
    repository: MagicMock,
) -> None:
    """Test duplicate email."""
    payload = UserCreate(
        email="existing@example.com",
        username="john",
        full_name="John",
        password="Password123!",
    )

    repository.exists_by_email.return_value = True

    with pytest.raises(ValueError):
        service.create_user(
            payload,
            uuid4(),
        )


def test_create_duplicate_username(
    service: UserService,
    repository: MagicMock,
) -> None:
    """Test duplicate username."""
    payload = UserCreate(
        email="john@example.com",
        username="existing",
        full_name="John",
        password="Password123!",
    )

    repository.exists_by_email.return_value = False
    repository.exists_by_username.return_value = True

    with pytest.raises(ValueError):
        service.create_user(
            payload,
            uuid4(),
        )


def test_update_user(
    service: UserService,
    repository: MagicMock,
) -> None:
    """Test updating a user."""
    user = build_user()

    repository.get.return_value = user
    repository.exists_by_email.return_value = False
    repository.exists_by_username.return_value = False
    repository.update.return_value = user

    payload = UserUpdate(
        full_name="Updated Name",
    )

    updated = service.update_user(
        user.id,
        payload,
    )

    assert updated.full_name == "Updated Name"


def test_delete_user(
    service: UserService,
    repository: MagicMock,
) -> None:
    """Test deleting a user."""
    user = build_user()

    repository.get.return_value = user

    service.delete_user(user.id)

    repository.delete.assert_called_once_with(user)


def test_delete_missing_user(
    service: UserService,
    repository: MagicMock,
) -> None:
    """Test deleting unknown user."""
    repository.get.return_value = None

    with pytest.raises(ValueError):
        service.delete_user(uuid4())


def test_update_duplicate_email(
    service: UserService,
    repository: MagicMock,
) -> None:
    """Test duplicate email on update."""
    user = build_user()

    repository.get.return_value = user
    repository.exists_by_email.return_value = True

    payload = UserUpdate(
        email="duplicate@example.com",
    )

    with pytest.raises(ValueError):
        service.update_user(
            user.id,
            payload,
        )


def test_update_duplicate_username(
    service: UserService,
    repository: MagicMock,
) -> None:
    """Test duplicate username on update."""
    user = build_user()

    repository.get.return_value = user
    repository.exists_by_email.return_value = False
    repository.exists_by_username.return_value = True

    payload = UserUpdate(
        username="duplicate",
    )

    with pytest.raises(ValueError):
        service.update_user(
            user.id,
            payload,
        )
