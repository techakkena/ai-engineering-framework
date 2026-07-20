from __future__ import annotations

from ai_workflows.steps.constants import (
    DEFAULT_STEP_DESCRIPTION,
    DEFAULT_STEP_NAME,
)


def test_default_step_name() -> None:
    assert DEFAULT_STEP_NAME == "step"


def test_default_step_description() -> None:
    assert "Default" in DEFAULT_STEP_DESCRIPTION
