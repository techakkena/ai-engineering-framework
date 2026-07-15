"""
Tests for ai_security.config.operations.
"""

import pytest

from ai_security.config.constants import (
    DEFAULT_ENVIRONMENT,
    DEFAULT_LOG_LEVEL,
    DEFAULT_TIMEOUT_SECONDS,
)
from ai_security.config.exceptions import (
    ConfigurationValidationError,
    MissingConfigurationError,
)
from ai_security.config.operations import (
    SecurityConfig,
    SecurityConfigManager,
)


def test_default_security_config() -> None:
    """Test default SecurityConfig values."""
    config = SecurityConfig()

    assert config.environment == DEFAULT_ENVIRONMENT
    assert config.log_level == DEFAULT_LOG_LEVEL
    assert config.timeout_seconds == DEFAULT_TIMEOUT_SECONDS
    assert config.settings == {}


def test_manager_default_config() -> None:
    """Test SecurityConfigManager default initialization."""
    manager = SecurityConfigManager()

    assert isinstance(manager.config, SecurityConfig)


def test_set_and_get_configuration() -> None:
    """Test storing and retrieving configuration values."""
    manager = SecurityConfigManager()

    manager.set("api_key", "secret")

    assert manager.get("api_key") == "secret"


def test_get_missing_configuration() -> None:
    """Getting a missing configuration should raise."""
    manager = SecurityConfigManager()

    with pytest.raises(MissingConfigurationError):
        manager.get("missing")


def test_update_configuration() -> None:
    """Test updating multiple configuration values."""
    manager = SecurityConfigManager()

    manager.update(
        host="localhost",
        port=8080,
        debug=True,
    )

    assert manager.get("host") == "localhost"
    assert manager.get("port") == 8080
    assert manager.get("debug") is True


def test_clear_configuration() -> None:
    """Test clearing configuration values."""
    manager = SecurityConfigManager()

    manager.set("key", "value")

    manager.clear()

    with pytest.raises(MissingConfigurationError):
        manager.get("key")


def test_validate_success() -> None:
    """Validation should succeed for default configuration."""
    manager = SecurityConfigManager()

    assert manager.validate() is True


def test_validate_invalid_timeout() -> None:
    """Validation should fail for invalid timeout."""
    config = SecurityConfig(timeout_seconds=0)

    manager = SecurityConfigManager(config)

    with pytest.raises(ConfigurationValidationError):
        manager.validate()


def test_validate_empty_environment() -> None:
    """Validation should fail for empty environment."""
    config = SecurityConfig(environment="")

    manager = SecurityConfigManager(config)

    with pytest.raises(ConfigurationValidationError):
        manager.validate()


def test_validate_empty_log_level() -> None:
    """Validation should fail for empty log level."""
    config = SecurityConfig(log_level="")

    manager = SecurityConfigManager(config)

    with pytest.raises(ConfigurationValidationError):
        manager.validate()