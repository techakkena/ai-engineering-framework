"""
AI Engineering Framework
Image Models

Author : TECHAKKENA
"""

from enum import Enum


class ImageModels(str, Enum):
    """
    Supported image generation models.
    """

    GPT_IMAGE_1 = "gpt-image-1"

    DALL_E_2 = "dall-e-2"

    DALL_E_3 = "dall-e-3"
