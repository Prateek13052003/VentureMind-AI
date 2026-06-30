from backend.app.services.groq_service import GroqService


class BusinessStrategistAgent:
    def __init__(self):
        self.groq = GroqService()

    def improve(self, startup_idea: str) -> str:
        prompt = f"""
You are an experienced Startup Business Strategist.

Analyze the following startup idea and improve it.

Startup Idea:
{startup_idea}

Improve the following aspects:

1. Business Model
2. Revenue Streams
3. Competitive Advantage
4. Scalability
5. Customer Acquisition Strategy
6. Pricing Strategy
7. Long-Term Growth Plan

Return the improved startup plan in professional markdown.
"""

        return self.groq.generate_response(prompt)