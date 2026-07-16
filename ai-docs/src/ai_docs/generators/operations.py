"""Operations for the ai_docs.generators module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_docs.generators.constants import (
    DEFAULT_ENABLED,
    DEFAULT_GENERATOR_TYPE,
    MAX_GENERATOR_NAME_LENGTH,
    MIN_GENERATOR_NAME_LENGTH,
    SUPPORTED_GENERATOR_TYPES,
)
from ai_docs.generators.exceptions import (
    DuplicateGeneratorError,
    GeneratorNotFoundError,
    GeneratorValidationError,
    UnsupportedGeneratorTypeError,
)


@dataclass(slots=True, frozen=True)
class DocumentationGenerator:
    """Represents a documentation generator."""

    name: str
    generator_type: str = DEFAULT_GENERATOR_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the generator."""
        normalized_name = self.name.strip()

        if not (
            MIN_GENERATOR_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_GENERATOR_NAME_LENGTH
        ):
            raise GeneratorValidationError(
                "Generator name length is outside the allowed range."
            )

        if (
            self.generator_type
            not in SUPPORTED_GENERATOR_TYPES
        ):
            raise UnsupportedGeneratorTypeError(
                f"Unsupported generator type: "
                f"{self.generator_type!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized_name,
        )


class GeneratorRegistry:
    """Registry for documentation generators."""

    __slots__ = ("_generators",)

    def __init__(self) -> None:
        self._generators: dict[
            str,
            DocumentationGenerator,
        ] = {}

    def register(
        self,
        generator: DocumentationGenerator,
    ) -> None:
        if generator.name in self._generators:
            raise DuplicateGeneratorError(
                f"Generator {generator.name!r} "
                "is already registered."
            )

        self._generators[
            generator.name
        ] = generator

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._generators:
            raise GeneratorNotFoundError(
                f"Generator {name!r} "
                "is not registered."
            )

        del self._generators[name]

    def get(
        self,
        name: str,
    ) -> DocumentationGenerator:
        try:
            return self._generators[name]
        except KeyError as exc:
            raise GeneratorNotFoundError(
                f"Generator {name!r} "
                "is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._generators

    def clear(self) -> None:
        self._generators.clear()

    def list(
        self,
    ) -> tuple[
        DocumentationGenerator,
        ...,
    ]:
        return tuple(
            self._generators.values()
        )

    def __len__(self) -> int:
        return len(self._generators)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return (
            isinstance(name, str)
            and name in self._generators
        )


def build_generator(
    *,
    name: str,
    generator_type: str = DEFAULT_GENERATOR_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> DocumentationGenerator:
    """Build a validated documentation generator."""

    return DocumentationGenerator(
        name=name,
        generator_type=generator_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "DocumentationGenerator",
    "GeneratorRegistry",
    "build_generator",
]