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


def query_db(query: str) -> dict:
    """ADK tool: Run a safe read-only SQL query against the mock DB.

    Only SELECT queries are allowed for safety. Returns rows and column names.
    This lets the agent use the ADK tool mechanism to query the DB directly.
    """
    try:
        q = query.strip().lower()
        if not q.startswith("select"):
            return {"status": "error", "message": "Only SELECT queries are allowed."}

        conn = connect_db(read_only=True)
        cur = conn.cursor()
        cur.execute(query)
        cols = [d[0] for d in cur.description] if cur.description else []
        rows = cur.fetchall()
        # Convert rows to list of dicts for readability
        results = [dict(zip(cols, row)) for row in rows]
        conn.close()
        return {"status": "success", "columns": cols, "rows": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def compute_dealer_insights(dealer_id: str) -> dict:
    """ADK tool: Compute simple insights for a given dealer id.

    The function is read-only and will try multiple ID normalizations (dash/underscore)
    and fallback to name matching. It returns counts and top products.
    """
    try:
        conn = connect_db(read_only=True)
        cur = conn.cursor()

        # Try multiple id variants (dealer-1 vs dealer_1)
        candidates = [dealer_id, dealer_id.replace('-', '_'), dealer_id.replace('_', '-')]
        dealer = None
        for cid in candidates:
            cur.execute("SELECT id, name, region FROM dealers WHERE id = ?", (cid,))
            row = cur.fetchone()
            if row:
                dealer = {"id": row[0], "name": row[1], "region": row[2]}
                break

        # Fallback: match by name containing the input
        if dealer is None:
            cur.execute("SELECT id, name, region FROM dealers WHERE name LIKE ? LIMIT 1", (f"%{dealer_id}%",))
            row = cur.fetchone()
            if row:
                dealer = {"id": row[0], "name": row[1], "region": row[2]}

        if dealer is None:
            conn.close()
            return {"status": "error", "message": f"Dealer '{dealer_id}' not found."}

        did = dealer["id"]

        # Orders count
        cur.execute("SELECT count(1) FROM orders WHERE dealer_id = ?", (did,))
        orders_count = cur.fetchone()[0] or 0

        # Sum of ordered quantities
        cur.execute(
            "SELECT sum(oi.quantity) FROM order_items oi JOIN orders o ON oi.order_id = o.id WHERE o.dealer_id = ?",
            (did,),
        )
        items_sum = cur.fetchone()[0] or 0

        # Top products by quantity
        cur.execute(
            "SELECT oi.product_id, sum(oi.quantity) as total FROM order_items oi JOIN orders o ON oi.order_id=o.id WHERE o.dealer_id=? GROUP BY oi.product_id ORDER BY total DESC LIMIT 5",
            (did,),
        )
        rows = cur.fetchall()

        top_products = []
        for pid, total in rows:
            # Try to resolve a friendly name via dealer_products or products
            cur.execute("SELECT brand_name FROM dealer_products WHERE id = ?", (pid,))
            r = cur.fetchone()
            if r and r[0]:
                name = r[0]
            else:
                cur.execute("SELECT name FROM products WHERE id = ?", (pid,))
                rr = cur.fetchone()
                name = rr[0] if rr else pid
            top_products.append({"product_id": pid, "name": name, "quantity": total})

        conn.close()

        insights = []
        insights.append(f"Dealer '{dealer['name']}' ({did}) has {orders_count} orders and {items_sum} total items ordered.")
        if top_products:
            insights.append("Top products: " + ", ".join([f"{p['name']} ({p['quantity']})" for p in top_products]))
        else:
            insights.append("No product orders found for this dealer.")

        return {"status": "success", "insights": insights, "dealer": dealer, "meta": {"orders_count": orders_count, "items_count": items_sum, "top_products": top_products}}
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
        query_db,
        compute_dealer_insights,
    ],
)