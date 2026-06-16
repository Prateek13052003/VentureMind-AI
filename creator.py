from autogen import AssistantAgent


class Creator:

    def __init__(self, llm_config):
        self.llm_config = llm_config

        self.creator_agent = AssistantAgent(
            name="creator",
            llm_config=llm_config,
            system_message="""
You create new AI agents.

You will receive a template agent.

Create a completely new version with:

- Different interests
- Different business domain
- Different personality
- Different goals

Keep the Python structure intact.

Return only valid Python code.
"""
        )

    def get_template(self):
        with open("agent.py", "r", encoding="utf-8") as f:
            return f.read()

    def create_agent_file(self, filename):

        template = self.get_template()

        prompt = f"""
Create a brand-new agent based on this template.

Requirements:
- Keep valid Python syntax
- Change the system message
- Give the agent a unique personality
- Different business vertical
- Different interests

Template:

{template}
"""

        response = self.creator_agent.generate_reply(
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

response = response.replace("```python", "")
response = response.replace("```", "")

with open(filename, "w", encoding="utf-8") as f:
    f.write(response)