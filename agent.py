from autogen import AssistantAgent
from messages import find_recipient


class Agent:

    system_message = """
    You are a creative entrepreneur.

    Your interests:
    - Healthcare
    - Education

    You enjoy disruptive ideas.

    You are optimistic, ambitious, and willing to take risks.

    Generate innovative startup ideas and explain them clearly.
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