from __future__ import annotations

"""Tests for UserRepository."""

from uuid import uuid4

import pytest

from app.repositories.user import UserRepository


@pytest.fixture
def repository(db_session):
    """Create repository."""
    return UserRepository(db_session)


def test_create_user(repository: UserRepository) -> None:
    """Test creating a user."""
    user = repository.create(
        email="john@example.com",
        username="john",
        full_name="John Doe",
        password_hash="hashed-password",
        organization_id=uuid4(),
    )

    assert user.id is not None
    assert user.email == "john@example.com"
    assert user.username == "john"
    assert user.full_name == "John Doe"


def test_get_by_email(repository: UserRepository) -> None:
    """Test get user by email."""
    repository.create(
        email="alice@example.com",
        username="alice",
        full_name="Alice",
        password_hash="hash",
        organization_id=uuid4(),
    )

    user = repository.get_by_email("alice@example.com")

    assert user is not None
    assert user.email == "alice@example.com"


def test_get_by_username(repository: UserRepository) -> None:
    """Test get user by username."""
    repository.create(
        email="bob@example.com",
        username="bob",
        full_name="Bob",
        password_hash="hash",
        organization_id=uuid4(),
    )

    user = repository.get_by_username("bob")

    assert user is not None
    assert user.username == "bob"


def test_exists_by_email(repository: UserRepository) -> None:
    """Test email existence."""
    repository.create(
        email="exists@example.com",
        username="exists",
        full_name="Exists",
        password_hash="hash",
        organization_id=uuid4(),
    )

    assert repository.exists_by_email("exists@example.com") is True
    assert repository.exists_by_email("missing@example.com") is False


def test_exists_by_username(repository: UserRepository) -> None:
    """Test username existence."""
    repository.create(
        email="user@example.com",
        username="existinguser",
        full_name="Existing User",
        password_hash="hash",
        organization_id=uuid4(),
    )

    assert repository.exists_by_username("existinguser") is True
    assert repository.exists_by_username("unknown") is False


def test_get_user(repository: UserRepository) -> None:
    """Test get by id."""
    created = repository.create(
        email="id@example.com",
        username="identifier",
        full_name="Identifier",
        password_hash="hash",
        organization_id=uuid4(),
    )

    user = repository.get(created.id)

    assert user is not None
    assert user.id == created.id


def test_list_users(repository: UserRepository) -> None:
    """Test listing users."""
    repository.create(
        email="one@example.com",
        username="one",
        full_name="One",
        password_hash="hash",
        organization_id=uuid4(),
    )

    repository.create(
        email="two@example.com",
        username="two",
        full_name="Two",
        password_hash="hash",
        organization_id=uuid4(),
    )

    users = repository.list()

    assert len(users) >= 2


def test_update_user(repository: UserRepository) -> None:
    """Test updating user."""
    user = repository.create(
        email="update@example.com",
        username="update",
        full_name="Before",
        password_hash="hash",
        organization_id=uuid4(),
    )

    user.full_name = "After"

    updated = repository.update(user)

    assert updated.full_name == "After"


def test_delete_user(repository: UserRepository) -> None:
    """Test soft delete."""
    user = repository.create(
        email="delete@example.com",
        username="delete",
        full_name="Delete",
        password_hash="hash",
        organization_id=uuid4(),
    )

    repository.delete(user)

    deleted = repository.get(user.id)

    assert deleted is None


def test_count(repository: UserRepository) -> None:
    """Test user count."""
    count_before = repository.count()

    repository.create(
        email="count@example.com",
        username="count",
        full_name="Counter",
        password_hash="hash",
        organization_id=uuid4(),
    )

    count_after = repository.count()

    assert count_after == count_before + 1
