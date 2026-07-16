"""Operations for the ai_testing.pytest module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_testing.pytest.constants import (
    DEFAULT_FAIL_FAST,
    DEFAULT_TEST_PATH,
    DEFAULT_VERBOSE,
    MAX_CONFIGURATION_NAME_LENGTH,
    MIN_CONFIGURATION_NAME_LENGTH,
)
from ai_testing.pytest.exceptions import PytestValidationError


@dataclass(slots=True, frozen=True)
class PytestConfiguration:
    """Represents a pytest execution configuration."""

    name: str
    test_path: str = DEFAULT_TEST_PATH
    verbose: bool = DEFAULT_VERBOSE
    fail_fast: bool = DEFAULT_FAIL_FAST

    def __post_init__(self) -> None:
        """Validate the configuration."""
        normalized = self.name.strip()

        if not (
            MIN_CONFIGURATION_NAME_LENGTH
            <= len(normalized)
            <= MAX_CONFIGURATION_NAME_LENGTH
        ):
            raise PytestValidationError(
                "Configuration name length is outside the allowed range."
            )

        if not self.test_path.strip():
            raise PytestValidationError(
                "Test path cannot be empty."
            )

        object.__setattr__(self, "name", normalized)
        object.__setattr__(self, "test_path", self.test_path.strip())


class PytestRunner:
    """Represents a lightweight pytest runner."""

    def build_command(
        self,
        configuration: PytestConfiguration,
    ) -> tuple[str, ...]:
        """Build a pytest command."""

        command: list[str] = [
            "pytest",
            configuration.test_path,
        ]

        if configuration.verbose:
            command.append("-v")

        if configuration.fail_fast:
            command.append("-x")

        return tuple(command)


def build_configuration(
    *,
    name: str,
    test_path: str = DEFAULT_TEST_PATH,
    verbose: bool = DEFAULT_VERBOSE,
    fail_fast: bool = DEFAULT_FAIL_FAST,
) -> PytestConfiguration:
    """Build a validated pytest configuration."""

    return PytestConfiguration(
        name=name,
        test_path=test_path,
        verbose=verbose,
        fail_fast=fail_fast,
    )


__all__ = [
    "PytestConfiguration",
    "PytestRunner",
    "build_configuration",
]