"""Operations for the ai_testing.mocks module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ai_testing.mocks.constants import (
    DEFAULT_ENABLED,
    DEFAULT_RESET_AFTER_USE,
    MAX_MOCK_NAME_LENGTH,
    MIN_MOCK_NAME_LENGTH,
)
from ai_testing.mocks.exceptions import (
    DuplicateMockError,
    MockNotFoundError,
    MockValidationError,
)


@dataclass(slots=True, frozen=True)
class MockDefinition:
    """Represents a registered mock."""

    name: str
    target: str
    value: Any
    enabled: bool = DEFAULT_ENABLED
    reset_after_use: bool = DEFAULT_RESET_AFTER_USE

    def __post_init__(self) -> None:
        """Validate the mock definition."""
        normalized = self.name.strip()

        if not (
            MIN_MOCK_NAME_LENGTH
            <= len(normalized)
            <= MAX_MOCK_NAME_LENGTH
        ):
            raise MockValidationError(
                "Mock name length is outside the allowed range."
            )

        if not self.target.strip():
            raise MockValidationError(
                "Mock target cannot be empty."
            )

        object.__setattr__(self, "name", normalized)
        object.__setattr__(self, "target", self.target.strip())


class MockRegistry:
    """Registry for mock definitions."""

    __slots__ = ("_mocks",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._mocks: dict[str, MockDefinition] = {}

    def register(self, mock: MockDefinition) -> None:
        """Register a mock."""
        if mock.name in self._mocks:
            raise DuplicateMockError(
                f"Mock {mock.name!r} is already registered."
            )

        self._mocks[mock.name] = mock

    def unregister(self, name: str) -> None:
        """Remove a registered mock."""
        if name not in self._mocks:
            raise MockNotFoundError(
                f"Mock {name!r} is not registered."
            )

        del self._mocks[name]

    def get(self, name: str) -> MockDefinition:
        """Retrieve a registered mock."""
        try:
            return self._mocks[name]
        except KeyError as exc:
            raise MockNotFoundError(
                f"Mock {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a mock exists."""
        return name in self._mocks

    def clear(self) -> None:
        """Clear the registry."""
        self._mocks.clear()

    def list(self) -> tuple[MockDefinition, ...]:
        """Return all registered mocks."""
        return tuple(self._mocks.values())

    def __len__(self) -> int:
        """Return the number of registered mocks."""
        return len(self._mocks)

    def __contains__(self, name: object) -> bool:
        """Return whether a mock exists."""
        return isinstance(name, str) and name in self._mocks


def build_mock(
    *,
    name: str,
    target: str,
    value: Any,
    enabled: bool = DEFAULT_ENABLED,
    reset_after_use: bool = DEFAULT_RESET_AFTER_USE,
) -> MockDefinition:
    """Build and validate a mock definition."""
    return MockDefinition(
        name=name,
        target=target,
        value=value,
        enabled=enabled,
        reset_after_use=reset_after_use,
    )


__all__ = [
    "MockDefinition",
    "MockRegistry",
    "build_mock",
]