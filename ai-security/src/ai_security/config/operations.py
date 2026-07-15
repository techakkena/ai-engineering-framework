"""
Framework-independent configuration management for ai_security.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_security.config.constants import (
    DEFAULT_ENVIRONMENT,
    DEFAULT_LOG_LEVEL,
    DEFAULT_TIMEOUT_SECONDS,
)
from ai_security.config.exceptions import (
    ConfigurationValidationError,
    MissingConfigurationError,
)


@dataclass(slots=True)
class SecurityConfig:
    """Represents security configuration."""

    environment: str = DEFAULT_ENVIRONMENT
    log_level: str = DEFAULT_LOG_LEVEL
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS
    settings: dict[str, Any] = field(default_factory=dict)


class SecurityConfigManager:
    """Framework-independent security configuration manager."""

    def __init__(self, config: SecurityConfig | None = None) -> None:
        self._config = config or SecurityConfig()

    @property
    def config(self) -> SecurityConfig:
        """Return the active configuration."""
        return self._config

    def get(self, key: str) -> Any:
        """Retrieve a configuration value."""
        if key not in self._config.settings:
            raise MissingConfigurationError(
                f"Configuration '{key}' does not exist."
            )

        return self._config.settings[key]

    def set(self, key: str, value: Any) -> None:
        """Store a configuration value."""
        self._config.settings[key] = value

    def validate(self) -> bool:
        """Validate the active configuration."""
        if self._config.timeout_seconds <= 0:
            raise ConfigurationValidationError(
                "timeout_seconds must be greater than zero."
            )

        if not self._config.environment:
            raise ConfigurationValidationError(
                "environment cannot be empty."
            )

        if not self._config.log_level:
            raise ConfigurationValidationError(
                "log_level cannot be empty."
            )

        return True

    def update(self, **settings: Any) -> None:
        """Update multiple configuration values."""
        self._config.settings.update(settings)

    def clear(self) -> None:
        """Remove all custom configuration values."""
        self._config.settings.clear()