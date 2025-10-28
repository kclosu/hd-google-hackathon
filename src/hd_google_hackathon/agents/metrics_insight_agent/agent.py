from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL
from hd_google_hackathon.data.repositories.dealer_repository import DealerRepository
from hd_google_hackathon.data.repositories.order_repository import OrderRepository
from hd_google_hackathon.data.repositories.product_repository import ProductRepository
from hd_google_hackathon.data.repositories.sqlite.dealer_repository import SqliteDealerRepository
from hd_google_hackathon.data.repositories.sqlite.order_repository import SqliteOrderRepository
from hd_google_hackathon.data.repositories.sqlite.product_repository import SqliteProductRepository

def surface_systemic_issues() -> dict:
    """Surfaces systemic issues from a collection of resolved cases."""
    return {"issues": ["Systemic Risk: Component 'CPU-001' has caused 5 order delays this week. Flagging for supply chain review."]}

def predict_maintenance_needs(tenant_id: str) -> dict:
    """Analyzes historical data to predict future maintenance needs for a given tenant."""
    # In a real system, this would analyze real usage and failure data.
    # For this simulation, we'll return a hardcoded prediction.
    return {
        "prediction": "Product 'luminette' at dealer 'David' (tenant_id) has a 75% probability of chain failure in the next 3 months based on usage patterns.",
        "recommendation": "Proactively send replacement chain_2 and schedule maintenance."
    }

def provide_insights(dealer_repo: DealerRepository, order_repo: OrderRepository, product_repo: ProductRepository) -> dict:
    """Provides data-driven insights to support business decisions."""
    try:
        products = product_repo.get_products()
        dealers = dealer_repo.get_all_dealers()
        insights = []
        if not products:
            insights.append("No products found in the mock DB.")
        else:
            insights.append(f"Found {len(products)} products; top sample: {products[0].name}")

        for dealer in dealers:
            orders = order_repo.get_orders_for_dealer(dealer.id)
            insights.append(f"Dealer {dealer.name} has {len(orders)} orders in the mock DB.")

        return {"status": "success", "insights": insights}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def compute_dealer_insights(dealer_id: str, dealer_repo: DealerRepository) -> dict:
    """ADK tool: Compute simple insights for a given dealer id.

    The function is read-only and will try multiple ID normalizations (dash/underscore)
    and fallback to name matching. It returns counts and top products.
    """
    return dealer_repo.get_dealer_insights(dealer_id)

def create_agent(
    dealer_repo: DealerRepository,
    order_repo: OrderRepository,
    product_repo: ProductRepository,
) -> Agent:
    def provide_insights_tool() -> dict:
        return provide_insights(
            dealer_repo=dealer_repo,
            order_repo=order_repo,
            product_repo=product_repo,
        )

    def compute_dealer_insights_tool(dealer_id: str) -> dict:
        return compute_dealer_insights(
            dealer_id=dealer_id,
            dealer_repo=dealer_repo,
        )

    provide_insights_tool.__name__ = "provide_insights"
    compute_dealer_insights_tool.__name__ = "compute_dealer_insights"

    return Agent(
        name="metrics_insight_agent",
        model=DEFAULT_MODEL,
        description="Synthesizes operational KPIs, surfacing systemic issues (e.g., recurring part shortages or dealer training gaps), and predicts maintenance needs from historical data.",
        tools=[
            surface_systemic_issues,
            predict_maintenance_needs,
            provide_insights_tool,
            compute_dealer_insights_tool,
        ],
    )

dealer_repo = SqliteDealerRepository()
order_repo = SqliteOrderRepository()
product_repo = SqliteProductRepository()

root_agent = create_agent(
    dealer_repo=dealer_repo,
    order_repo=order_repo,
    product_repo=product_repo,
)
