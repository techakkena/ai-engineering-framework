from __future__ import annotations

from dataclasses import dataclass

from .constants import DEFAULT_MODEL_NAME


@dataclass(slots=True)
class TokenUsage:
    """Represents token usage."""

    prompt_tokens: int = 0
    completion_tokens: int = 0
    model: str = DEFAULT_MODEL_NAME

    @property
    def total_tokens(self) -> int:
        """Return total token count."""
        return self.prompt_tokens + self.completion_tokens


class TokenUsageRegistry:
    """Registry for token usage."""

    def __init__(self) -> None:
        self._usage: list[TokenUsage] = []

    def add(
        self,
        usage: TokenUsage,
    ) -> None:
        self._usage.append(usage)

    @property
    def total_prompt_tokens(self) -> int:
        return sum(item.prompt_tokens for item in self._usage)

    @property
    def total_completion_tokens(self) -> int:
        return sum(item.completion_tokens for item in self._usage)

    @property
    def total_tokens(self) -> int:
        return sum(item.total_tokens for item in self._usage)

    @property
    def count(self) -> int:
        return len(self._usage)
