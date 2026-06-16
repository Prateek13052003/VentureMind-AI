from dataclasses import dataclass
import glob
import os
import random

@dataclass
class Message:
    content: str


def find_recipient():
    try:
        agent_files = glob.glob("agent*.py")

        agent_names = [
            os.path.splitext(file)[0]
            for file in agent_files
            if file != "agent.py"
        ]

        if not agent_names:
            return None

        return random.choice(agent_names)

    except Exception as e:
        print(f"Error finding recipient: {e}")
        return None