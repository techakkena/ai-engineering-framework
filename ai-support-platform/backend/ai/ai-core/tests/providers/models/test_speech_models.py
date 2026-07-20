from __future__ import annotations

"""
AI Engineering Framework
Speech Models Tests

Author : TECHAKKENA
"""

from ai.providers.models import SpeechModels


def test_tts1():
    assert SpeechModels.TTS_1.value == "tts-1"


def test_tts1_hd():
    assert SpeechModels.TTS_1_HD.value == "tts-1-hd"


def test_whisper():
    assert SpeechModels.WHISPER_1.value == "whisper-1"


def test_transcribe():
    assert SpeechModels.GPT4O_TRANSCRIBE.value == "gpt-4o-transcribe"
