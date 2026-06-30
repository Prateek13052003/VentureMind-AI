from app.services.groq_service import GroqService


class BusinessOptimizerAgent:
    def __init__(self):
        self.groq = GroqService()

    def optimize(self, startup_plan: str, critique: str) -> str:
        prompt = f"""
You are an expert Startup Business Optimizer.

Your task is to improve the startup by addressing every issue raised in the critique.

Startup Plan:
{startup_plan}

Critique:
{critique}

Generate an optimized version including:

1. Improved Business Model
2. Risk Mitigation
3. Better Revenue Strategy
4. Stronger Competitive Advantage
5. Improved Scalability
6. Customer Retention Strategy
7. Operational Improvements
8. Financial Sustainability

Return the optimized startup plan in professional markdown.
"""

        return self.groq.generate_response(prompt)