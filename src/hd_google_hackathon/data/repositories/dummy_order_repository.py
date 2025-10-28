from typing import List, Optional

from hd_google_hackathon.data.repositories.order_repository import OrderRepository
from hd_google_hackathon.domain.order import Order, OrderItem


class DummyOrderRepository(OrderRepository):
    """This is a dummy implementation of the `OrderRepository` that returns empty data."""

    def get_order_by_id(self, order_id: str, tenant_id: str) -> Optional[Order]:
        return None

    def get_orders_by_dealer(self, dealer_id: str, tenant_id: str) -> List[Order]:
        return []

    def update_order_status(self, order_id: str, status: str, tenant_id: str) -> Optional[Order]:
        return None

    def create_order(self, dealer_id: str, items: List[dict], tenant_id: str) -> Order:
        return Order(id="dummy_order", dealer_id=dealer_id, items=[], status="new")

    def update_shipment_priority(self, order_id: str, priority: str, tenant_id: str) -> Optional[Order]:
        return None
