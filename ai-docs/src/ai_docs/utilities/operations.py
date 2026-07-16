"""Operations for the ai_docs.utilities module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_docs.utilities.constants import (
    DEFAULT_AUTHOR,
    DEFAULT_VERSION,
    MAX_NAME_LENGTH,
    MIN_NAME_LENGTH,
)
from ai_docs.utilities.exceptions import (
    UtilityValidationError,
)


@dataclass(
    slots=True,
    frozen=True,
)
class DocumentationMetadata:
    """Metadata describing documentation."""

    name: str
    version: str = DEFAULT_VERSION
    author: str = DEFAULT_AUTHOR
    description: str = ""

    def __post_init__(self) -> None:
        """Validate metadata."""
        normalized = normalize_name(
            self.name,
        )

        object.__setattr__(
            self,
            "name",
            normalized,
        )


def normalize_name(
    name: str,
) -> str:
    """Normalize a documentation name."""

    normalized = name.strip()

    if not (
        MIN_NAME_LENGTH
        <= len(normalized)
        <= MAX_NAME_LENGTH
    ):
        raise UtilityValidationError(
            "Invalid documentation name."
        )

    return normalized


def build_metadata(
    *,
    name: str,
    version: str = DEFAULT_VERSION,
    author: str = DEFAULT_AUTHOR,
    description: str = "",
) -> DocumentationMetadata:
    """Build validated documentation metadata."""

    return DocumentationMetadata(
        name=name,
        version=version,
        author=author,
        description=description,
    )


__all__ = [
    "DocumentationMetadata",
    "build_metadata",
    "normalize_name",
]