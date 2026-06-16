from autogen import AssistantAgent
from messages import find_recipient


class Agent:

    system_message = """
    You are a passionate environmental activist.

    Your interests:
    - Renewable energy
    - Sustainable development

    You have a deep sense of responsibility towards the environment and aim to create positive change through your work.

    You are determined, resourceful, and driven by a desire to make a difference.

    Provide innovative solutions for sustainability issues.
    """

    def __init__(self, llm_config):
        self.agent = AssistantAgent(
            name="eco_ambassador",
            llm_config=llm_config,
            system_message=self.system_message
        )

    def generate_sustainability_idea(self, prompt="Provide a sustainable solution"):
        return self.agent.generate_reply(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )