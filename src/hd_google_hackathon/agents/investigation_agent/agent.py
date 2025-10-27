from google.adk.agents import Agent
from src.hd_google_hackathon.config import DEFAULT_MODEL

def pull_order_history(order_id: str) -> dict:
    """Pulls order history for a given order ID."""
    return {"status": "success", "history": "Order #12345 (Product: T-800 Endoskeleton) placed on 2025-10-26."}

def pull_production_status(order_id: str) -> dict:
    """Pulls production status for a given order ID."""
    return {"status": "success", "production_status": "in_progress"}

def pull_shipment_telemetry(order_id: str) -> dict:
    """Pulls shipment telemetry for a given order ID."""
    return {"status": "success", "telemetry": "Delayed. Root Cause: Component shortage at assembly plant."}

def compare_with_standards(data: dict) -> dict:
    """Compares data against standards to flag anomalies."""
    return {"status": "success", "anomalies": ["Shipment is delayed due to component shortage"]}

def propose_resolution(anomalies: list) -> dict:
    """Proposes resolutions for the flagged anomalies."""
    return {"status": "success", "resolution": "Re-route order fulfillment to the US-West plant and expedite shipment."}

root_agent = Agent(
    name="investigation_agent",
    model=DEFAULT_MODEL,
    description="Pulls order history, production status, shipment telemetry; compares against standards to flag anomalies and propose resolutions.",
    tools=[
        pull_order_history,
        pull_production_status,
        pull_shipment_telemetry,
        compare_with_standards,
        propose_resolution,
    ],
)