from __future__ import annotations

"""
AI Engineering Framework
Speech Models

Author : TECHAKKENA
"""

from enum import Enum


class SpeechModels(str, Enum):
    """
    Supported speech models.
    """

    TTS_1 = "tts-1"

    TTS_1_HD = "tts-1-hd"

    WHISPER_1 = "whisper-1"

    GPT4O_TRANSCRIBE = "gpt-4o-transcribe"
