from typing import List
from hd_google_hackathon.domain.product import Product, DealerProduct
from hd_google_hackathon.data.repositories.product_repository import ProductRepository
from hd_google_hackathon.mock_db import connect_db

class SqliteProductRepository(ProductRepository):
    def get_products(self) -> List[Product]:
        conn = connect_db(read_only=True)
        cur = conn.cursor()
        cur.execute("SELECT id, name, description FROM products")
        rows = cur.fetchall()
        conn.close()
        return [Product(id=row[0], name=row[1], description=row[2]) for row in rows]

    def get_product_by_id(self, product_id: str, tenant_id: str) -> Product | None:
        pass

    def get_dealer_product_by_id(self, dealer_product_id: str, tenant_id: str) -> DealerProduct | None:
        pass

    def get_dealer_products_by_dealer(self, dealer_id: str, tenant_id: str) -> List[DealerProduct]:
        return []
