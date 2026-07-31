"""Global pytest fixtures."""

from __future__ import annotations

from collections.abc import Callable, Generator
from datetime import UTC, datetime, timedelta
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from slugify import slugify
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.ai.chat.constants import ConversationStatus, MessageStatus, MessageType
from app.ai.chat.models import Conversation, ConversationMessage
from app.ai.chat.repository import ConversationRepository
from app.ai.chat.service import ConversationService
from app.ai.embeddings.constants import (
    EmbeddingProvider,
    EmbeddingSourceType,
    EmbeddingStatus,
)
from app.ai.embeddings.models import Embedding
from app.ai.embeddings.repository import AIEmbeddingRepository
from app.ai.embeddings.schemas import EmbeddingCreate
from app.ai.embeddings.service import AIEmbeddingService
from app.ai.knowledge.repository import AIKnowledgeRepository
from app.ai.knowledge.service import AIKnowledgeService
from app.ai.rag.repository import RAGRepository
from app.ai.rag.service import RAGService
from app.ai.repository import AIRepository
from app.ai.service import AIService
from app.ai.vectorstore.repository import VectorStoreRepository
from app.ai.vectorstore.service import VectorStoreService
from app.analytics.repository import AnalyticsRepository
from app.analytics.service import AnalyticsService
from app.audit.models import AuditLog
from app.audit.repository import AuditRepository
from app.audit.service import AuditService
from app.auth.password import hash_password
from app.customers.models import Customer
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
from app.sla.models import SLAEvent, SLAPolicy
from app.tests.database import (
    create_database,
    drop_database,
    get_db_session,
)
from app.tickets.repository import TicketRepository

# ---------------------------------------------------------------------
# Workflow Fixtures
# ---------------------------------------------------------------------
from app.workflows.models import (
    Workflow,
    WorkflowAction,
    WorkflowCondition,
)
from app.workflows.repository import WorkflowRepository
from app.workflows.service import WorkflowService

now = datetime.now(UTC)


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


@pytest.fixture
def audit_repository(
    db_session: Session,
) -> AuditRepository:
    """Return an audit repository."""
    return AuditRepository(db_session)


@pytest.fixture
def audit_service(
    audit_repository: AuditRepository,
) -> AuditService:
    """Return an audit service."""
    return AuditService(audit_repository)


@pytest.fixture
def audit_log(
    db_session: Session,
    organization: Organization,
    user: User,
) -> AuditLog:
    """Create a persisted audit log."""
    audit_log = AuditLog(
        organization_id=organization.id,
        user_id=user.id,
        action="create",
        entity_type="ticket",
        entity_id=uuid4(),
        entity_name="Ticket-1",
        old_values=None,
        new_values={"status": "open"},
        ip_address="127.0.0.1",
        user_agent="pytest",
        request_id="req-123",
        status="success",
    )

    db_session.add(audit_log)
    db_session.commit()
    db_session.refresh(audit_log)

    return audit_log


@pytest.fixture
def sla_policy(
    db_session: Session,
    organization: Organization,
) -> SLAPolicy:
    """Create a persisted SLA policy."""
    policy = SLAPolicy(
        id=uuid4(),
        organization_id=organization.id,
        name="Default SLA",
        description="Default policy",
        priority="medium",
        first_response_minutes=60,
        resolution_minutes=480,
        business_hours_only=False,
        is_active=True,
        created_at=now,
        updated_at=now,
    )

    db_session.add(policy)
    db_session.commit()
    db_session.refresh(policy)

    return policy


@pytest.fixture
def sla_policy_factory(
    db_session: Session,
    organization: Organization,
) -> Callable[..., SLAPolicy]:
    """Return an SLA policy factory."""

    def factory(
        name: str = "Default SLA",
        priority: str = "medium",
        first_response_minutes: int = 60,
        resolution_minutes: int = 480,
        is_active: bool = True,
    ) -> SLAPolicy:
        policy = SLAPolicy(
            id=uuid4(),
            organization_id=organization.id,
            name="Default SLA",
            description="Default policy",
            priority="medium",
            first_response_minutes=60,
            resolution_minutes=480,
            business_hours_only=False,
            is_active=True,
            created_at=now,
            updated_at=now,
        )

        db_session.add(policy)
        db_session.commit()
        db_session.refresh(policy)

        return policy

    return factory


