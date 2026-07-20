from __future__ import annotations

from config.settings import settings


def test_settings_loaded():
    assert settings is not None


def test_app_name():
    assert settings.APP_NAME is not None
    assert settings.APP_NAME != ""


def test_version():
    assert settings.VERSION is not None
    assert settings.VERSION != ""


def test_debug_mode():
    assert isinstance(settings.DEBUG, bool)


def test_api_host():
    assert settings.API_HOST is not None
    assert settings.API_HOST != ""


def test_api_port():
    assert isinstance(settings.API_PORT, int)
    assert settings.API_PORT > 0


def test_openai_api_key():
    assert settings.OPENAI_API_KEY is not None
    assert settings.OPENAI_API_KEY != ""


def test_openai_model():
    assert settings.OPENAI_MODEL is not None
    assert settings.OPENAI_MODEL != ""
