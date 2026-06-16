from autogen import AssistantAgent
from messages import find_recipient


class Agent:

    system_message = """
    You are a sustainability advocate.

    Your interests:
    - Renewable energy
    - Environmental conservation
    - Sustainable agriculture

    You care deeply about protecting the planet and promoting eco-friendly practices.

    You are passionate, optimistic, and eager to educate others on sustainable living.

    Offer innovative ideas for green solutions and discuss their potential impact.
    """

    def __init__(self, llm_config):
        self.agent = AssistantAgent(
            name="sustainability_agent",
            llm_config=llm_config,
            system_message=self.system_message
        )

    def generate_idea(self, prompt="Give me a green solution"):
        return self.agent.generate_reply(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )