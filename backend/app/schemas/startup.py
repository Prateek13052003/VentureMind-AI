from pydantic import BaseModel


class StartupRequest(BaseModel):
    startup_domain: str
    problem_statement: str


class StartupResponse(BaseModel):
    startup_idea: str
    business_plan: str
    critique: str
    optimized_plan: str
    investor_pitch: str