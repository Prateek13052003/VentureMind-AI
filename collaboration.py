from agent1 import Agent as Agent1
from agent2 import Agent as Agent2
from agent3 import Agent as Agent3
from agent4 import Agent as Agent4
from agent5 import Agent as Agent5

llm_config = {
"config_list": [
{
"model": "qwen2.5:7b",
"base_url": "http://localhost:11434/v1",
"api_key": "ollama",
"price": [0, 0]
}
]
}

# =====================================================

# CREATE AGENTS

# =====================================================

a1 = Agent1(llm_config)
a2 = Agent2(llm_config)
a3 = Agent3(llm_config)
a4 = Agent4(llm_config)
a5 = Agent5(llm_config)

# =====================================================

# STEP 1 - IDEA GENERATION

# =====================================================

idea = a1.agent.generate_reply(
messages=[
{
"role": "user",
"content": "Generate a unique startup idea."
}
]
)

print("\n" + "=" * 80)
print("AGENT 1 - IDEA GENERATOR")
print("=" * 80)
print(idea)

# =====================================================

# STEP 2 - BUSINESS IMPROVEMENT

# =====================================================

improved_idea = a2.agent.generate_reply(
messages=[
{
"role": "user",
"content": f"""
Improve this startup idea.

Add:

* Better monetization
* Stronger competitive advantage
* Scalability
* Revenue streams

Startup Idea:

{idea}
"""
}
]
)

print("\n" + "=" * 80)
print("AGENT 2 - BUSINESS STRATEGIST")
print("=" * 80)
print(improved_idea)

# =====================================================

# STEP 3 - CRITIQUE

# =====================================================

critique = a3.agent.generate_reply(
messages=[
{
"role": "user",
"content": f"""
Critically analyze this startup.

Find:

* Risks
* Weaknesses
* Market challenges
* Competition
* Execution difficulties
* Financial risks

Startup:

{improved_idea}
"""
}
]
)

print("\n" + "=" * 80)
print("AGENT 3 - CRITIC")
print("=" * 80)
print(critique)

# =====================================================

# STEP 4 - OPTIMIZATION

# =====================================================

optimized_idea = a4.agent.generate_reply(
messages=[
{
"role": "user",
"content": f"""
Improve this startup.

ORIGINAL STARTUP:

{improved_idea}

CRITIQUE:

{critique}

Create an improved version that addresses every criticism.

Include:

* Risk mitigation
* Better business model
* Stronger competitive advantage
* Better scalability
* Better profitability
  """
  }
  ]
  )

print("\n" + "=" * 80)
print("AGENT 4 - OPTIMIZER")
print("=" * 80)
print(optimized_idea)

# =====================================================

# STEP 5 - INVESTOR PITCH

# =====================================================

pitch = a5.agent.generate_reply(
messages=[
{
"role": "user",
"content": f"""
Create a professional investor pitch.

Startup:

{optimized_idea}

Use this format:

1. Startup Name
2. Problem
3. Solution
4. Market Opportunity
5. Business Model
6. Competitive Advantage
7. Revenue Strategy
8. Go-To-Market Strategy
9. Financial Potential
10. Investment Ask

Make it sound like a startup seeking seed funding.
"""
}
]
)

print("\n" + "=" * 80)
print("AGENT 5 - INVESTOR PITCH")
print("=" * 80)
print(pitch)

# =====================================================

# =====================================================
# SAVE RESULTS
# =====================================================

with open("final_startup_pitch.md", "w", encoding="utf-8") as f:
    f.write("# Multi-Agent Startup Incubator\n\n")

    f.write("## Agent 1 - Idea\n\n")
    f.write(str(idea))
    f.write("\n\n")

    f.write("## Agent 2 - Improvement\n\n")
    f.write(str(improved_idea))
    f.write("\n\n")

    f.write("## Agent 3 - Critique\n\n")
    f.write(str(critique))
    f.write("\n\n")

    f.write("## Agent 4 - Optimization\n\n")
    f.write(str(optimized_idea))
    f.write("\n\n")

    f.write("## Agent 5 - Investor Pitch\n\n")
    f.write(str(pitch))

print("\n")
print("=" * 80)
print("WORKFLOW COMPLETE")
print("Output saved to final_startup_pitch.md")
print("=" * 80)