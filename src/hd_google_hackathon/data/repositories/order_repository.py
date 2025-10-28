from abc import ABC, abstractmethod
from typing import List, Optional

from hd_google_hackathon.domain.order import Order, OrderItem

class OrderRepository(ABC):
    @abstractmethod
    def get_order_by_id(self, order_id: str, tenant_id: str) -> Optional[Order]:
        pass

    @abstractmethod
    def get_orders_by_dealer(self, dealer_id: str, tenant_id: str) -> List[Order]:
        pass

    @abstractmethod
    def update_order_status(self, order_id: str, status: str, tenant_id: str) -> Optional[Order]:
        pass

    @abstractmethod
    def create_order(self, dealer_id: str, items: List[dict], tenant_id: str) -> Order:
        pass

    @abstractmethod
    def update_shipment_priority(self, order_id: str, priority: str, tenant_id: str) -> Optional[Order]:
        pass
