"""Operations for the ai_testing.utilities module."""

from __future__ import annotations

from typing import ClassVar

from dataclasses import dataclass, field

from ai_testing.utilities.constants import (
    DEFAULT_CATEGORY,
    MAX_NAME_LENGTH,
    MIN_NAME_LENGTH,
)
from ai_testing.utilities.exceptions import UtilityValidationError


@dataclass(slots=True, frozen=True)
class TestMetadata:
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
                "Test name length is outside the allowed range."
            )

        object.__setattr__(self, "name", normalized)


# Prevent pytest from collecting this dataclass as a test class.
#TestMetadata.__test__ = False


def normalize_test_name(name: str) -> str:
    """Normalize a test name."""
    normalized = "_".join(name.strip().split()).lower()

    if not (
        MIN_NAME_LENGTH
        <= len(normalized)
        <= MAX_NAME_LENGTH
    ):
        raise UtilityValidationError(
            "Normalized test name is outside the allowed range."
        )

    return normalized


def build_test_metadata(
    *,
    name: str,
    category: str = DEFAULT_CATEGORY,
    tags: tuple[str, ...] = (),
) -> TestMetadata:
    """Build validated test metadata."""
    return TestMetadata(
        name=name,
        category=category,
        tags=tags,
    )


__all__ = [
    "TestMetadata",
    "build_test_metadata",
    "normalize_test_name",
]