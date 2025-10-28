"""Seed the mock SQLite DB used by the hackathon agents.

This script stays idempotent by creating tables when missing and upserting the
latest mock data that powers the agents and demos.
"""
from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
import sys

repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root / "src"))
sys.path.insert(0, str(repo_root))

from hd_google_hackathon.mock_db import connect_db, initialize_schema

from tests.mocks.data.products import products as seed_products
from tests.mocks.data.dealers import dealers as seed_dealers
from tests.mocks.data.orders import orders as seed_orders
from tests.mocks.data.dealer_products import dealer_products as seed_dealer_products
from tests.mocks.data.components import components as seed_components
from tests.mocks.data.plants import plants as seed_plants
from tests.mocks.data.personas import personas as seed_personas


def ensure_column(conn, table: str, column: str, definition: str) -> bool:
    """Add a column to `table` if it is missing. Returns True when a column was added."""
    existing_columns = {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}
    if column in existing_columns:
        return False
    conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")
    return True


def upgrade_schema(conn) -> None:
    """Align legacy tables with the richer domain models."""
    description_added = ensure_column(conn, "products", "description", "TEXT")
    if description_added:
        conn.execute("UPDATE products SET description = '' WHERE description IS NULL")

    components_added = ensure_column(conn, "products", "components", "TEXT DEFAULT '[]'")
    if components_added:
        conn.execute("UPDATE products SET components = '[]' WHERE components IS NULL")

    shipment_added = ensure_column(conn, "orders", "shipment_priority", "TEXT DEFAULT 'standard'")
    if shipment_added:
        conn.execute(
            "UPDATE orders SET shipment_priority = 'standard' WHERE shipment_priority IS NULL OR shipment_priority = ''"
        )

    history_added = ensure_column(conn, "orders", "history", "TEXT DEFAULT '[]'")
    if history_added:
        conn.execute("UPDATE orders SET history = '[]' WHERE history IS NULL OR history = ''")

    order_date_added = ensure_column(conn, "orders", "order_date", "TEXT")
    if order_date_added:
        conn.execute(
            "UPDATE orders SET order_date = COALESCE(created_at, datetime('now')) WHERE order_date IS NULL OR order_date = ''"
        )

    ensure_column(conn, "order_items", "dealer_product_id", "TEXT")

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS dealer_products (
            id TEXT PRIMARY KEY,
            product_id TEXT NOT NULL,
            dealer_id TEXT NOT NULL,
            brand_name TEXT,
            dealer_sku TEXT,
            FOREIGN KEY (product_id) REFERENCES products(id),
            FOREIGN KEY (dealer_id) REFERENCES dealers(id)
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS components (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            stock INTEGER DEFAULT 0,
            plant_id TEXT
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS plants (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            location TEXT
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS personas (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            description TEXT,
            permissions TEXT
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS product_components (
            product_id TEXT NOT NULL,
            component_id TEXT NOT NULL,
            PRIMARY KEY (product_id, component_id),
            FOREIGN KEY (product_id) REFERENCES products(id),
            FOREIGN KEY (component_id) REFERENCES components(id)
        )
        """
    )


def main() -> None:
    conn = connect_db(read_only=False)
    try:
        initialize_schema(conn)
        upgrade_schema(conn)

        # Upsert core dimension tables.
        product_rows = [
            (
                product.id,
                product.name,
                getattr(product, "description", ""),
                json.dumps(getattr(product, "components", [])),
            )
            for product in seed_products
        ]
        if product_rows:
            conn.executemany(
                "INSERT OR REPLACE INTO products (id, name, description, components) VALUES (?, ?, ?, ?)",
                product_rows,
            )

        dealer_rows = [(dealer.id, dealer.name, dealer.region) for dealer in seed_dealers]
        if dealer_rows:
            conn.executemany(
                "INSERT OR REPLACE INTO dealers (id, name, region) VALUES (?, ?, ?)",
                dealer_rows,
            )

        dealer_product_rows = [
            (dp.id, dp.product_id, dp.dealer_id, dp.brand_name, dp.dealer_sku)
            for dp in seed_dealer_products
        ]
        if dealer_product_rows:
            conn.executemany(
                """
                INSERT OR REPLACE INTO dealer_products (id, product_id, dealer_id, brand_name, dealer_sku)
                VALUES (?, ?, ?, ?, ?)
                """,
                dealer_product_rows,
            )

        component_rows = [
            (component.id, component.name, getattr(component, "description", ""), getattr(component, "stock", 0), getattr(component, "plant_id", None))
            for component in seed_components
        ]
        if component_rows:
            conn.executemany(
                """
                INSERT OR REPLACE INTO components (id, name, description, stock, plant_id)
                VALUES (?, ?, ?, ?, ?)
                """,
                component_rows,
            )

        plant_rows = [(plant.id, plant.name, plant.location) for plant in seed_plants]
        if plant_rows:
            conn.executemany(
                "INSERT OR REPLACE INTO plants (id, name, location) VALUES (?, ?, ?)",
                plant_rows,
            )

        persona_rows = [
            (persona.id, persona.name, persona.role, persona.description, json.dumps(persona.permissions))
            for persona in seed_personas
        ]
        if persona_rows:
            conn.executemany(
                """
                INSERT OR REPLACE INTO personas (id, name, role, description, permissions)
                VALUES (?, ?, ?, ?, ?)
                """,
                persona_rows,
            )

        product_component_rows = [
            (product.id, component_id)
            for product in seed_products
            for component_id in getattr(product, "components", [])
        ]
        if product_component_rows:
            conn.executemany(
                """
                INSERT OR REPLACE INTO product_components (product_id, component_id)
                VALUES (?, ?)
                """,
                product_component_rows,
            )

        # Upsert transactional data.
        dealer_product_lookup = {dp.id: dp.product_id for dp in seed_dealer_products}
        order_insert_sql = """
            INSERT OR REPLACE INTO orders (id, dealer_id, status, created_at, shipment_priority, history, order_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        for order in seed_orders:
            existing = conn.execute(
                "SELECT created_at, shipment_priority, history, order_date FROM orders WHERE id = ?",
                (order.id,),
            ).fetchone()

            created_at = (
                existing[0]
                if existing and existing[0]
                else datetime.now(UTC).isoformat(timespec="seconds")
            )

            shipment_priority = getattr(order, "shipment_priority", "standard") or "standard"

            history_payload = getattr(order, "history", None)
            if history_payload:
                history_json = json.dumps(history_payload)
            else:
                history_json = existing[2] if existing and existing[2] else json.dumps([])

            order_date = (
                existing[3] if existing and existing[3] else created_at
            )

            conn.execute(
                order_insert_sql,
                (order.id, order.dealer_id, order.status, created_at, shipment_priority, history_json, order_date),
            )

            conn.execute("DELETE FROM order_items WHERE order_id = ?", (order.id,))
            for idx, item in enumerate(order.items, start=1):
                dealer_product_id = item.dealer_product_id
                product_id = dealer_product_lookup.get(dealer_product_id, dealer_product_id)
                conn.execute(
                    """
                    INSERT OR REPLACE INTO order_items (id, order_id, product_id, quantity, dealer_product_id)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (f"{order.id}_item_{idx}", order.id, product_id, item.quantity, dealer_product_id),
                )

        conn.commit()
        db_list = conn.execute("PRAGMA database_list").fetchall()
        print("Seeded mock DB; database_list=", db_list)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
