from .base_agent import BaseAgent
from constants.ai_constants import AIProvider, ChatModels

class DemoAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Demo Agent",
            provider=AIProvider.OPENAI,
            model=ChatModels.GPT_5_5,
        )

    def chat(self, prompt):

        return f"AI Response: {prompt}"

    def generate(self):

        return "Generated Content"


def main():

    agent = DemoAgent()

    agent.initialize()

    print()

    print(agent.get_agent_info())

    print()

    print(agent.chat("Hello"))

    print()

    print(agent.generate())


if __name__ == "__main__":
    main()