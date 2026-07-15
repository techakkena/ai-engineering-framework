"""
Tests for ai_deployment.ci_cd.constants.
"""

from ai_deployment.ci_cd.constants import (
    DEFAULT_BRANCH,
    DEFAULT_PIPELINE_NAME,
    DEFAULT_TRIGGER,
)


def test_default_pipeline_name() -> None:
    assert DEFAULT_PIPELINE_NAME == "default"


def test_default_branch() -> None:
    assert DEFAULT_BRANCH == "main"


def test_default_trigger() -> None:
    assert DEFAULT_TRIGGER == "push"