from __future__ import annotations

from ai_workflows.conditions.constants import (
    DEFAULT_CONDITION_DESCRIPTION,
    DEFAULT_CONDITION_NAME,
)


def test_default_condition_name() -> None:
    assert DEFAULT_CONDITION_NAME == "condition"


def test_default_condition_description() -> None:
    assert "Default" in DEFAULT_CONDITION_DESCRIPTION
