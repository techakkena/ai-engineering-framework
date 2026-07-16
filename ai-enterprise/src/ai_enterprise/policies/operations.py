"""Operations for the ai_enterprise.policies module."""

from __future__ import annotations

from dataclasses import dataclass, field

from ai_enterprise.policies.constants import (
    DEFAULT_ENABLED,
    DEFAULT_POLICY_TYPE,
    MAX_POLICY_NAME_LENGTH,
    MIN_POLICY_NAME_LENGTH,
    SUPPORTED_POLICY_TYPES,
)
from ai_enterprise.policies.exceptions import (
    DuplicatePolicyError,
    PolicyNotFoundError,
    PolicyValidationError,
    UnsupportedPolicyTypeError,
)


@dataclass(slots=True, frozen=True)
class EnterprisePolicy:
    """Represents an enterprise policy."""

    name: str
    policy_type: str = DEFAULT_POLICY_TYPE
    rules: tuple[str, ...] = field(default_factory=tuple)
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the policy."""
        normalized = self.name.strip()

        if not (
            MIN_POLICY_NAME_LENGTH
            <= len(normalized)
            <= MAX_POLICY_NAME_LENGTH
        ):
            raise PolicyValidationError(
                "Policy name length is outside the allowed range."
            )

        if self.policy_type not in SUPPORTED_POLICY_TYPES:
            raise UnsupportedPolicyTypeError(
                f"Unsupported policy type: {self.policy_type!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized,
        )


class PolicyRegistry:
    """Registry for enterprise policies."""

    __slots__ = ("_policies",)

    def __init__(self) -> None:
        self._policies: dict[
            str,
            EnterprisePolicy,
        ] = {}

    def register(
        self,
        policy: EnterprisePolicy,
    ) -> None:
        if policy.name in self._policies:
            raise DuplicatePolicyError(
                f"Policy {policy.name!r} is already registered."
            )

        self._policies[policy.name] = policy

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._policies:
            raise PolicyNotFoundError(
                f"Policy {name!r} is not registered."
            )

        del self._policies[name]

    def get(
        self,
        name: str,
    ) -> EnterprisePolicy:
        try:
            return self._policies[name]
        except KeyError as exc:
            raise PolicyNotFoundError(
                f"Policy {name!r} is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._policies

    def clear(self) -> None:
        self._policies.clear()

    def list(self) -> tuple[EnterprisePolicy, ...]:
        return tuple(self._policies.values())

    def __len__(self) -> int:
        return len(self._policies)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return (
            isinstance(name, str)
            and name in self._policies
        )


def build_policy(
    *,
    name: str,
    policy_type: str = DEFAULT_POLICY_TYPE,
    rules: tuple[str, ...] = (),
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> EnterprisePolicy:
    """Build a validated enterprise policy."""

    return EnterprisePolicy(
        name=name,
        policy_type=policy_type,
        rules=rules,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "EnterprisePolicy",
    "PolicyRegistry",
    "build_policy",
]