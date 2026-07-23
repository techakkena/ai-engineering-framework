"""Constants used by the knowledge module."""

from __future__ import annotations

from app.knowledge.types import KnowledgeStatus

#
# Database
#

KNOWLEDGE_TABLE_NAME = "knowledge_articles"

#
# Field Lengths
#

MAX_TITLE_LENGTH = 255
MIN_TITLE_LENGTH = 3

MAX_SUMMARY_LENGTH = 1000

MAX_CATEGORY_LENGTH = 100

MAX_SLUG_LENGTH = 255

#
# Pagination
#

DEFAULT_PAGE = 1
DEFAULT_OFFSET = 0
DEFAULT_LIMIT = 100
MAX_LIMIT = 100

#
# Versioning
#

INITIAL_VERSION = 1

#
# Publishing
#

DEFAULT_PUBLISHED = False
DEFAULT_DELETED = False

#
# Search
#

MIN_SEARCH_LENGTH = 2

SEARCHABLE_FIELDS = (
    "title",
    "summary",
    "content",
    "tags",
    "category",
)

#
# Sorting
#

DEFAULT_SORT_FIELD = "created_at"
DEFAULT_SORT_ORDER = "desc"

ALLOWED_SORT_FIELDS = (
    "title",
    "category",
    "status",
    "created_at",
    "updated_at",
    "published_at",
)

#
# Status
#

DEFAULT_STATUS = KnowledgeStatus.DRAFT

ACTIVE_STATUSES = (
    KnowledgeStatus.DRAFT,
    KnowledgeStatus.REVIEW,
    KnowledgeStatus.PUBLISHED,
)

TERMINAL_STATUSES = (KnowledgeStatus.ARCHIVED,)

#
# Slug
#

SLUG_SEPARATOR = "-"

#
# Tags
#

TAG_SEPARATOR = ","

#
# Content
#

SUPPORTED_CONTENT_TYPES = (
    "markdown",
    "html",
    "text",
)

#
# Metadata
#

DEFAULT_LANGUAGE = "en"

DEFAULT_ENCODING = "utf-8"
