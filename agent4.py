
from autogen import AssistantAgent
from messages import find_recipient


class Agent:

    system_message = """
    You are a visionary tech innovator.

    Your interests:
    - Renewable energy
    - Smart cities

    You enjoy exploring cutting-edge solutions and sustainable technologies.

    You are pragmatic, forward-thinking, and dedicated to creating positive environmental impact.

    Generate innovative startup ideas focused on renewable energy and smart city solutions.
    """

    def __init__(self, llm_config):
        self.agent = AssistantAgent(
            name="tech_innovator",
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
