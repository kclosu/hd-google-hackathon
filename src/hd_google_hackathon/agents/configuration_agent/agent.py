from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL

def validate_configuration(options: dict, tenant_id: str) -> dict:
    """Validates that a set of product options are compatible.
    For example, certain fabrics may not be available for certain headrails.
    """
    # In a real system, this would use a rules engine or knowledge graph.
    if options.get("fabric") == "fabric_1" and options.get("headrail") == "headrail_2":
        return {"valid": False, "reason": "Fabric 'fabric_1' is not compatible with headrail 'headrail_2'."}
    return {"valid": True}

def generate_quote(config: dict, tenant_id: str) -> dict:
    """Generates a price quote for a given valid configuration."""
    # Prices are for demonstration purposes.
    price = 100.0
    if config.get("motorized"):
        price += 50.0
    price *= config.get("quantity", 1)
    return {"quote": f"${price:.2f}"}

def create_agent() -> Agent:
    return Agent(
        name="configuration_agent",
        model=DEFAULT_MODEL,
        description="Helps dealers configure complex products, validates compatibility, and generates quotes.",
        tools=[
            validate_configuration,
            generate_quote,
        ],
    )

root_agent = create_agent()
