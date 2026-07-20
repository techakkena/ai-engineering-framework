from __future__ import annotations

"""
AI Engineering Framework
Chat Models Tests

Author : TECHAKKENA
"""

from ai.providers.models.chat_models import ChatModels


def test_gpt5():
    assert ChatModels.GPT5 == "gpt-5"


def test_gpt5_mini():
    assert ChatModels.GPT5_MINI == "gpt-5-mini"


def test_gpt5_nano():
    assert ChatModels.GPT5_NANO == "gpt-5-nano"


def test_gpt4_1():
    assert ChatModels.GPT4_1 == "gpt-4.1"


def test_gpt4_1_mini():
    assert ChatModels.GPT4_1_MINI == "gpt-4.1-mini"


def test_gpt4o():
    assert ChatModels.GPT4O == "gpt-4o"


def test_gpt4o_mini():
    assert ChatModels.GPT4O_MINI == "gpt-4o-mini"


def test_o1():
    assert ChatModels.O1 == "o1"


def test_o3():
    assert ChatModels.O3 == "o3"


def test_o4_mini():
    assert ChatModels.O4_MINI == "o4-mini"
