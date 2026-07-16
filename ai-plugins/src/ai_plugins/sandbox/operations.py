"""Operations for the ai_plugins.sandbox module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_plugins.sandbox.constants import (
    DEFAULT_ENABLED,
    DEFAULT_SANDBOX_MODE,
    MAX_SANDBOX_NAME_LENGTH,
    MIN_SANDBOX_NAME_LENGTH,
    SUPPORTED_SANDBOX_MODES,
)
from ai_plugins.sandbox.exceptions import (
    DuplicateSandboxError,
    SandboxNotFoundError,
    SandboxValidationError,
    UnsupportedSandboxModeError,
)


@dataclass(slots=True, frozen=True)
class SandboxDefinition:
    """Represents a sandbox configuration."""

    name: str
    memory_limit: int
    mode: str = DEFAULT_SANDBOX_MODE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the sandbox definition."""
        normalized = self.name.strip()

        if not (
            MIN_SANDBOX_NAME_LENGTH
            <= len(normalized)
            <= MAX_SANDBOX_NAME_LENGTH
        ):
            raise SandboxValidationError(
                "Sandbox name length is outside the allowed range."
            )

        if self.memory_limit <= 0:
            raise SandboxValidationError(
                "Memory limit must be greater than zero."
            )

        if self.mode not in SUPPORTED_SANDBOX_MODES:
            raise UnsupportedSandboxModeError(
                f"Unsupported sandbox mode: {self.mode!r}."
            )

        object.__setattr__(self, "name", normalized)


class SandboxRegistry:
    """Registry for sandbox definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, SandboxDefinition] = {}

    def register(
        self,
        sandbox: SandboxDefinition,
    ) -> None:
        """Register a sandbox definition."""
        if sandbox.name in self._definitions:
            raise DuplicateSandboxError(
                f"Sandbox {sandbox.name!r} is already registered."
            )

        self._definitions[sandbox.name] = sandbox

    def unregister(self, name: str) -> None:
        """Remove a sandbox definition."""
        if name not in self._definitions:
            raise SandboxNotFoundError(
                f"Sandbox {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> SandboxDefinition:
        """Return a registered sandbox definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise SandboxNotFoundError(
                f"Sandbox {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a sandbox exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered sandboxes."""
        self._definitions.clear()

    def list(self) -> tuple[SandboxDefinition, ...]:
        """Return all registered sandboxes."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered sandboxes."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a sandbox exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_sandbox(
    *,
    name: str,
    memory_limit: int,
    mode: str = DEFAULT_SANDBOX_MODE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> SandboxDefinition:
    """Build and validate a sandbox definition."""

    return SandboxDefinition(
        name=name,
        memory_limit=memory_limit,
        mode=mode,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "SandboxDefinition",
    "SandboxRegistry",
    "build_sandbox",
]