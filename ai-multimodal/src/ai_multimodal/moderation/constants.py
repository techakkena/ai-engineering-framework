"""
Constants for the ai_multimodal.moderation module.

This module defines framework-independent constants used by moderation
operations throughout the AI Engineering Framework.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Moderation tasks
# ---------------------------------------------------------------------------

TASK_TEXT: Final[str] = "text"
TASK_IMAGE: Final[str] = "image"
TASK_AUDIO: Final[str] = "audio"
TASK_VIDEO: Final[str] = "video"
TASK_DOCUMENT: Final[str] = "document"
TASK_METADATA: Final[str] = "metadata"

SUPPORTED_TASKS: Final[tuple[str, ...]] = (
    TASK_TEXT,
    TASK_IMAGE,
    TASK_AUDIO,
    TASK_VIDEO,
    TASK_DOCUMENT,
    TASK_METADATA,
)

# ---------------------------------------------------------------------------
# Moderation results
# ---------------------------------------------------------------------------

STATUS_SAFE: Final[str] = "safe"
STATUS_REVIEW: Final[str] = "review"
STATUS_BLOCKED: Final[str] = "blocked"

SUPPORTED_STATUSES: Final[tuple[str, ...]] = (
    STATUS_SAFE,
    STATUS_REVIEW,
    STATUS_BLOCKED,
)

# ---------------------------------------------------------------------------
# Risk thresholds
# ---------------------------------------------------------------------------

DEFAULT_RISK_THRESHOLD: Final[float] = 0.50
MIN_RISK_THRESHOLD: Final[float] = 0.00
MAX_RISK_THRESHOLD: Final[float] = 1.00

# ---------------------------------------------------------------------------
# Categories
# ---------------------------------------------------------------------------

CATEGORY_HATE: Final[str] = "hate"
CATEGORY_HARASSMENT: Final[str] = "harassment"
CATEGORY_SELF_HARM: Final[str] = "self_harm"
CATEGORY_SEXUAL: Final[str] = "sexual"
CATEGORY_VIOLENCE: Final[str] = "violence"

SUPPORTED_CATEGORIES: Final[tuple[str, ...]] = (
    CATEGORY_HATE,
    CATEGORY_HARASSMENT,
    CATEGORY_SELF_HARM,
    CATEGORY_SEXUAL,
    CATEGORY_VIOLENCE,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_PROVIDER: Final[str] = "provider"
METADATA_MODEL: Final[str] = "model"
METADATA_POLICY: Final[str] = "policy"
METADATA_RISK_SCORE: Final[str] = "risk_score"
METADATA_LATENCY: Final[str] = "latency_ms"