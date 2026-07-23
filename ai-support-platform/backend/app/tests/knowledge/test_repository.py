"""Tests for KnowledgeRepository."""

from __future__ import annotations

import uuid
from collections.abc import Callable

import pytest
from sqlalchemy.orm import Session

from app.knowledge.models import KnowledgeArticle
from app.knowledge.repository import KnowledgeRepository
from app.knowledge.types import KnowledgeStatus


@pytest.fixture
def repository(
    db_session: Session,
) -> KnowledgeRepository:
    """Return a knowledge repository."""
    return KnowledgeRepository(db_session)


def test_create_persists_article(
    repository: KnowledgeRepository,
    knowledge_article_factory: Callable[..., KnowledgeArticle],
) -> None:
    """Test creating a knowledge article."""
    article = knowledge_article_factory()

    created = repository.create(article)

    assert created.id is not None
    assert created.title == article.title
    assert repository.get(created.id) is not None


def test_get_by_slug_returns_article(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test retrieving an article by slug."""
    result = repository.get_by_slug(knowledge_article.slug)

    assert result is not None
    assert result.id == knowledge_article.id
    assert result.slug == knowledge_article.slug


def test_get_by_slug_returns_none_for_unknown_slug(
    repository: KnowledgeRepository,
) -> None:
    """Test retrieving an unknown slug."""
    assert repository.get_by_slug("unknown-slug") is None


def test_exists_by_slug_returns_true(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test exists_by_slug returns True."""
    assert repository.exists_by_slug(knowledge_article.slug)


def test_exists_by_slug_returns_false(
    repository: KnowledgeRepository,
) -> None:
    """Test exists_by_slug returns False."""
    assert not repository.exists_by_slug("missing-slug")


def test_get_returns_article(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test retrieving an article by id."""
    result = repository.get(knowledge_article.id)

    assert result is not None
    assert result.id == knowledge_article.id


def test_get_returns_none_for_unknown_id(
    repository: KnowledgeRepository,
) -> None:
    """Test retrieving an unknown article."""
    assert repository.get(uuid.uuid4()) is None


def test_list_returns_articles(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test listing articles."""
    result = repository.list_articles()

    assert knowledge_article in result


def test_search_honors_limit(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test search pagination."""
    result = repository.search(
        knowledge_article.title,
        limit=1,
    )

    assert len(result) == 1


def test_list_by_category_returns_articles(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test listing articles by category."""
    assert knowledge_article.category is not None

    result = repository.list_by_category(
        knowledge_article.category,
    )

    assert knowledge_article in result


def test_list_by_category_returns_empty(
    repository: KnowledgeRepository,
) -> None:
    """Test listing an unknown category."""
    assert repository.list_by_category("unknown-category") == []


def test_list_by_status_returns_articles(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test listing articles by status."""
    result = repository.list_by_status(
        KnowledgeStatus.DRAFT,
    )

    assert knowledge_article in result


def test_count_returns_total(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test counting articles."""
    assert repository.count() >= 1


def test_search_returns_matching_article(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test searching articles."""
    result = repository.search(
        knowledge_article.title,
    )

    assert knowledge_article in result


def test_update_persists_changes(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test updating an article."""
    knowledge_article.title = "Updated Title"

    updated = repository.update(knowledge_article)

    assert updated.title == "Updated Title"

    refreshed = repository.get(knowledge_article.id)

    assert refreshed is not None
    assert refreshed.title == "Updated Title"


def test_delete_marks_article_deleted(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test soft deleting an article."""
    repository.delete(knowledge_article)

    assert knowledge_article.is_deleted is True
    assert repository.get(knowledge_article.id) is None


def test_publish_marks_article_published(
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Test publishing an article."""
    published = repository.publish(
        knowledge_article,
    )

    assert published.status is KnowledgeStatus.PUBLISHED
    assert published.is_published is True


def test_get_by_slug_ignores_deleted_article(
    db_session: Session,
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Deleted articles should not be returned."""
    knowledge_article.is_deleted = True
    db_session.commit()

    assert (
        repository.get_by_slug(
            knowledge_article.slug,
        )
        is None
    )


def test_exists_by_slug_returns_false_for_deleted_article(
    db_session: Session,
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Deleted articles should not exist."""
    knowledge_article.is_deleted = True
    db_session.commit()

    assert not repository.exists_by_slug(
        knowledge_article.slug,
    )


def test_get_returns_none_for_deleted_article(
    db_session: Session,
    repository: KnowledgeRepository,
    knowledge_article: KnowledgeArticle,
) -> None:
    """Deleted articles should not be returned."""
    knowledge_article.is_deleted = True
    db_session.commit()

    assert (
        repository.get(
            knowledge_article.id,
        )
        is None
    )


def test_list_honors_offset(
    repository: KnowledgeRepository,
    knowledge_article_factory: Callable[..., KnowledgeArticle],
) -> None:
    """Test list pagination offset."""
    article1 = knowledge_article_factory(title="First")
    article2 = knowledge_article_factory(title="Second")

    repository.create(article1)
    repository.create(article2)

    all_articles = repository.list_articles()
    paged_articles = repository.list_articles(
        offset=1,
        limit=10,
    )

    assert paged_articles == all_articles[1:]
