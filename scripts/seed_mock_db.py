"""Seed the mock SQLite DB used by the hackathon agents.

This script is safe to call multiple times; it will create tables if missing
and only insert sample rows when tables are empty.
"""
from pathlib import Path
import sys

repo_root = Path(__file__).resolve().parents[1]
# Add src and repo root so we can import both the package and the mock_data package
sys.path.insert(0, str(repo_root / "src"))
sys.path.insert(0, str(repo_root))

from hd_google_hackathon.mock_db import connect_db, initialize_schema, seed_sample_data

# Import the in-memory mock data structures (mock_data is at repo root)
from mock_data.products import products as md_products
from mock_data.dealers import dealers as md_dealers
from mock_data.orders import orders as md_orders
from mock_data.dealer_products import dealer_products as md_dealer_products
from mock_data.components import components as md_components
from mock_data.plants import plants as md_plants
from mock_data.personas import personas as md_personas


def main():
    conn = connect_db(read_only=False)
    initialize_schema(conn)

    # Seed any sample data in the helper first (keeps backward compatibility)
    seed_sample_data(conn)

    cur = conn.cursor()

    # Insert products
    cur.executemany(
        "INSERT OR IGNORE INTO products (id, sku, name, price_cents) VALUES (?, ?, ?, ?)",
        [
            (p.id, getattr(p, "sku", p.id), p.name, getattr(p, "price_cents", 0))
            for p in md_products
        ],
    )

    # Insert dealers
    cur.executemany(
        "INSERT OR IGNORE INTO dealers (id, name, region) VALUES (?, ?, ?)",
        [(d.id, d.name, d.region) for d in md_dealers],
    )

    # Insert dealer_products as a simple mapping table
    cur.execute(
        "CREATE TABLE IF NOT EXISTS dealer_products (id TEXT PRIMARY KEY, product_id TEXT, dealer_id TEXT, brand_name TEXT, dealer_sku TEXT)"
    )
    cur.executemany(
        "INSERT OR IGNORE INTO dealer_products (id, product_id, dealer_id, brand_name, dealer_sku) VALUES (?, ?, ?, ?, ?)",
        [(dp.id, dp.product_id, dp.dealer_id, dp.brand_name, dp.dealer_sku) for dp in md_dealer_products],
    )

    # Insert components
    cur.execute(
        "CREATE TABLE IF NOT EXISTS components (id TEXT PRIMARY KEY, name TEXT, plant_id TEXT)"
    )
    cur.executemany(
        "INSERT OR IGNORE INTO components (id, name, plant_id) VALUES (?, ?, ?)",
        [(c.id, c.name, c.plant_id) for c in md_components],
    )

    # Insert plants
    cur.execute(
        "CREATE TABLE IF NOT EXISTS plants (id TEXT PRIMARY KEY, name TEXT, location TEXT)"
    )
    cur.executemany(
        "INSERT OR IGNORE INTO plants (id, name, location) VALUES (?, ?, ?)",
        [(p.id, p.name, p.location) for p in md_plants],
    )

    # Insert orders and order_items
    cur.execute(
        "CREATE TABLE IF NOT EXISTS order_items (id TEXT PRIMARY KEY, order_id TEXT, product_id TEXT, quantity INTEGER)"
    )
    for o in md_orders:
        cur.execute("INSERT OR IGNORE INTO orders (id, dealer_id, status, created_at) VALUES (?, ?, ?, datetime('now'))", (o.id, o.dealer_id, o.status))
        for idx, item in enumerate(o.items, start=1):
            oi_id = f"{o.id}_item_{idx}"
            # Attempt to map dealer_product_id to product_id via dealer_products
            product_id = None
            matched = [dp for dp in md_dealer_products if dp.id == item.dealer_product_id]
            if matched:
                product_id = matched[0].product_id
            else:
                product_id = item.dealer_product_id
            cur.execute("INSERT OR IGNORE INTO order_items (id, order_id, product_id, quantity) VALUES (?, ?, ?, ?)", (oi_id, o.id, product_id, item.quantity))

    # Insert personas (simple table)
    cur.execute("CREATE TABLE IF NOT EXISTS personas (id TEXT PRIMARY KEY, name TEXT, role TEXT, description TEXT)")
    cur.executemany(
        "INSERT OR IGNORE INTO personas (id, name, role, description) VALUES (?, ?, ?, ?)",
        [(ps.id, ps.name, ps.role, ps.description) for ps in md_personas],
    )

    conn.commit()
    db_list = conn.execute("PRAGMA database_list").fetchall()
    print("Seeded mock DB; database_list=", db_list)
    conn.close()


if __name__ == "__main__":
    main()
