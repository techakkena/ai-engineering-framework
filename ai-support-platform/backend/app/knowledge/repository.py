"""Repository layer for knowledge articles."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.knowledge.models import KnowledgeArticle
from app.knowledge.types import KnowledgeStatus


class KnowledgeRepository:
    """Repository for knowledge articles."""

    def __init__(self, session: Session) -> None:
        """Initialize repository."""
        self._session = session

    def create(
        self,
        article: KnowledgeArticle,
    ) -> KnowledgeArticle:
        """Create a knowledge article."""
        self._session.add(article)
        self._session.commit()
        self._session.refresh(article)
        return article

    def get(
        self,
        article_id: UUID,
    ) -> KnowledgeArticle | None:
        """Return a knowledge article by ID."""
        statement = select(KnowledgeArticle).where(
            KnowledgeArticle.id == article_id,
            KnowledgeArticle.is_deleted.is_(False),
        )
        return self._session.execute(statement).scalar_one_or_none()

    def get_by_slug(
        self,
        slug: str,
    ) -> KnowledgeArticle | None:
        """Return a knowledge article by slug."""
        statement = select(KnowledgeArticle).where(
            KnowledgeArticle.slug == slug,
            KnowledgeArticle.is_deleted.is_(False),
        )
        return self._session.execute(statement).scalar_one_or_none()

    def exists_by_slug(
        self,
        slug: str,
    ) -> bool:
        """Return whether a slug already exists."""
        statement = (
            select(func.count())
            .select_from(KnowledgeArticle)
            .where(
                KnowledgeArticle.slug == slug,
                KnowledgeArticle.is_deleted.is_(False),
            )
        )
        return int(self._session.execute(statement).scalar_one()) > 0

    def list_articles(
        self,
        offset: int = 0,
        limit: int = 100,
    ) -> list[KnowledgeArticle]:
        """Return knowledge articles."""
        statement = (
            select(KnowledgeArticle)
            .where(KnowledgeArticle.is_deleted.is_(False))
            .order_by(
                KnowledgeArticle.created_at.desc(),
                KnowledgeArticle.id.desc(),
            )
            .offset(offset)
            .limit(limit)
        )

        return list(
            self._session.execute(statement).scalars().all(),
        )

    def search(
        self,
        query: str,
        offset: int = 0,
        limit: int = 100,
    ) -> list[KnowledgeArticle]:
        """Search knowledge articles."""
        pattern = f"%{query}%"

        statement = (
            select(KnowledgeArticle)
            .where(
                KnowledgeArticle.is_deleted.is_(False),
                or_(
                    KnowledgeArticle.title.ilike(pattern),
                    KnowledgeArticle.summary.ilike(pattern),
                    KnowledgeArticle.content.ilike(pattern),
                    KnowledgeArticle.tags.ilike(pattern),
                ),
            )
            .order_by(KnowledgeArticle.created_at.desc())
            .offset(offset)
            .limit(limit)
        )

        return cast(
            list[KnowledgeArticle],
            self._session.execute(statement).scalars().all(),
        )

    def list_by_category(
        self,
        category: str | None,
    ) -> list[KnowledgeArticle]:
        """Return articles by category."""
        statement = (
            select(KnowledgeArticle)
            .where(
                KnowledgeArticle.category == category,
                KnowledgeArticle.is_deleted.is_(False),
            )
            .order_by(KnowledgeArticle.created_at.desc())
        )

        return cast(
            list[KnowledgeArticle],
            self._session.execute(statement).scalars().all(),
        )

    def list_by_status(
        self,
        status: KnowledgeStatus,
    ) -> list[KnowledgeArticle]:
        """Return articles by status."""
        statement = (
            select(KnowledgeArticle)
            .where(
                KnowledgeArticle.status == status,
                KnowledgeArticle.is_deleted.is_(False),
            )
            .order_by(KnowledgeArticle.created_at.desc())
        )

        return cast(
            list[KnowledgeArticle],
            self._session.execute(statement).scalars().all(),
        )

    def update(
        self,
        article: KnowledgeArticle,
    ) -> KnowledgeArticle:
        """Update a knowledge article."""
        self._session.commit()
        self._session.refresh(article)
        return article

    def delete(
        self,
        article: KnowledgeArticle,
    ) -> None:
        """Soft delete a knowledge article."""
        article.is_deleted = True
        self._session.commit()
        self._session.refresh(article)

    def publish(
        self,
        article: KnowledgeArticle,
    ) -> KnowledgeArticle:
        """Publish a knowledge article."""
        article.status = KnowledgeStatus.PUBLISHED
        article.is_published = True

        self._session.commit()
        self._session.refresh(article)

        return article

    def count(self) -> int:
        """Return the number of active knowledge articles."""
        statement = (
            select(func.count())
            .select_from(KnowledgeArticle)
            .where(KnowledgeArticle.is_deleted.is_(False))
        )

        return int(self._session.scalar(statement) or 0)
