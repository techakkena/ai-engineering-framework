"""
Unit tests for ai_api.base.constants.
"""

from __future__ import annotations

from ai_api.base.constants import (
    DEFAULT_API_VERSION,
    DEFAULT_CONTENT_TYPE,
    DEFAULT_DOCS_PATH,
    DEFAULT_OPENAPI_PATH,
    DEFAULT_PREFIX,
    DEFAULT_REDOC_PATH,
    DEFAULT_TIMEOUT,
    JSON_MEDIA_TYPE,
    SUPPORTED_HTTP_METHODS,
)


def test_default_api_version() -> None:
    assert DEFAULT_API_VERSION == "v1"


def test_default_prefix() -> None:
    assert DEFAULT_PREFIX == "/api"


def test_default_timeout() -> None:
    assert DEFAULT_TIMEOUT == 30


def test_default_content_type() -> None:
    assert DEFAULT_CONTENT_TYPE == "application/json"


def test_json_media_type() -> None:
    assert JSON_MEDIA_TYPE == "application/json"


def test_openapi_path() -> None:
    assert DEFAULT_OPENAPI_PATH == "/openapi.json"


def test_docs_path() -> None:
    assert DEFAULT_DOCS_PATH == "/docs"


def test_redoc_path() -> None:
    assert DEFAULT_REDOC_PATH == "/redoc"


def test_supported_http_methods() -> None:
    expected = {
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
        "HEAD",
        "OPTIONS",
    }

    assert SUPPORTED_HTTP_METHODS == expected


def test_supported_http_methods_are_uppercase() -> None:
    assert all(method.isupper() for method in SUPPORTED_HTTP_METHODS)
