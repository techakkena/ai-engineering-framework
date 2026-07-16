"""Operations for the ai_analytics.utilities module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar

from ai_analytics.utilities.constants import (
    DEFAULT_CATEGORY,
    MAX_NAME_LENGTH,
    MIN_NAME_LENGTH,
)
from ai_analytics.utilities.exceptions import (
    UtilityValidationError,
)


@dataclass(slots=True, frozen=True)
class AnalyticsMetadata:
    """Represents analytics metadata."""

    __test__: ClassVar[bool] = False

    name: str
    category: str = DEFAULT_CATEGORY
    tags: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        """Validate metadata."""
        normalized = self.name.strip()

        if not (
            MIN_NAME_LENGTH
            <= len(normalized)
            <= MAX_NAME_LENGTH
        ):
            raise UtilityValidationError(
                "Metadata name length is outside the allowed range."
            )

        object.__setattr__(self, "name", normalized)


def normalize_name(name: str) -> str:
    """Normalize a metadata name."""
    normalized = "_".join(name.strip().split()).lower()

    if not (
        MIN_NAME_LENGTH
        <= len(normalized)
        <= MAX_NAME_LENGTH
    ):
        raise UtilityValidationError(
            "Normalized name is outside the allowed range."
        )

    return normalized


def build_metadata(
    *,
    name: str,
    category: str = DEFAULT_CATEGORY,
    tags: tuple[str, ...] = (),
) -> AnalyticsMetadata:
    """Build validated analytics metadata."""

    return AnalyticsMetadata(
        name=name,
        category=category,
        tags=tags,
    )


__all__ = [
    "AnalyticsMetadata",
    "build_metadata",
    "normalize_name",
]