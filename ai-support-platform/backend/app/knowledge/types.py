"""Shared types for the knowledge module."""

from __future__ import annotations

from enum import StrEnum


class KnowledgeStatus(StrEnum):
    """Knowledge article lifecycle."""

    DRAFT = "draft"
    REVIEW = "review"
    PUBLISHED = "published"
    ARCHIVED = "archived"
