"""Global pytest fixtures."""

from __future__ import annotations

from collections.abc import Callable, Generator
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from slugify import slugify
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth.password import hash_password
from app.database.session import get_db
from app.email.constants import (
    EmailPriority,
    EmailProvider,
    EmailStatus,
    EmailTemplate,
)
from app.email.models import Email
from app.files.constants import (
    FileCategory,
    FileProvider,
    FileStatus,
)
from app.files.models import File
from app.knowledge.models import KnowledgeArticle
from app.knowledge.repository import KnowledgeRepository
from app.knowledge.types import KnowledgeStatus
from app.main import app
from app.models.organization import Organization
from app.models.ticket import Ticket
from app.models.user import User
from app.organizations.repository import OrganizationRepository
from app.repositories.project import ProjectRepository
from app.repositories.user import UserRepository
from app.tests.database import (
    create_database,
    drop_database,
    get_db_session,
)
from app.tickets.repository import TicketRepository


@pytest.fixture(autouse=True)
def setup_database() -> Generator[None]:
    """Create and destroy the test database."""
    create_database()

    yield

    drop_database()


@pytest.fixture
def db_session() -> Generator[Session]:
    """Provide a database session."""
    session = next(get_db_session())

    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture
def organization(
    db_session: Session,
) -> Organization:
    """Create a test organization."""
    unique = uuid4().hex[:8]

    organization = Organization(
        name=f"Organization {unique}",
        code=f"ORG-{unique}",
        email=f"{unique}@example.com",
        phone="+919999999999",
        website="https://example.com",
        logo_url="https://example.com/logo.png",
        address="123 Test Street",
        city="Hyderabad",
        state="Telangana",
        country="India",
        postal_code="500001",
        timezone="Asia/Kolkata",
        is_active=True,
    )

    db_session.add(organization)
    db_session.commit()
    db_session.refresh(organization)

    return organization


@pytest.fixture
def user(
    db_session: Session,
    organization: Organization,
) -> User:
    """Return the test admin user."""
    user = db_session.scalar(
        select(User).where(
            User.email == "admin@example.com",
        )
    )

    if user is not None:
        return user

    user = User(
        organization_id=organization.id,
        email="admin@example.com",
        username="admin",
        full_name="Test Admin",
        password_hash=hash_password("Password123!"),
        is_active=True,
        is_superuser=True,
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    return user


@pytest.fixture
def ticket(
    db_session: Session,
    organization: Organization,
    user: User,
) -> Ticket:
    """Create a test ticket."""
    ticket = Ticket(
        organization_id=organization.id,
        created_by=user.id,
        assigned_to=user.id,
        title="Sample Ticket",
        description="Sample ticket description",
        status="open",
        priority="medium",
        is_active=True,
    )

    db_session.add(ticket)
    db_session.commit()
    db_session.refresh(ticket)

    return ticket


@pytest.fixture
def repository(
    db_session: Session,
) -> UserRepository:
    """Return user repository."""
    return UserRepository(db_session)


@pytest.fixture
def organization_repository(
    db_session: Session,
) -> OrganizationRepository:
    """Return organization repository."""
    return OrganizationRepository(db_session)


@pytest.fixture
def ticket_repository(
    db_session: Session,
) -> TicketRepository:
    """Return ticket repository."""
    return TicketRepository(db_session)


@pytest.fixture
def client() -> Generator[TestClient]:
    """Return FastAPI test client using the test database."""
    app.dependency_overrides[get_db] = get_db_session

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def auth_headers(
    client: TestClient,
    user: User,
) -> dict[str, str]:
    """Return authenticated headers."""
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "admin@example.com",
            "password": "Password123!",
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}",
    }


@pytest.fixture
def created_user(
    repository: UserRepository,
    organization: Organization,
) -> User:
    """Create a persisted user."""
    user = User(
        email="john@example.com",
        username="john",
        full_name="John Doe",
        password_hash="hashed",
        organization_id=organization.id,
    )

    return repository.create(user)


@pytest.fixture
def project_repository(
    db_session: Session,
) -> ProjectRepository:
    """Return project repository."""
    return ProjectRepository(db_session)


@pytest.fixture
def knowledge_repository(
    db_session: Session,
) -> KnowledgeRepository:
    """Return knowledge repository."""
    return KnowledgeRepository(db_session)


