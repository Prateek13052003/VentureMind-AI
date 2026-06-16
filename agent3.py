from autogen import AssistantAgent
from messages import find_recipient


class Agent:

    system_message = """
    You are a technology innovator.

    Your interests:
    - Renewable energy
    - Smart home automation

    You enjoy leveraging cutting-edge technology to solve complex problems.

    You are visionary, curious, and driven by the potential for global impact.

    Develop innovative solutions that combine renewable energy with smart home technologies.
    """

    def __init__(self, llm_config):
        self.agent = AssistantAgent(
            name="agent",
            llm_config=llm_config,
            system_message=self.system_message
        )

    def generate_idea(self, prompt="Give me a startup idea"):
        return self.agent.generate_reply(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )