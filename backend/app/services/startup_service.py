from backend.app.agents.idea_generator import IdeaGeneratorAgent
from backend.app.agents.business_strategist import BusinessStrategistAgent
from backend.app.agents.startup_critic import StartupCriticAgent
from backend.app.agents.business_optimizer import BusinessOptimizerAgent
from backend.app.agents.investor_pitch import InvestorPitchAgent


class StartupService:

    def __init__(self):
        self.idea_agent = IdeaGeneratorAgent()
        self.strategy_agent = BusinessStrategistAgent()
        self.critic_agent = StartupCriticAgent()
        self.optimizer_agent = BusinessOptimizerAgent()
        self.pitch_agent = InvestorPitchAgent()

    def generate_startup_report(
        self,
        startup_domain: str,
        problem_statement: str
    ):

        # Step 1
        startup_idea = self.idea_agent.generate(
            startup_domain=startup_domain,
            problem_statement=problem_statement
        )

        # Step 2
        business_plan = self.strategy_agent.improve(
            startup_idea
        )

        # Step 3
        critique = self.critic_agent.critique(
            business_plan
        )

        # Step 4
        optimized_plan = self.optimizer_agent.optimize(
            business_plan,
            critique
        )

        # Step 5
        investor_pitch = self.pitch_agent.generate(
            optimized_plan
        )

        return {
            "startup_idea": startup_idea,
            "business_plan": business_plan,
            "critique": critique,
            "optimized_plan": optimized_plan,
            "investor_pitch": investor_pitch
        }