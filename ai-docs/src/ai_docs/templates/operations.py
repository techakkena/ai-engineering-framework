"""Operations for the ai_docs.templates module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_docs.templates.constants import (
    DEFAULT_ENABLED,
    DEFAULT_TEMPLATE_TYPE,
    MAX_TEMPLATE_NAME_LENGTH,
    MIN_TEMPLATE_NAME_LENGTH,
    SUPPORTED_TEMPLATE_TYPES,
)
from ai_docs.templates.exceptions import (
    DuplicateTemplateError,
    TemplateNotFoundError,
    TemplateValidationError,
    UnsupportedTemplateTypeError,
)


@dataclass(slots=True, frozen=True)
class TemplateDefinition:
    """Represents a reusable template."""

    name: str
    content: str
    template_type: str = DEFAULT_TEMPLATE_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the template."""
        normalized_name = self.name.strip()

        if not (
            MIN_TEMPLATE_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_TEMPLATE_NAME_LENGTH
        ):
            raise TemplateValidationError(
                "Template name length is outside the allowed range."
            )

        if not self.content.strip():
            raise TemplateValidationError(
                "Template content cannot be empty."
            )

        if (
            self.template_type
            not in SUPPORTED_TEMPLATE_TYPES
        ):
            raise UnsupportedTemplateTypeError(
                f"Unsupported template type: "
                f"{self.template_type!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized_name,
        )


class TemplateRegistry:
    """Registry for templates."""

    __slots__ = ("_templates",)

    def __init__(self) -> None:
        self._templates: dict[
            str,
            TemplateDefinition,
        ] = {}

    def register(
        self,
        template: TemplateDefinition,
    ) -> None:
        if template.name in self._templates:
            raise DuplicateTemplateError(
                f"Template {template.name!r} is already registered."
            )

        self._templates[
            template.name
        ] = template

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._templates:
            raise TemplateNotFoundError(
                f"Template {name!r} is not registered."
            )

        del self._templates[name]

    def get(
        self,
        name: str,
    ) -> TemplateDefinition:
        try:
            return self._templates[name]
        except KeyError as exc:
            raise TemplateNotFoundError(
                f"Template {name!r} is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._templates

    def clear(self) -> None:
        self._templates.clear()

    def list(
        self,
    ) -> tuple[
        TemplateDefinition,
        ...,
    ]:
        return tuple(
            self._templates.values()
        )

    def __len__(self) -> int:
        return len(self._templates)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return (
            isinstance(name, str)
            and name in self._templates
        )


def build_template(
    *,
    name: str,
    content: str,
    template_type: str = DEFAULT_TEMPLATE_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> TemplateDefinition:
    """Build a validated template."""

    return TemplateDefinition(
        name=name,
        content=content,
        template_type=template_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "TemplateDefinition",
    "TemplateRegistry",
    "build_template",
]