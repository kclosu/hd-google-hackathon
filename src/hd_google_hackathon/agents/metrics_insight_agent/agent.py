from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL

def synthesize_kpis() -> dict:
    """Synthesizes operational KPIs from various data sources."""
    return {"status": "success", "kpis": {"avg_resolution_time": "24h"}}

def surface_systemic_issues() -> dict:
    """Surfaces systemic issues based on the analysis of operational data."""
    return {"status": "success", "issues": ["Systemic Risk: Component 'CPU-001' has caused 5 order delays this week. Flagging for supply chain review."]}

def provide_insights() -> dict:
    """Provides data-driven insights to support business decisions."""
    # Placeholder implementation
    return {"status": "success", "insights": ["Dealer training for product Y needs improvement."]}

def print_dealer() -> dict:
    """Prints dealer information."""
    # Placeholder implementation
    return {"status": "success", "dealer": str(d)}


root_agent = Agent(
    name="metrics_insight_agent",
    model=DEFAULT_MODEL,
    description="Synthesizes operational KPIs, surfacing systemic issues (e.g., recurring part shortages or dealer training gaps).",
    tools=[
        synthesize_kpis,
        surface_systemic_issues,
        provide_insights,
    ],
)