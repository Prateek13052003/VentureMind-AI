from app.services.groq_service import GroqService


class IdeaGeneratorAgent:
    def __init__(self):
        self.groq = GroqService()

    def generate(self, startup_domain: str, problem_statement: str) -> str:
        prompt = f"""
You are an expert Startup Idea Generator.

Your job is to create a unique startup idea.

Startup Domain:
{startup_domain}

Problem Statement:
{problem_statement}

Generate a detailed startup idea including:

1. Startup Name
2. Problem
3. Proposed Solution
4. Target Customers
5. Unique Selling Proposition
6. Key Features

Return only the startup idea in professional markdown.
"""

        return self.groq.generate_response(prompt)