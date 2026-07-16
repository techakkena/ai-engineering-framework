"""OpenAPI document support for ai-docs."""

from __future__ import annotations

from ai_docs.openapi.operations import (
    OpenAPIDocument,
    OpenAPIRegistry,
    build_openapi,
)

__all__ = [
    "OpenAPIDocument",
    "OpenAPIRegistry",
    "build_openapi",
]