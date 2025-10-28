from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL
from hd_google_hackathon.data.repositories.product_repository import ProductRepository
from hd_google_hackathon.utils.tooling import bind_tool

def get_product_components(product_id: str, tenant_id: str, product_repo: ProductRepository) -> dict:
    """Gets the component list for a given product ID."""
    product = product_repo.get_product_by_id(product_id, tenant_id)
    if product:
        return {"status": "success", "components": product.components}
    return {"status": "error", "message": f"Product with ID {product_id} not found."}


def create_agent(product_repo: ProductRepository) -> Agent:
    return Agent(
        name="installer_support_agent",
        model=DEFAULT_MODEL,
        description="Provides on-site support for installers by finding solutions in manuals and identifying product components.",
        tools=[
            bind_tool(get_product_components, product_repo=product_repo),
        ],
    )

from hd_google_hackathon.data.repositories.dummy_product_repository import DummyProductRepository

root_agent = create_agent(product_repo=DummyProductRepository())
