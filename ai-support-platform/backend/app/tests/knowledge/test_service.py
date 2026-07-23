"""Tests for KnowledgeService."""

from __future__ import annotations

from uuid import UUID

import pytest
from sqlalchemy.orm import Session

from app.knowledge.exceptions import (
    KnowledgeAlreadyExistsError,
    KnowledgeNotFoundError,
)
from app.knowledge.models import KnowledgeArticle
from app.knowledge.repository import KnowledgeRepository
from app.knowledge.schemas import (
    KnowledgeCreate,
    KnowledgeSearchParams,
    KnowledgeUpdate,
)
from app.knowledge.service import KnowledgeService
from app.knowledge.types import KnowledgeStatus
from app.models.organization import Organization
from app.models.user import User


@pytest.fixture
def service(
    db_session: Session,
) -> KnowledgeService:
    """Return a knowledge service."""
    repository = KnowledgeRepository(db_session)
    return KnowledgeService(repository)


def test_get_returns_article(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test retrieving a knowledge article."""
    result = service.get(knowledge_article.id)

    assert result.id == knowledge_article.id
    assert result.title == knowledge_article.title


def test_get_raises_not_found(
    service: KnowledgeService,
) -> None:
    """Test retrieving an unknown article."""
    with pytest.raises(KnowledgeNotFoundError):
        service.get(
            UUID("00000000-0000-0000-0000-000000000000"),
        )


def test_create_article(
    service: KnowledgeService,
    organization: Organization,
    user: User,
) -> None:
    """Test creating a knowledge article."""
    request = KnowledgeCreate(
        title="Knowledge Service Test",
        summary="Summary",
        content="Knowledge content",
        category="General",
        tags=[
            "python",
            "fastapi",
        ],
    )

    article = service.create(
        organization_id=organization.id,
        author_id=user.id,
        request=request,
    )

    assert article.title == request.title
    assert article.slug == "knowledge-service-test"
    assert article.version == 1
    assert article.status == KnowledgeStatus.DRAFT
    assert article.is_published is False
    assert article.tags == "python,fastapi"


def test_create_duplicate_slug_raises(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test duplicate slug validation."""
    request = KnowledgeCreate(
        title=knowledge_article.title,
        summary="Duplicate summary",
        content="Duplicate content",
        category="General",
        tags=["duplicate"],
    )

    with pytest.raises(KnowledgeAlreadyExistsError):
        service.create(
            organization_id=knowledge_article.organization_id,
            author_id=knowledge_article.author_id,
            request=request,
        )


def test_update_article(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test updating a knowledge article."""
    request = KnowledgeUpdate(
        title="Updated Title",
        summary="Updated Summary",
    )

    article = service.update(
        knowledge_article.id,
        request,
    )

    assert article.title == "Updated Title"
    assert article.summary == "Updated Summary"


def test_update_increments_version(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test updating increments version."""
    version = knowledge_article.version

    request = KnowledgeUpdate(
        title="New Version",
    )

    article = service.update(
        knowledge_article.id,
        request,
    )

    assert article.version == version + 1


def test_update_tags(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test updating article tags."""
    request = KnowledgeUpdate(
        tags=[
            "python",
            "fastapi",
        ],
    )

    article = service.update(
        knowledge_article.id,
        request,
    )

    assert article.tags == "python,fastapi"


def test_publish_article(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test publishing an article."""
    article = service.publish(
        knowledge_article.id,
    )

    assert article.is_published is True
    assert article.status == KnowledgeStatus.PUBLISHED
    assert article.published_at is not None


def test_archive_article(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test archiving an article."""
    article = service.archive(
        knowledge_article.id,
    )

    assert article.status == KnowledgeStatus.ARCHIVED


def test_delete_article(
    db_session: Session,
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test deleting an article."""
    service.delete(
        knowledge_article.id,
    )

    db_session.refresh(knowledge_article)

    assert knowledge_article.is_deleted is True


def test_search_returns_articles(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test searching articles."""
    result = service.search(
        KnowledgeSearchParams(
            query=knowledge_article.title,
        ),
    )

    assert knowledge_article in result


def test_search_by_category(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test filtering by category."""
    result = service.search(
        KnowledgeSearchParams(
            category=knowledge_article.category,
        ),
    )

    assert knowledge_article in result


def test_search_by_status(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test filtering by status."""
    result = service.search(
        KnowledgeSearchParams(
            status=KnowledgeStatus.DRAFT,
        ),
    )

    assert knowledge_article in result


def test_search_without_filters_returns_articles(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test searching without filters."""
    result = service.search(
        KnowledgeSearchParams(),
    )

    assert knowledge_article in result


def test_list_returns_articles(
    service: KnowledgeService,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test listing articles."""
    total, articles = service.list_articles()

    assert total >= 1
    assert knowledge_article in articles
