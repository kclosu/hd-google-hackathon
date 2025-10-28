from abc import ABC, abstractmethod
from typing import Optional, List

from hd_google_hackathon.domain.product import Product, DealerProduct

class ProductRepository(ABC):
    @abstractmethod
    def get_product_by_id(self, product_id: str, tenant_id: str) -> Optional[Product]:
        pass

    @abstractmethod
    def get_dealer_product_by_id(self, dealer_product_id: str, tenant_id: str) -> Optional[DealerProduct]:
        pass

    @abstractmethod
    def get_dealer_products_by_dealer(self, dealer_id: str, tenant_id: str) -> List[DealerProduct]:
        pass
