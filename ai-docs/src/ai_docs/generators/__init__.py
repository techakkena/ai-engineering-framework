"""Documentation generator support for ai-docs."""

from __future__ import annotations

from ai_docs.generators.operations import (
    DocumentationGenerator,
    GeneratorRegistry,
    build_generator,
)

__all__ = [
    "DocumentationGenerator",
    "GeneratorRegistry",
    "build_generator",
]