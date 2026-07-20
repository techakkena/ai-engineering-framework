from __future__ import annotations

"""Operations for RAG pipelines."""

from .constants import (
    DEFAULT_MAX_STEPS,
    DEFAULT_PIPELINE,
    MAX_STEPS,
    MIN_STEPS,
    SUPPORTED_PIPELINES,
)


def default_pipeline() -> str:
    """Return the default pipeline."""

    return DEFAULT_PIPELINE


def supported_pipeline(name: str) -> bool:
    """Return True if the pipeline is supported."""

    return name.lower() in SUPPORTED_PIPELINES


def validate_pipeline_steps(steps: int) -> bool:
    """Validate the number of pipeline steps."""

    return MIN_STEPS <= steps <= MAX_STEPS


def default_max_steps() -> int:
    """Return the default maximum pipeline steps."""

    return DEFAULT_MAX_STEPS
