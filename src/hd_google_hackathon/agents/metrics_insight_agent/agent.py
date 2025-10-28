from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL

def surface_systemic_issues() -> dict:
    """Surfaces systemic issues from a collection of resolved cases."""
    return {"issues": ["Systemic Risk: Component 'CPU-001' has caused 5 order delays this week. Flagging for supply chain review."]}

def predict_maintenance_needs(tenant_id: str) -> dict:
    """Analyzes historical data to predict future maintenance needs for a given tenant."""
    # In a real system, this would analyze real usage and failure data.
    # For this simulation, we'll return a hardcoded prediction.
    return {
        "prediction": "Product 'luminette' at dealer 'David' (tenant_id) has a 75% probability of chain failure in the next 3 months based on usage patterns.",
        "recommendation": "Proactively send replacement chain_2 and schedule maintenance."
    }

def create_agent() -> Agent:
    return Agent(
        name="metrics_insight_agent",
        model=DEFAULT_MODEL,
        description="Surfaces systemic issues and predicts maintenance needs from historical data.",
        tools=[
            surface_systemic_issues,
            predict_maintenance_needs,
        ],
    )

root_agent = create_agent()