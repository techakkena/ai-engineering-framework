from __future__ import annotations

"""Global pytest fixtures."""

from collections.abc import Generator
from uuid import uuid4

import pytest
from sqlalchemy.orm import Session

# Ensure all ORM mappers are registered before tests run.
from app.models.organization import Organization
from app.models.user import User
from app.repositories.user import UserRepository
from app.tests.database import (
    create_database,
    drop_database,
    get_db_session,
)


@pytest.fixture(scope="session", autouse=True)
def setup_database() -> Generator[None]:
    """Create the test database before the test session starts."""
    create_database()

    yield

    drop_database()


@pytest.fixture
def db_session() -> Generator[Session]:
    """Provide a database session for each test."""
    db = next(get_db_session())

    try:
        yield db
    finally:
        db.rollback()
        db.close()


@pytest.fixture
def organization(
    db_session: Session,
) -> Organization:
    """Create a test organization."""
    unique = uuid4().hex[:8]

    organization = Organization(
        name=f"Test Organization {unique}",
        code=f"ORG-{unique}",
        email=f"{unique}@example.com",
        phone="+919999999999",
        website="https://example.com",
        is_active=True,
    )

    db_session.add(organization)
    db_session.flush()
    db_session.refresh(organization)

    return organization

@pytest.fixture
def user(
    db_session: Session,
    organization: Organization,
) -> User:
    """Create a test user."""
    unique = uuid4().hex[:8]

    user = User(
        organization_id=organization.id,
        email=f"{unique}@example.com",
        username=f"user_{unique}",
        full_name="John Smith",
        password_hash="hashed-password",
        is_active=True,
        is_superuser=False,
    )

    db_session.add(user)
    db_session.flush()
    db_session.refresh(user)

    return user
    
@pytest.fixture
def repository(db_session):
    """Return a UserRepository for tests."""
    return UserRepository(db_session)