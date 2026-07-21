from __future__ import annotations

"""Global pytest fixtures."""

from collections.abc import Generator
from datetime import UTC, datetime
from uuid import uuid4
from app.main import app
import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient   
from app.organizations.repository import OrganizationRepository
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
def organization(self) -> MagicMock:
    """Return organization."""

    organization = MagicMock(spec=Organization)

    organization.id = uuid4()
    organization.name = "Test Organization"
    organization.code = "ORG001"
    organization.email = "org@example.com"
    organization.phone = "+919999999999"
    organization.website = "https://example.com"

    organization.logo_url = "https://example.com/logo.png"
    organization.address = "123 Test Street"
    organization.city = "Hyderabad"
    organization.state = "Telangana"
    organization.country = "India"
    organization.postal_code = "500001"
    organization.timezone = "Asia/Kolkata"

    organization.is_active = True

    organization.created_at = datetime.now(UTC)
    organization.updated_at = datetime.now(UTC)

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

@pytest.fixture
def organization_repository(
    db_session: Session,
) -> OrganizationRepository:
    """Return organization repository."""
    return OrganizationRepository(db_session)


@pytest.fixture
def client() -> TestClient:
    """Return FastAPI test client."""
    return TestClient(app)

@pytest.fixture
def auth_headers(client: TestClient) -> dict[str, str]:
    """Return authenticated headers."""

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "admin@example.com",
            "password": "Password123!",
        },
    )

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}",
    }

@pytest.fixture
def created_user(
    repository: UserRepository,
    organization: Organization,
) -> User:
    """Create a test user."""

    return repository.create(
        email="john@example.com",
        username="john",
        full_name="John Doe",
        password_hash="hashed",
        organization_id=organization.id,
    )