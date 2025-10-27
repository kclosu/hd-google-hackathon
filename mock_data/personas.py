
from dataclasses import dataclass
from typing import List

@dataclass
class Persona:
    id: str
    name: str
    role: str
    description: str
    permissions: List[str]

personas = [
    Persona(
        id="support_agent_1",
        name="Sarah",
        role="Support Agent",
        description="A support agent in the US region, responsible for handling dealer inquiries and issues.",
        permissions=["read_orders", "create_ticket", "view_knowledge_base"]
    ),
    Persona(
        id="account_manager_1",
        name="Michael",
        role="Account Manager",
        description="An account manager for top-tier dealers in the US.",
        permissions=["read_orders", "view_dealer_information", "escalate_ticket"]
    ),
    Persona(
        id="planner_1",
        name="Maria",
        role="Production Planner",
        description="A production planner at the Fabric Plant.",
        permissions=["view_production_schedule", "view_component_inventory"]
    ),
    Persona(
        id="dealer_1_user",
        name="David",
        role="Dealer",
        description="A user from The Shade Store, responsible for placing orders and tracking shipments.",
        permissions=["place_order", "track_shipment", "view_invoices"]
    )
]
