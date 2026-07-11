"""
AI Engineering Framework
Image Models Tests

Author : TECHAKKENA
"""

from ai.providers.models import ImageModels


def test_gpt_image():
    assert ImageModels.GPT_IMAGE_1.value == "gpt-image-1"


def test_dalle2():
    assert ImageModels.DALL_E_2.value == "dall-e-2"


def test_dalle3():
    assert ImageModels.DALL_E_3.value == "dall-e-3"
