from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL

def classify_request(request: str) -> dict:
    """Classifies the type of inbound request (e.g., ticket, chat)."""
    return {"status": "success", "type": "urgent_order_inquiry"}

def enrich_request(request: str) -> dict:
    """Enriches the request with relevant dealer context."""
    return {"status": "success", "enriched_request": request + " [Dealer Tier: Platinum]"}

def route_request(request: str) -> dict:
    """Routes the request to the appropriate support queue."""
    return {"status": "success", "queue": "investigation_queue"}

def extract_sla(request: str) -> dict:
    """Automatically extracts and sets Service Level Agreement (SLA) timers."""
    return {"status": "success", "sla": "1-hour response"}

root_agent = Agent(
    name="support_triage_agent",
    model=DEFAULT_MODEL,
    description="Classifies inbound tickets/chats, enriches with dealer context, routes to correct queue, auto-extracts SLA timers.",
    tools=[classify_request, enrich_request, route_request, extract_sla],
)