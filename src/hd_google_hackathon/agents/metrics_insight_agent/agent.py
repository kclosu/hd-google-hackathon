from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL
from hd_google_hackathon.mock_db import connect_db, get_products, get_orders_for_dealer

def synthesize_kpis() -> dict:
    """Synthesizes operational KPIs from various data sources."""
    return {"status": "success", "kpis": {"avg_resolution_time": "24h"}}

def surface_systemic_issues() -> dict:
    """Surfaces systemic issues based on the analysis of operational data."""
    return {"status": "success", "issues": ["Systemic Risk: Component 'CPU-001' has caused 5 order delays this week. Flagging for supply chain review."]}

def provide_insights() -> dict:
    """Provides data-driven insights to support business decisions."""
    try:
        conn = connect_db(read_only=True)
        products = get_products(conn)
        # For demo, compute a simple metric: orders per dealer for seeded dealers
        dealer_ids = ["dealer-1", "dealer-2"]
        dealer_order_counts = {d: len(get_orders_for_dealer(conn, d)) for d in dealer_ids}
        conn.close()

        insights = []
        if not products:
            insights.append("No products found in the mock DB.")
        else:
            insights.append(f"Found {len(products)} products; top sample: {products[0]['name']}")

        for dealer, count in dealer_order_counts.items():
            insights.append(f"Dealer {dealer} has {count} orders in the mock DB.")

        return {"status": "success", "insights": insights}
    except Exception as e:
        return {"status": "error", "message": str(e)}


root_agent = Agent(
    name="metrics_insight_agent",
    model=DEFAULT_MODEL,
    description="Synthesizes operational KPIs, surfacing systemic issues (e.g., recurring part shortages or dealer training gaps).",
    tools=[
        synthesize_kpis,
        surface_systemic_issues,
        provide_insights,
    ],
)