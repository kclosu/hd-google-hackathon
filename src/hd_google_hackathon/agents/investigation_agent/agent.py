from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL
from hd_google_hackathon.data.repositories.order_repository import OrderRepository
from hd_google_hackathon.data.repositories.component_repository import ComponentRepository
from hd_google_hackathon.utils.tooling import bind_tool

def pull_order_history(order_id: str, tenant_id: str, order_repo: OrderRepository) -> dict:
    """Pulls order history for a given order ID."""
    order = order_repo.get_order_by_id(order_id, tenant_id) # tenant_id is handled by repo injection
    if order:
        return {"status": "success", "history": str(order)}
    return {"status": "error", "message": f"Order with ID {order_id} not found."}

def check_component_stock(component_id: str, tenant_id: str, component_repo: ComponentRepository) -> dict:
    """Checks the stock level for a given component ID."""
    stock = component_repo.get_component_stock(component_id, tenant_id)
    return {"status": "success", "component_id": component_id, "stock": stock}

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
        ],
    )

root_agent = create_agent(
    order_repo=DummyOrderRepository(), 
    component_repo=DummyComponentRepository()
)
