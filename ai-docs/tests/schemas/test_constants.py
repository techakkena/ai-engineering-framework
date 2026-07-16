"""Tests for ai_docs.schemas.constants."""

from __future__ import annotations

from ai_docs.schemas import constants


def test_default_values() -> None:
    assert constants.DEFAULT_SCHEMA_NAME == "schema"
    assert constants.DEFAULT_SCHEMA_FORMAT == "json-schema"
    assert constants.DEFAULT_ENABLED is True


def test_supported_schema_formats() -> None:
    assert constants.SUPPORTED_SCHEMA_FORMATS == frozenset(
        {
            "json-schema",
            "openapi",
            "avro",
            "protobuf",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_SCHEMA_NAME_LENGTH == 3
    assert constants.MAX_SCHEMA_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.FORMAT_KEY == "format"
    assert constants.CONTENT_KEY == "content"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"