@pytest.fixture
def sla_event(
    db_session: Session,
    ticket: Ticket,
    sla_policy: SLAPolicy,
) -> SLAEvent:
    """Create a persisted SLA event."""
    now = datetime.now(UTC)

    event = SLAEvent(
        id=uuid4(),
        ticket_id=ticket.id,
        policy_id=sla_policy.id,
        started_at=now,
        first_response_due=now,
        resolution_due=now,
        first_response_at=None,
        resolved_at=None,
        first_response_breached=False,
        resolution_breached=False,
    )

    db_session.add(event)
    db_session.commit()
    db_session.refresh(event)

    return event


@pytest.fixture
def sla_event_factory(
    db_session: Session,
    ticket: Ticket,
    sla_policy: SLAPolicy,
) -> Callable[..., SLAEvent]:
    """Return an SLA event factory."""

    def factory(
        *,
        first_response_breached: bool = False,
        resolution_breached: bool = False,
    ) -> SLAEvent:
        now = datetime.now(UTC)

        event = SLAEvent(
            ticket_id=ticket.id,
            policy_id=sla_policy.id,
            started_at=now,
            first_response_due=now + timedelta(minutes=60),
            resolution_due=now + timedelta(minutes=480),
            first_response_breached=first_response_breached,
            resolution_breached=resolution_breached,
        )

        db_session.add(event)
        db_session.commit()
        db_session.refresh(event)

        return event

    return factory


@pytest.fixture
def workflow(
    db_session: Session,
    organization: Organization,
) -> Workflow:
    """Create a workflow fixture."""
    workflow = Workflow(
        organization_id=organization.id,
        name="Default Workflow",
        description="Default workflow",
        trigger="ticket_created",
        is_active=True,
    )

    db_session.add(workflow)
    db_session.commit()
    db_session.refresh(workflow)

    return workflow


@pytest.fixture
def workflow_condition(
    db_session: Session,
    workflow: Workflow,
) -> WorkflowCondition:
    """Create a workflow condition fixture."""
    condition = WorkflowCondition(
        workflow_id=workflow.id,
        field="priority",
        operator="eq",
        value="high",
    )

    db_session.add(condition)
    db_session.commit()
    db_session.refresh(condition)

    return condition


@pytest.fixture
def workflow_action(
    db_session: Session,
    workflow: Workflow,
) -> WorkflowAction:
    """Create a workflow action fixture."""
    action = WorkflowAction(
        workflow_id=workflow.id,
        action="assign_user",
        value="support-agent",
        execution_order=1,
    )

    db_session.add(action)
    db_session.commit()
    db_session.refresh(action)

    return action


@pytest.fixture
def workflow_repository(
    db_session: Session,
) -> WorkflowRepository:
    """Create a workflow repository."""
    return WorkflowRepository(db_session)


@pytest.fixture
def workflow_service(
    workflow_repository: WorkflowRepository,
) -> WorkflowService:
    """Create a workflow service."""
    return WorkflowService(workflow_repository)


@pytest.fixture
def analytics_repository(
    db_session: Session,
) -> AnalyticsRepository:
    """Create a workflow repository."""
    return AnalyticsRepository(db_session)


@pytest.fixture
def analytics_service(
    analytics_repository: AnalyticsRepository,
) -> AnalyticsService:
    """Create a analytics service."""
    return AnalyticsService(analytics_repository)


@pytest.fixture
def ai_repository(
    db_session: Session,
) -> AIRepository:
    """Create an AI repository."""
    return AIRepository(db_session)


@pytest.fixture
def ai_service(
    ai_repository: AIRepository,
) -> AIService:
    """Create an AI service."""
    return AIService(ai_repository)


