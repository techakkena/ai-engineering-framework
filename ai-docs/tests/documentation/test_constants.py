"""Operations for the ai_docs.documentation module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_docs.documentation.constants import (
    DEFAULT_DOCUMENTATION_TYPE,
    DEFAULT_ENABLED,
    MAX_DOCUMENTATION_NAME_LENGTH,
    MIN_DOCUMENTATION_NAME_LENGTH,
    SUPPORTED_DOCUMENTATION_TYPES,
)
from ai_docs.documentation.exceptions import (
    DocumentationNotFoundError,
    DocumentationValidationError,
    DuplicateDocumentationError,
    UnsupportedDocumentationTypeError,
)


@dataclass(slots=True, frozen=True)
class DocumentationDefinition:
    """Represents a documentation definition."""

    name: str
    documentation_type: str = DEFAULT_DOCUMENTATION_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the documentation definition."""
        normalized_name = self.name.strip()

        if not (
            MIN_DOCUMENTATION_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_DOCUMENTATION_NAME_LENGTH
        ):
            raise DocumentationValidationError(
                "Documentation name length is outside the allowed range."
            )

        if (
            self.documentation_type
            not in SUPPORTED_DOCUMENTATION_TYPES
        ):
            raise UnsupportedDocumentationTypeError(
                f"Unsupported documentation type: "
                f"{self.documentation_type!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized_name,
        )


class DocumentationRegistry:
    """Registry for documentation definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[
            str,
            DocumentationDefinition,
        ] = {}

    def register(
        self,
        definition: DocumentationDefinition,
    ) -> None:
        """Register a documentation definition."""
        if definition.name in self._definitions:
            raise DuplicateDocumentationError(
                f"Documentation {definition.name!r} "
                "is already registered."
            )

        self._definitions[
            definition.name
        ] = definition

    def unregister(
        self,
        name: str,
    ) -> None:
        """Remove a documentation definition."""
        if name not in self._definitions:
            raise DocumentationNotFoundError(
                f"Documentation {name!r} "
                "is not registered."
            )

        del self._definitions[name]

    def get(
        self,
        name: str,
    ) -> DocumentationDefinition:
        """Return a documentation definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise DocumentationNotFoundError(
                f"Documentation {name!r} "
                "is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether a definition exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Clear all definitions."""
        self._definitions.clear()

    def list(
        self,
    ) -> tuple[
        DocumentationDefinition,
        ...,
    ]:
        """Return all registered definitions."""
        return tuple(
            self._definitions.values()
        )

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._definitions)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        """Return membership."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_documentation(
    *,
    name: str,
    documentation_type: str = DEFAULT_DOCUMENTATION_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> DocumentationDefinition:
    """Build a validated documentation definition."""

    return DocumentationDefinition(
        name=name,
        documentation_type=documentation_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "DocumentationDefinition",
    "DocumentationRegistry",
    "build_documentation",
]