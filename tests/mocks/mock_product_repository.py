from typing import Dict, List, Optional

from hd_google_hackathon.data.repositories.product_repository import ProductRepository
from hd_google_hackathon.domain.product import Product, DealerProduct

from .data.products import products as MOCK_PRODUCTS
from .data.dealer_products import dealer_products as MOCK_DEALER_PRODUCTS


class MockProductRepository(ProductRepository):
    """This is a mock implementation of the `ProductRepository` that uses a dictionary for storage."""

    def __init__(self) -> None:
        self._products: Dict[str, Product] = {product.id: product for product in MOCK_PRODUCTS}
        self._dealer_products: Dict[str, DealerProduct] = {
            dealer_product.id: dealer_product for dealer_product in MOCK_DEALER_PRODUCTS
        }

    def get_products(self) -> List[Product]:
        """Return all available products in insertion order."""
        return list(self._products.values())

    def get_product_by_id(self, product_id: str, tenant_id: str) -> Optional[Product]:
        """This method retrieves a product by its ID."""
        # The tenant_id is not used in this mock implementation.
        return self._products.get(product_id)

    def get_dealer_product_by_id(self, dealer_product_id: str, tenant_id: str) -> Optional[DealerProduct]:
        """This method retrieves a dealer product by its ID."""
        # The tenant_id is not used in this mock implementation.
        return self._dealer_products.get(dealer_product_id)

    def get_dealer_products_by_dealer(self, dealer_id: str, tenant_id: str) -> List[DealerProduct]:
        """This method retrieves all dealer products for a given dealer."""
        # The tenant_id is not used in this mock implementation.
        return [dp for dp in self._dealer_products.values() if dp.dealer_id == dealer_id]
