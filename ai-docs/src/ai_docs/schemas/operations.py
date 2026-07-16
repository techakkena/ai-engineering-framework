"""Operations for the ai_docs.schemas module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_docs.schemas.constants import (
    DEFAULT_ENABLED,
    DEFAULT_SCHEMA_FORMAT,
    MAX_SCHEMA_NAME_LENGTH,
    MIN_SCHEMA_NAME_LENGTH,
    SUPPORTED_SCHEMA_FORMATS,
)
from ai_docs.schemas.exceptions import (
    DuplicateSchemaError,
    SchemaNotFoundError,
    SchemaValidationError,
    UnsupportedSchemaFormatError,
)


@dataclass(slots=True, frozen=True)
class SchemaDefinition:
    """Represents a schema definition."""

    name: str
    content: str
    schema_format: str = DEFAULT_SCHEMA_FORMAT
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the schema definition."""
        normalized_name = self.name.strip()

        if not (
            MIN_SCHEMA_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_SCHEMA_NAME_LENGTH
        ):
            raise SchemaValidationError(
                "Schema name length is outside the allowed range."
            )

        if not self.content.strip():
            raise SchemaValidationError(
                "Schema content cannot be empty."
            )

        if self.schema_format not in SUPPORTED_SCHEMA_FORMATS:
            raise UnsupportedSchemaFormatError(
                f"Unsupported schema format: "
                f"{self.schema_format!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized_name,
        )


class SchemaRegistry:
    """Registry for schema definitions."""

    __slots__ = ("_schemas",)

    def __init__(self) -> None:
        self._schemas: dict[
            str,
            SchemaDefinition,
        ] = {}

    def register(
        self,
        schema: SchemaDefinition,
    ) -> None:
        if schema.name in self._schemas:
            raise DuplicateSchemaError(
                f"Schema {schema.name!r} is already registered."
            )

        self._schemas[schema.name] = schema

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._schemas:
            raise SchemaNotFoundError(
                f"Schema {name!r} is not registered."
            )

        del self._schemas[name]

    def get(
        self,
        name: str,
    ) -> SchemaDefinition:
        try:
            return self._schemas[name]
        except KeyError as exc:
            raise SchemaNotFoundError(
                f"Schema {name!r} is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._schemas

    def clear(self) -> None:
        self._schemas.clear()

    def list(
        self,
    ) -> tuple[
        SchemaDefinition,
        ...,
    ]:
        return tuple(
            self._schemas.values()
        )

    def __len__(self) -> int:
        return len(self._schemas)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return (
            isinstance(name, str)
            and name in self._schemas
        )


def build_schema(
    *,
    name: str,
    content: str,
    schema_format: str = DEFAULT_SCHEMA_FORMAT,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> SchemaDefinition:
    """Build a validated schema definition."""

    return SchemaDefinition(
        name=name,
        content=content,
        schema_format=schema_format,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "SchemaDefinition",
    "SchemaRegistry",
    "build_schema",
]