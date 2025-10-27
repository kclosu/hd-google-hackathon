from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL

def update_shipment_priority(order_id: str, priority: str) -> dict:
    """Updates the shipment priority for a given order ID."""
    return {"status": "success", "message": f"New, expedited order #12346 created from US-West plant to resolve issue with order #{order_id}."}

def get_erp_variant(order_id: str) -> str:
    """Determines the ERP variant for a given order ID."""
    return "erp_variant_1"

root_agent = Agent(
    name="erp_sherpa_agent",
    model=DEFAULT_MODEL,
    description="Encapsulates knowledge of each ERP variant via tool connectors; translates high-level intents (“update shipment priority”) into correct transactions.",
    tools=[update_shipment_priority],
)