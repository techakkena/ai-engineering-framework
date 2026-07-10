"""
AI Engineering Framework
Provider Factory Tests

Author : TECHAKKENA
"""

import pytest

from ai.providers.openai_provider import OpenAIProvider
from ai.providers.provider_factory import ProviderFactory
from ai.providers.types import ProviderConfig


def test_create_openai():
    provider = ProviderFactory.create(
        "openai",
        ProviderConfig(
            model="gpt-5",
            api_key="dummy",
        ),
    )

    assert isinstance(
        provider,
        OpenAIProvider,
    )


def test_create_uppercase():
    provider = ProviderFactory.create(
        "OPENAI",
        ProviderConfig(
            model="gpt-5",
            api_key="dummy",
        ),
    )

    assert isinstance(
        provider,
        OpenAIProvider,
    )


def test_invalid_provider():
    with pytest.raises(ValueError):
        ProviderFactory.create(
            "anthropic",
            ProviderConfig(
                model="claude",
            ),
        )
