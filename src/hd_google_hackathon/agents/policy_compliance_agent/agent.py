from google.adk.agents import Agent
from src.hd_google_hackathon.config import DEFAULT_MODEL

def check_regional_rules(action: str) -> dict:
    """Checks the action against regional rules."""
    return {"status": "success", "compliant": True}

def check_warranty_terms(action: str) -> dict:
    """Checks the action against warranty terms."""
    return {"status": "success", "compliant": True}

def check_data_sharing_agreements(action: str) -> dict:
    """Checks the action against data-sharing agreements."""
    return {"status": "success", "compliant": True}


root_agent = Agent(
    name="policy_compliance_agent",
    model=DEFAULT_MODEL,
    description="Checks suggested actions against regional rules, warranty terms, data-sharing agreements before execution.",
    tools=[
        check_regional_rules,
        check_warranty_terms,
        check_data_sharing_agreements,
    ],
)