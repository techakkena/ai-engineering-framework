"""
Unit tests for config operations.
"""

from ai_config.config.operations import Config


def test_create_config() -> None:
    config = Config()

    assert config is not None


def test_set_value() -> None:
    config = Config()

    config.set("host", "localhost")

    assert config.get("host") == "localhost"


def test_get_default() -> None:
    config = Config()

    assert config.get("missing", "default") == "default"


def test_remove_value() -> None:
    config = Config()

    config.set("host", "localhost")
    config.remove("host")

    assert config.get("host") is None


def test_clear() -> None:
    config = Config()

    config.set("a", 1)
    config.clear()

    assert config.items() == {}


def test_keys() -> None:
    config = Config()

    config.set("a", 1)

    assert "a" in config.keys()


def test_values() -> None:
    config = Config()

    config.set("a", 1)

    assert 1 in config.values()


def test_items() -> None:
    config = Config()

    config.set("a", 1)

    assert config.items()["a"] == 1


def test_default_profile() -> None:
    config = Config()

    assert config.profile() == "default"
