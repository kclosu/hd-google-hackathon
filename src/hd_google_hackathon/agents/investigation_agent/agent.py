from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL
from hd_google_hackathon.data.repositories.order_repository import OrderRepository
from hd_google_hackathon.data.repositories.component_repository import ComponentRepository
from hd_google_hackathon.utils.tooling import bind_tool

def pull_order_history(order_id: str, order_repo: OrderRepository) -> dict:
    """Pulls order history for a given order ID."""
    order = order_repo.get_order_by_id(order_id, tenant_id="dummy") # tenant_id is handled by repo injection
    if order:
        return {"status": "success", "history": str(order)}
    return {"status": "error", "message": f"Order with ID {order_id} not found."}

def check_component_stock(component_id: str, component_repo: ComponentRepository) -> dict:
    """Checks the stock level for a given component ID."""
    stock = component_repo.get_component_stock(component_id, tenant_id="dummy")
    return {"status": "success", "component_id": component_id, "stock": stock}

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

from hd_google_hackathon.data.repositories.dummy_order_repository import DummyOrderRepository
from hd_google_hackathon.data.repositories.dummy_component_repository import DummyComponentRepository

def create_agent(order_repo: OrderRepository, component_repo: ComponentRepository) -> Agent:
    return Agent(
        name="investigation_agent",
        model=DEFAULT_MODEL,
        description="Pulls order history, production status, shipment telemetry; checks component stock; compares against standards to flag anomalies and propose resolutions.",
        tools=[
            bind_tool(pull_order_history, order_repo=order_repo),
            bind_tool(check_component_stock, component_repo=component_repo),
            pull_production_status,
            pull_shipment_telemetry,
            compare_with_standards,
            propose_resolution,
        ],
    )

root_agent = create_agent(
    order_repo=DummyOrderRepository(), 
    component_repo=DummyComponentRepository()
)