@pytest.fixture
def conversation(
    organization: Organization,
    user: User,
    customer: Customer,
    ticket: Ticket,
) -> Conversation:
    """Create a conversation fixture."""
    return Conversation(
        id=uuid4(),
        organization_id=organization.id,
        customer_id=customer.id,
        ticket_id=ticket.id,
        created_by=user.id,
        title="Test Conversation",
        provider="openai",
        model="gpt-5.5",
        status=ConversationStatus.ACTIVE,
    )


@pytest.fixture
def conversation_message(
    conversation: Conversation,
) -> ConversationMessage:
    """Create a conversation message fixture."""
    return ConversationMessage(
        id=uuid4(),
        conversation_id=conversation.id,
        role=MessageType.USER,
        content="Hello AI!",
        token_count=5,
        latency_ms=100,
        status=MessageStatus.COMPLETED,
    )


@pytest.fixture
def conversation_repository(
    db_session: Session,
) -> ConversationRepository:
    """Create a conversation repository."""
    return ConversationRepository(db_session)


@pytest.fixture
def conversation_service(
    conversation_repository: ConversationRepository,
) -> ConversationService:
    """Create a conversation service."""
    return ConversationService(conversation_repository)


@pytest.fixture
def ai_knowledge_repository(
    db_session: Session,
) -> AIKnowledgeRepository:
    """Return AI knowledge repository."""
    return AIKnowledgeRepository(db_session)


@pytest.fixture
def ai_knowledge_service(
    ai_knowledge_repository: AIKnowledgeRepository,
) -> AIKnowledgeService:
    """Return AI knowledge service."""
    return AIKnowledgeService(ai_knowledge_repository)


@pytest.fixture
def embedding_repository(
    db_session: Session,
) -> AIEmbeddingRepository:
    """Create an embedding repository."""
    return AIEmbeddingRepository(
        db_session,
    )


@pytest.fixture
def embedding_service(
    embedding_repository: AIEmbeddingRepository,
) -> AIEmbeddingService:
    """Create an embedding service."""
    return AIEmbeddingService(
        embedding_repository,
    )


@pytest.fixture
def embedding(
    db_session: Session,
    organization: Organization,
    user: User,
) -> Embedding:
    """Create a test embedding."""
    embedding = Embedding(
        organization_id=organization.id,
        knowledge_id=None,
        provider=EmbeddingProvider.OPENAI,
        model="text-embedding-3-small",
        source_type=EmbeddingSourceType.DOCUMENT,
        source_id=uuid4(),
        content="Test embedding",
        dimensions=1536,
        vector=[0.1, 0.2, 0.3],
        metadata_json={},
        status=EmbeddingStatus.READY,
        created_by=user.id,
        updated_by=user.id,
    )

    db_session.add(embedding)
    db_session.commit()
    db_session.refresh(embedding)

    return embedding


@pytest.fixture
def embedding_create() -> EmbeddingCreate:
    """Create an embedding request."""
    return EmbeddingCreate(
        provider=EmbeddingProvider.OPENAI,
        model="text-embedding-3-small",
        source_type=EmbeddingSourceType.DOCUMENT,
        source_id=uuid4(),
        content="Sample embedding",
        metadata={},
    )


@pytest.fixture
def vectorstore_repository(
    db_session: Session,
) -> VectorStoreRepository:
    """Create a Vector Store repository."""
    return VectorStoreRepository(db_session)


@pytest.fixture
def vectorstore_service(
    vectorstore_repository: VectorStoreRepository,
) -> VectorStoreService:
    """Create a Vector Store service."""
    return VectorStoreService(vectorstore_repository)


@pytest.fixture
def rag_repository(
    db_session: Session,
) -> RAGRepository:
    """Create a RAG repository."""
    return RAGRepository(db_session)


@pytest.fixture
def rag_service(
    rag_repository: RAGRepository,
) -> RAGService:
    """Create a RAG service."""
    return RAGService(rag_repository)
