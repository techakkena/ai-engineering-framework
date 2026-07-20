from __future__ import annotations

from base.base_agent import BaseAgent
from constants.ai_constants import AIProvider, ChatModels


class DemoAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Demo Agent",
            provider=AIProvider.OPENAI,
            model=ChatModels.GPT_5_5,
        )

    def chat(self, prompt: str) -> str:
        return f"AI Response: {prompt}"

    def generate(self) -> str:
        return "Generated Content"


def test_demo_agent_creation():
    agent = DemoAgent()

    assert agent is not None
    assert agent.name == "Demo Agent"
    assert agent.provider == AIProvider.OPENAI
    assert agent.model == ChatModels.GPT_5_5


def test_chat():
    agent = DemoAgent()

    result = agent.chat("Hello")

    assert result == "AI Response: Hello"


def test_generate():
    agent = DemoAgent()

    result = agent.generate()

    assert result == "Generated Content"
