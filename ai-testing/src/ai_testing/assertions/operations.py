"""Operations for the ai_testing.assertions module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_testing.assertions.constants import (
    DEFAULT_STRICT,
    MAX_ASSERTION_NAME_LENGTH,
    MIN_ASSERTION_NAME_LENGTH,
    STATUS_FAILED,
    STATUS_PASSED,
    SUPPORTED_ASSERTION_STATUSES,
)
from ai_testing.assertions.exceptions import (
    AssertionValidationError,
    UnsupportedAssertionStatusError,
)


@dataclass(slots=True, frozen=True)
class AssertionResult:
    """Represents the outcome of an assertion."""

    name: str
    passed: bool
    expected: object
    actual: object
    message: str = ""

    def status(self) -> str:
        """Return the assertion status."""
        return STATUS_PASSED if self.passed else STATUS_FAILED


class AssertionRunner:
    """Runs assertion operations."""

    def evaluate(
        self,
        *,
        name: str,
        expected: object,
        actual: object,
        strict: bool = DEFAULT_STRICT,
    ) -> AssertionResult:
        """Evaluate an equality assertion."""
        normalized = name.strip()

        if not (
            MIN_ASSERTION_NAME_LENGTH
            <= len(normalized)
            <= MAX_ASSERTION_NAME_LENGTH
        ):
            raise AssertionValidationError(
                "Assertion name length is outside the allowed range."
            )

        passed = expected == actual if strict else str(expected) == str(actual)

        return AssertionResult(
            name=normalized,
            passed=passed,
            expected=expected,
            actual=actual,
            message="" if passed else "Assertion failed.",
        )


def assert_equal(
    *,
    name: str,
    expected: object,
    actual: object,
    strict: bool = DEFAULT_STRICT,
) -> AssertionResult:
    """Evaluate an equality assertion."""
    result = AssertionRunner().evaluate(
        name=name,
        expected=expected,
        actual=actual,
        strict=strict,
    )

    if result.status() not in SUPPORTED_ASSERTION_STATUSES:
        raise UnsupportedAssertionStatusError(
            f"Unsupported assertion status: {result.status()!r}."
        )

    return result


__all__ = [
    "AssertionResult",
    "AssertionRunner",
    "assert_equal",
]