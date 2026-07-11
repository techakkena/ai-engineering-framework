"""
AI Engineering Framework
Moderation Models Tests

Author : TECHAKKENA
"""

from ai.providers.models import ModerationModels


def test_omni():
    assert ModerationModels.OMNI_MODERATION_LATEST.value == "omni-moderation-latest"


def test_text():
    assert ModerationModels.TEXT_MODERATION_LATEST.value == "text-moderation-latest"
