from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL

def classify_request(request: str) -> dict:
    """Classifies the type of a support request."""
    return {"type": "urgent_order_inquiry"}

def enrich_request(request: str) -> dict:
    """Enriches a support request with additional context."""
    return {"enriched_request": "[Order ID: 12345] Our high-priority order is delayed!"}

def extract_sla(request: str) -> dict:
    """Extracts the SLA for a support request."""
    return {"sla": "1-hour response"}

def route_request(request: str) -> dict:
    """Routes the request to the appropriate queue."""
    return {"queue": "investigation_queue"}

def create_agent() -> Agent:
    return Agent(
        name="support_triage_agent",
        model=DEFAULT_MODEL,
        description="Classifies, enriches, and routes incoming support requests.",
        tools=[
            classify_request,
            enrich_request,
            extract_sla,
            route_request,
        ],
    )

root_agent = create_agent()