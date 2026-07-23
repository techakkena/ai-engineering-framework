"""Business logic for knowledge management."""

from __future__ import annotations

from datetime import UTC, datetime
from uuid import UUID

from slugify import slugify

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
from app.knowledge.types import KnowledgeStatus


class KnowledgeService:
    """Service for managing knowledge articles."""

    def __init__(
        self,
        repository: KnowledgeRepository,
    ) -> None:
        """Initialize the service."""
        self._repository = repository

    def create(
        self,
        organization_id: UUID,
        author_id: UUID,
        request: KnowledgeCreate,
    ) -> KnowledgeArticle:
        """Create a knowledge article."""
        slug = slugify(request.title)

        if self._repository.get_by_slug(slug) is not None:
            raise KnowledgeAlreadyExistsError()

        article = KnowledgeArticle(
            organization_id=organization_id,
            author_id=author_id,
            title=request.title,
            slug=slug,
            summary=request.summary,
            content=request.content,
            category=request.category,
            tags=",".join(request.tags) if request.tags else None,
            version=1,
            status=KnowledgeStatus.DRAFT,
            is_published=False,
        )

        return self._repository.create(article)

    def get(
        self,
        article_id: UUID,
    ) -> KnowledgeArticle:
        """Return a knowledge article."""
        article = self._repository.get(article_id)

        if article is None:
            raise KnowledgeNotFoundError()

        return article

    def list_articles(
        self,
        offset: int = 0,
        limit: int = 100,
    ) -> tuple[int, list[KnowledgeArticle]]:
        """Return knowledge articles."""
        total = self._repository.count()
        articles = self._repository.list_articles(
            offset=offset,
            limit=limit,
        )

        return total, articles

    def search(
        self,
        request: KnowledgeSearchParams,
    ) -> list[KnowledgeArticle]:
        """Search knowledge articles."""
        if request.query:
            return self._repository.search(
                query=request.query,
                offset=request.offset,
                limit=request.limit,
            )

        if request.category is not None:
            return self._repository.list_by_category(
                request.category,
            )

        if request.status is not None:
            return self._repository.list_by_status(
                request.status,
            )

        return self._repository.list_articles(
            offset=request.offset,
            limit=request.limit,
        )

    def update(
        self,
        article_id: UUID,
        request: KnowledgeUpdate,
    ) -> KnowledgeArticle:
        """Update a knowledge article."""
        article = self.get(article_id)

        updated = False

        for field, value in request.model_dump(
            exclude_unset=True,
        ).items():
            if field == "tags" and value is not None:
                value = ",".join(value)

            setattr(article, field, value)
            updated = True

        if updated:
            article.version += 1

        return self._repository.update(article)

    def publish(
        self,
        article_id: UUID,
    ) -> KnowledgeArticle:
        """Publish a knowledge article."""
        article = self.get(article_id)

        article.status = KnowledgeStatus.PUBLISHED
        article.is_published = True
        article.published_at = datetime.now(UTC)

        return self._repository.update(article)

    def archive(
        self,
        article_id: UUID,
    ) -> KnowledgeArticle:
        """Archive a knowledge article."""
        article = self.get(article_id)

        article.status = KnowledgeStatus.ARCHIVED
        article.is_published = False

        return self._repository.update(article)

    def delete(
        self,
        article_id: UUID,
    ) -> None:
        """Soft delete a knowledge article."""
        article = self.get(article_id)
        self._repository.delete(article)
