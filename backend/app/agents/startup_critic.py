from app.services.groq_service import GroqService


class StartupCriticAgent:
    def __init__(self):
        self.groq = GroqService()

    def critique(self, startup_plan: str) -> str:
        prompt = f"""
You are a startup investor and business analyst.

Critically evaluate the following startup plan.

Startup Plan:
{startup_plan}

Provide a detailed analysis covering:

1. Strengths
2. Weaknesses
3. Risks
4. Market Challenges
5. Competitive Threats
6. Financial Risks
7. Legal & Regulatory Concerns
8. Suggestions for Improvement

Return the analysis in professional markdown.
"""

        return self.groq.generate_response(prompt)