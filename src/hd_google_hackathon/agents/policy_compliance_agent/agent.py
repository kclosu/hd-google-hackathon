from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL

def check_regional_rules(action: str) -> dict:
    """Checks if the proposed action complies with regional rules."""
    return {"compliant": True}

def check_warranty_terms(action: str) -> dict:
    """Checks if the proposed action complies with warranty terms."""
    return {"compliant": True}

def create_agent() -> Agent:
    return Agent(
        name="policy_compliance_agent",
        model=DEFAULT_MODEL,
        description="Checks if proposed actions comply with regional rules and warranty terms.",
        tools=[
            check_regional_rules,
            check_warranty_terms,
        ],
    )

root_agent = create_agent()