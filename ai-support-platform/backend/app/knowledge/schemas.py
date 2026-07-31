"""Pydantic schemas for the knowledge module."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    model_validator,
)

from app.knowledge.types import KnowledgeStatus


class KnowledgeBase(BaseModel):
    """Base knowledge schema."""

    title: str = Field(
        min_length=3,
        max_length=255,
    )
    summary: str | None = Field(
        default=None,
        max_length=1000,
    )
    content: str = Field(
        min_length=1,
    )
    category: str | None = Field(
        default=None,
        max_length=100,
    )
    tags: list[str] = Field(
        default_factory=list,
    )


class KnowledgeCreate(KnowledgeBase):
    """Create knowledge article."""


class KnowledgeUpdate(BaseModel):
    """Update knowledge article."""

    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=255,
    )
    summary: str | None = Field(
        default=None,
        max_length=1000,
    )
    content: str | None = None
    category: str | None = Field(
        default=None,
        max_length=100,
    )
    tags: list[str] | None = None
    status: KnowledgeStatus | None = None


class KnowledgePublishRequest(BaseModel):
    """Publish knowledge article."""

    publish: bool = True


class KnowledgeResponse(KnowledgeBase):
    """Knowledge response."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    organization_id: UUID
    author_id: UUID

    slug: str
    status: KnowledgeStatus
    version: int

    is_published: bool
    is_deleted: bool

    published_at: datetime | None

    created_at: datetime
    updated_at: datetime

    @model_validator(mode="before")
    @classmethod
    def convert_tags(
        cls,
        value: object,
    ) -> object:
        """Convert database tag string into a list."""
        if not hasattr(value, "tags"):
            return value

        tags = value.tags

        if isinstance(tags, str):
            value.tags = (
                [tag.strip() for tag in tags.split(",") if tag.strip()] if tags else []
            )
        elif tags is None:
            value.tags = []

        return value


class KnowledgeListResponse(BaseModel):
    """Knowledge list response."""

    items: list[KnowledgeResponse]
    total: int


class KnowledgeSearchParams(BaseModel):
    """Knowledge search parameters."""

    query: str | None = None
    category: str | None = None
    tag: str | None = None
    status: KnowledgeStatus | None = None

    offset: int = 0
    limit: int = Field(
        default=100,
        ge=1,
        le=100,
    )
