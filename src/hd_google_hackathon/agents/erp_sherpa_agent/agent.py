from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL
from hd_google_hackathon.data.repositories.order_repository import OrderRepository
from hd_google_hackathon.utils.tooling import bind_tool


def update_shipment_priority(order_id: str, priority: str, tenant_id: str, order_repo: OrderRepository) -> dict:
    """Updates the shipment priority for a given order ID."""
    order = order_repo.update_shipment_priority(order_id, priority, tenant_id)
    if order:
        return {"status": "success", "message": f"Shipment priority for order #{order_id} updated to {priority}."}
    return {"status": "error", "message": f"Could not update shipment priority for order #{order_id}."}


def create_agent(order_repo: OrderRepository) -> Agent:
    return Agent(
        name="erp_sherpa_agent",
        model=DEFAULT_MODEL,
        description="Encapsulates knowledge of each ERP variant via tool connectors; translates high-level intents (“update shipment priority”) into correct transactions.",
        tools=[
            bind_tool(update_shipment_priority, order_repo=order_repo),
        ],
    )

from hd_google_hackathon.data.repositories.dummy_order_repository import DummyOrderRepository

root_agent = create_agent(order_repo=DummyOrderRepository())