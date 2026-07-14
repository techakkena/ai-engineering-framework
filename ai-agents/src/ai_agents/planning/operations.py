from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class PlanStep:
    """Represents one planning step."""

    id: int
    description: str


@dataclass(slots=True)
class Plan:
    """Execution plan."""

    steps: list[PlanStep] = field(default_factory=list)

    def add_step(self, step: PlanStep) -> None:
        """Add a planning step."""
        self.steps.append(step)

    @property
    def size(self) -> int:
        """Return number of steps."""
        return len(self.steps)


class SimplePlanner:
    """Simple sequential planner."""

    def create_plan(self, task: str) -> Plan:
        """Create a one-step execution plan."""

        plan = Plan()

        plan.add_step(
            PlanStep(
                id=1,
                description=task,
            )
        )

        return plan
