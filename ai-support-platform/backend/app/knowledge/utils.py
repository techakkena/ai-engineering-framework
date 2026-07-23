"""Utility functions for the knowledge module."""

from __future__ import annotations

import re
from typing import Any

from slugify import slugify

from app.knowledge.constants import SLUG_SEPARATOR, TAG_SEPARATOR


def generate_slug(title: str) -> str:
    """Generate a URL-friendly slug from a title.

    Args:
        title: Article title.

    Returns:
        URL-friendly slug.
    """
    return slugify(
        title,
        separator=SLUG_SEPARATOR,
    )


def normalize_tags(tags: list[str]) -> str:
    """Normalize tags for database storage.

    Args:
        tags: List of tags.

    Returns:
        Comma-separated normalized tags.
    """
    normalized = {tag.strip().lower() for tag in tags if tag.strip()}

    return TAG_SEPARATOR.join(sorted(normalized))


def parse_tags(tags: str | None) -> list[str]:
    """Convert stored tags into a list.

    Args:
        tags: Comma-separated tags.

    Returns:
        List of tags.
    """
    if not tags:
        return []

    return [tag.strip() for tag in tags.split(TAG_SEPARATOR) if tag.strip()]


def sanitize_search_query(query: str) -> str:
    """Sanitize a search query.

    Args:
        query: User search query.

    Returns:
        Sanitized query.
    """
    query = query.strip()
    query = re.sub(r"\s+", " ", query)

    return query


def estimate_reading_time(content: str) -> int:
    """Estimate reading time in minutes.

    Uses an average reading speed of 200 words per minute.

    Args:
        content: Article content.

    Returns:
        Estimated reading time.
    """
    words = len(content.split())

    return max(1, (words + 199) // 200)


def build_search_vector(article: dict[str, Any]) -> str:
    """Build searchable text from article fields.

    Args:
        article: Article data.

    Returns:
        Combined searchable string.
    """
    fields = (
        article.get("title", ""),
        article.get("summary", ""),
        article.get("content", ""),
        article.get("category", ""),
        article.get("tags", ""),
    )

    return " ".join(value for value in fields if value)


def extract_headings(content: str) -> list[str]:
    """Extract Markdown headings.

    Args:
        content: Markdown content.

    Returns:
        Heading list.
    """
    headings: list[str] = []

    for line in content.splitlines():
        line = line.strip()

        if line.startswith("#"):
            headings.append(
                line.lstrip("#").strip(),
            )

    return headings


def build_article_summary(
    content: str,
    max_length: int = 250,
) -> str:
    """Generate a short summary.

    Args:
        content: Article content.
        max_length: Maximum summary length.

    Returns:
        Summary text.
    """
    text = re.sub(r"\s+", " ", content).strip()

    if len(text) <= max_length:
        return text

    return text[:max_length].rstrip() + "..."
