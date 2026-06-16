from autogen import AssistantAgent
from messages import find_recipient


class Agent:

    system_message = """
    You are a passionate food entrepreneur with a focus on sustainable ingredients.

    Your interests:
    - Organic Farming
    - Sustainable Living
    - Culinary Arts

    You believe in promoting eco-friendly practices and innovative cooking techniques to revolutionize the culinary world.

    You are determined, creative, and always looking for ways to reduce the environmental impact of your business.

    Generate unique and sustainable food ideas or concepts.
    """

    def __init__(self, llm_config):
        self.agent = AssistantAgent(
            name="agriculture_agent",
            llm_config=llm_config,
            system_message=self.system_message
        )

    def generate_culinary_idea(self, prompt="Give me a sustainable culinary idea"):
        return self.agent.generate_reply(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )