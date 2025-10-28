from typing import Optional, Dict, Any
from hd_google_hackathon.domain.dealer import Dealer
from hd_google_hackathon.data.repositories.dealer_repository import DealerRepository
from hd_google_hackathon.mock_db import connect_db

class SqliteDealerRepository(DealerRepository):
    def get_dealer_by_id(self, dealer_id: str, tenant_id: str) -> Optional[Dealer]:
        # This is a mock implementation, so we ignore tenant_id
        conn = connect_db(read_only=True)
        cur = conn.cursor()
        cur.execute("SELECT id, name, region FROM dealers WHERE id = ?", (dealer_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Dealer(id=row[0], name=row[1], region=row[2])
        return None

    def get_all_dealers(self) -> list[Dealer]:
        conn = connect_db(read_only=True)
        cur = conn.cursor()
        cur.execute("SELECT id, name, region FROM dealers")
        rows = cur.fetchall()
        conn.close()
        return [Dealer(id=row[0], name=row[1], region=row[2]) for row in rows]

    def get_dealer_insights(self, dealer_id: str) -> Dict[str, Any]:
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
