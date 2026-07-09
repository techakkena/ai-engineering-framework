import pytest
from unittest.mock import AsyncMock
from ai.providers.base_provider import BaseProvider
from ai.providers.openai_provider import OpenAIProvider


def test_base_provider_is_abstract():
    with pytest.raises(TypeError):
        BaseProvider()

def test_openai_provider_creation():

    provider = OpenAIProvider(
        api_key="dummy-key"
    )

    assert provider is not None

@pytest.mark.asyncio
async def test_health():

    provider = OpenAIProvider(
        api_key="dummy"
    )

    health = await provider.health()

    assert health.provider == "openai"
    assert health.status == "healthy"

@pytest.mark.asyncio
async def test_close():

    provider = OpenAIProvider(
        api_key="dummy"
    )

    provider.client.close = AsyncMock()

    await provider.close()

    provider.client.close.assert_awaited_once()