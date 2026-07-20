from __future__ import annotations

from ai_prompts.templates.constants import (
    DEFAULT_TEMPLATE_NAME,
    DEFAULT_TEMPLATE_VERSION,
    SUPPORTED_TEMPLATE_EXTENSIONS,
)


def test_default_template_name():
    assert DEFAULT_TEMPLATE_NAME == "default"


def test_default_template_version():
    assert DEFAULT_TEMPLATE_VERSION == "1.0"


def test_supported_extensions():
    assert ".txt" in SUPPORTED_TEMPLATE_EXTENSIONS
