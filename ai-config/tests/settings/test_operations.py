"""
Tests for settings operations.
"""

import pytest

from ai_config.settings.exceptions import SettingNotFoundError
from ai_config.settings.operations import Settings


def test_create_settings() -> None:
    settings = Settings()

    assert len(settings) == 0


def test_set_value() -> None:
    settings = Settings()

    settings.set("host", "localhost")

    assert settings.get("host") == "localhost"


def test_get_default() -> None:
    settings = Settings()

    assert settings.get("port", 8000) == 8000


def test_has_value() -> None:
    settings = Settings({"debug": True})

    assert settings.has("debug")


def test_contains() -> None:
    settings = Settings({"host": "localhost"})

    assert "host" in settings


def test_require() -> None:
    settings = Settings({"host": "localhost"})

    assert settings.require("host") == "localhost"


def test_require_missing() -> None:
    settings = Settings()

    with pytest.raises(SettingNotFoundError):
        settings.require("missing")


def test_remove() -> None:
    settings = Settings({"host": "localhost"})

    settings.remove("host")

    assert not settings.has("host")


def test_merge() -> None:
    settings = Settings({"host": "localhost"})

    settings.merge({"port": 8000})

    assert settings.get("port") == 8000


def test_clear() -> None:
    settings = Settings({"host": "localhost"})

    settings.clear()

    assert len(settings) == 0


def test_to_dict() -> None:
    settings = Settings({"host": "localhost"})

    data = settings.to_dict()

    assert data == {"host": "localhost"}
