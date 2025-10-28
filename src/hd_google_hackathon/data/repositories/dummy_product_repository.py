from typing import List, Optional

from hd_google_hackathon.data.repositories.product_repository import ProductRepository
from hd_google_hackathon.domain.product import Product, DealerProduct


class DummyProductRepository(ProductRepository):
    """This is a dummy implementation of the `ProductRepository` that returns empty data."""

    def get_product_by_id(self, product_id: str, tenant_id: str) -> Optional[Product]:
        return None

    def get_dealer_product_by_id(self, dealer_product_id: str, tenant_id: str) -> Optional[DealerProduct]:
        return None

    def get_dealer_products_by_dealer(self, dealer_id: str, tenant_id: str) -> List[DealerProduct]:
        return []
