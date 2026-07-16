"""Operations for the ai_docs.markdown module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_docs.markdown.constants import (
    DEFAULT_ENABLED,
    DEFAULT_MARKDOWN_FORMAT,
    MAX_MARKDOWN_NAME_LENGTH,
    MIN_MARKDOWN_NAME_LENGTH,
    SUPPORTED_MARKDOWN_FORMATS,
)
from ai_docs.markdown.exceptions import (
    DuplicateMarkdownError,
    MarkdownNotFoundError,
    MarkdownValidationError,
    UnsupportedMarkdownFormatError,
)


@dataclass(slots=True, frozen=True)
class MarkdownDocument:
    """Represents a markdown document."""

    name: str
    content: str
    markdown_format: str = DEFAULT_MARKDOWN_FORMAT
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the markdown document."""
        normalized_name = self.name.strip()

        if not (
            MIN_MARKDOWN_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_MARKDOWN_NAME_LENGTH
        ):
            raise MarkdownValidationError(
                "Markdown name length is outside the allowed range."
            )

        if not self.content.strip():
            raise MarkdownValidationError(
                "Markdown content cannot be empty."
            )

        if (
            self.markdown_format
            not in SUPPORTED_MARKDOWN_FORMATS
        ):
            raise UnsupportedMarkdownFormatError(
                f"Unsupported markdown format: "
                f"{self.markdown_format!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized_name,
        )


class MarkdownRegistry:
    """Registry for markdown documents."""

    __slots__ = ("_documents",)

    def __init__(self) -> None:
        self._documents: dict[
            str,
            MarkdownDocument,
        ] = {}

    def register(
        self,
        document: MarkdownDocument,
    ) -> None:
        if document.name in self._documents:
            raise DuplicateMarkdownError(
                f"Markdown {document.name!r} "
                "is already registered."
            )

        self._documents[
            document.name
        ] = document

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._documents:
            raise MarkdownNotFoundError(
                f"Markdown {name!r} "
                "is not registered."
            )

        del self._documents[name]

    def get(
        self,
        name: str,
    ) -> MarkdownDocument:
        try:
            return self._documents[name]
        except KeyError as exc:
            raise MarkdownNotFoundError(
                f"Markdown {name!r} "
                "is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._documents

    def clear(self) -> None:
        self._documents.clear()

    def list(
        self,
    ) -> tuple[
        MarkdownDocument,
        ...,
    ]:
        return tuple(
            self._documents.values()
        )

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


def build_markdown(
    *,
    name: str,
    content: str,
    markdown_format: str = DEFAULT_MARKDOWN_FORMAT,
    enabled: bool = DEFAULT_ENABLED,
) -> MarkdownDocument:
    """Build a validated markdown document."""

    return MarkdownDocument(
        name=name,
        content=content,
        markdown_format=markdown_format,
        enabled=enabled,
    )


__all__ = [
    "MarkdownDocument",
    "MarkdownRegistry",
    "build_markdown",
]