@pytest.fixture
def knowledge_article(
    db_session: Session,
    organization: Organization,
    user: User,
) -> KnowledgeArticle:
    """Create a persisted knowledge article."""
    article = KnowledgeArticle(
        organization_id=organization.id,
        title="Getting Started",
        slug=slugify("Getting Started"),
        summary="Knowledge summary",
        content="Knowledge content",
        category="General",
        tags="docs,help",
        status=KnowledgeStatus.DRAFT,
        version=1,
        is_published=False,
        is_deleted=False,
        author_id=user.id,
    )

    db_session.add(article)
    db_session.commit()
    db_session.refresh(article)

    return article


@pytest.fixture
def knowledge_article_factory(
    db_session: Session,
    organization: Organization,
    user: User,
) -> Callable[..., KnowledgeArticle]:
    """Return a persisted knowledge article factory."""

    def factory(
        title: str = "Article",
    ) -> KnowledgeArticle:
        article = KnowledgeArticle(
            organization_id=organization.id,
            author_id=user.id,
            title=title,
            slug=slugify(title),
            summary="Summary",
            content="Content",
            category="General",
            tags="tag1,tag2",
            status=KnowledgeStatus.DRAFT,
            version=1,
            is_published=False,
            is_deleted=False,
        )

        db_session.add(article)
        db_session.commit()
        db_session.refresh(article)

        return article

    return factory


@pytest.fixture
def email(
    db_session: Session,
    organization: Organization,
    user: User,
) -> Email:
    """Create a persisted email."""
    email = Email(
        organization_id=organization.id,
        sender_id=user.id,
        recipient="customer@example.com",
        subject="Test Subject",
        body="Test email body",
        cc=None,
        bcc=None,
        template=EmailTemplate.GENERIC,
        provider=EmailProvider.SMTP,
        priority=EmailPriority.NORMAL,
        status=EmailStatus.PENDING,
        retry_count=0,
        is_deleted=False,
    )

    db_session.add(email)
    db_session.commit()
    db_session.refresh(email)

    return email


@pytest.fixture
def email_factory(
    db_session: Session,
    organization: Organization,
    user: User,
) -> Callable[..., Email]:
    """Return a persisted email factory."""

    def factory(
        subject: str = "Test Subject",
        recipient: str = "customer@example.com",
        status: EmailStatus = EmailStatus.PENDING,
    ) -> Email:
        email = Email(
            organization_id=organization.id,
            sender_id=user.id,
            recipient=recipient,
            subject=subject,
            body="Test email body",
            cc=None,
            bcc=None,
            template=EmailTemplate.GENERIC,
            provider=EmailProvider.SMTP,
            priority=EmailPriority.NORMAL,
            status=status,
            retry_count=0,
            is_deleted=False,
        )

        db_session.add(email)
        db_session.commit()
        db_session.refresh(email)

        return email

    return factory


@pytest.fixture
def file_factory(
    db_session: Session,
    organization: Organization,
    user: User,
) -> Callable[..., File]:
    """Return a factory for creating files."""

    def factory(
        **kwargs: object,
    ) -> File:
        file = File(
            organization_id=organization.id,
            uploaded_by_id=user.id,
            filename=kwargs.get(
                "filename",
                "document.pdf",
            ),
            original_filename=kwargs.get(
                "original_filename",
                "document.pdf",
            ),
            content_type=kwargs.get(
                "content_type",
                "application/pdf",
            ),
            size=kwargs.get(
                "size",
                1024,
            ),
            checksum=kwargs.get(
                "checksum",
                "abc123checksum",
            ),
            storage_path=kwargs.get(
                "storage_path",
                "uploads/document.pdf",
            ),
            provider=kwargs.get(
                "provider",
                FileProvider.LOCAL,
            ),
            category=kwargs.get(
                "category",
                FileCategory.DOCUMENT,
            ),
            status=kwargs.get(
                "status",
                FileStatus.ACTIVE,
            ),
        )

        db_session.add(file)
        db_session.commit()
        db_session.refresh(file)

        return file

    return factory


@pytest.fixture
def file(
    file_factory: Callable[..., File],
) -> File:
    """Return a persisted file."""
    return file_factory()
