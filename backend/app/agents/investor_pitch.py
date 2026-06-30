from app.services.groq_service import GroqService


class InvestorPitchAgent:
    def __init__(self):
        self.groq = GroqService()

    def generate(self, optimized_startup: str) -> str:
        prompt = f"""
You are an experienced Venture Capitalist and Startup Pitch Consultant.

Based on the startup below, generate a professional investor-ready startup report.

Startup Details:
{optimized_startup}

The report must contain the following sections in markdown format:

# Executive Summary

# Startup Name

# Vision & Mission

# Problem Statement

# Proposed Solution

# Target Customers

# Market Analysis

# TAM / SAM / SOM

# Business Model

# Revenue Streams

# Competitive Advantage

# SWOT Analysis

# Marketing Strategy

# Go-To-Market Strategy

# Financial Projection

# Funding Requirement

# Investment Ask

# 30-60-90 Day Roadmap

# Conclusion

Make the report detailed, professional, investor-friendly, and suitable for PDF export.
"""

        return self.groq.generate_response(prompt)