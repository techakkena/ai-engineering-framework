"""Operations for the ai_docs.openapi module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_docs.openapi.constants import (
    DEFAULT_ENABLED,
    DEFAULT_OPENAPI_VERSION,
    MAX_OPENAPI_NAME_LENGTH,
    MIN_OPENAPI_NAME_LENGTH,
    SUPPORTED_OPENAPI_VERSIONS,
)
from ai_docs.openapi.exceptions import (
    DuplicateOpenAPIError,
    OpenAPINotFoundError,
    OpenAPIValidationError,
    UnsupportedOpenAPIVersionError,
)


@dataclass(slots=True, frozen=True)
class OpenAPIDocument:
    """Represents an OpenAPI document."""

    name: str
    title: str
    version: str = DEFAULT_OPENAPI_VERSION
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the OpenAPI document."""
        normalized_name = self.name.strip()
        normalized_title = self.title.strip()

        if not (
            MIN_OPENAPI_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_OPENAPI_NAME_LENGTH
        ):
            raise OpenAPIValidationError(
                "OpenAPI name length is outside the allowed range."
            )

        if not normalized_title:
            raise OpenAPIValidationError(
                "OpenAPI title cannot be empty."
            )

        if self.version not in SUPPORTED_OPENAPI_VERSIONS:
            raise UnsupportedOpenAPIVersionError(
                f"Unsupported OpenAPI version: {self.version!r}."
            )

        object.__setattr__(self, "name", normalized_name)
        object.__setattr__(self, "title", normalized_title)


class OpenAPIRegistry:
    """Registry for OpenAPI documents."""

    __slots__ = ("_documents",)

    def __init__(self) -> None:
        self._documents: dict[str, OpenAPIDocument] = {}

    def register(
        self,
        document: OpenAPIDocument,
    ) -> None:
        if document.name in self._documents:
            raise DuplicateOpenAPIError(
                f"OpenAPI document {document.name!r} is already registered."
            )

        self._documents[document.name] = document

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._documents:
            raise OpenAPINotFoundError(
                f"OpenAPI document {name!r} is not registered."
            )

        del self._documents[name]

    def get(
        self,
        name: str,
    ) -> OpenAPIDocument:
        try:
            return self._documents[name]
        except KeyError as exc:
            raise OpenAPINotFoundError(
                f"OpenAPI document {name!r} is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._documents

    def clear(self) -> None:
        self._documents.clear()

    def list(self) -> tuple[OpenAPIDocument, ...]:
        return tuple(self._documents.values())

    def __len__(self) -> int:
        return len(self._documents)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return (
            isinstance(name, str)
            and name in self._documents
        )


def build_openapi(
    *,
    name: str,
    title: str,
    version: str = DEFAULT_OPENAPI_VERSION,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> OpenAPIDocument:
    """Build a validated OpenAPI document."""

    return OpenAPIDocument(
        name=name,
        title=title,
        version=version,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "OpenAPIDocument",
    "OpenAPIRegistry",
    "build_openapi",
]