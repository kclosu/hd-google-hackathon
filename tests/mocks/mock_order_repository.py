from typing import Dict, List, Optional

from hd_google_hackathon.data.repositories.order_repository import OrderRepository
from hd_google_hackathon.domain.order import Order, OrderItem

from .data.orders import orders as MOCK_ORDERS


class MockOrderRepository(OrderRepository):
    """This is a mock implementation of the `OrderRepository` that uses a dictionary for storage."""

    def __init__(self) -> None:
        self._orders: Dict[str, Order] = {order.id: order for order in MOCK_ORDERS}

    def get_order_by_id(self, order_id: str, tenant_id: str) -> Optional[Order]:
        """This method retrieves an order by its ID."""
        # The tenant_id is not used in this mock implementation.
        return self._orders.get(order_id)

    def get_orders_by_dealer(self, dealer_id: str, tenant_id: str) -> List[Order]:
        """This method retrieves all orders for a given dealer."""
        # The tenant_id is not used in this mock implementation.
        return [order for order in self._orders.values() if order.dealer_id == dealer_id]

    def update_order_status(self, order_id: str, status: str, tenant_id: str) -> Optional[Order]:
        """This method updates the status of an order."""
        # The tenant_id is not used in this mock implementation.
        order = self._orders.get(order_id)
        if order:
            order.status = status
            order.history.append(f"Status updated to {status}")
        return order

    def create_order(self, dealer_id: str, items: List[dict], tenant_id: str) -> Order:
        """This method creates a new order."""
        # The tenant_id is not used in this mock implementation.
        new_id = f"order_{len(self._orders) + 1}"
        order_items = [OrderItem(**item) for item in items]
        new_order = Order(
            id=new_id,
            dealer_id=dealer_id,
            items=order_items,
            status="new",
            history=[f"Order created by {dealer_id}"],
        )
        self._orders[new_id] = new_order
        return new_order

    def update_shipment_priority(self, order_id: str, priority: str, tenant_id: str) -> Optional[Order]:
        """This method updates the shipment priority of an order."""
        # The tenant_id is not used in this mock implementation.
        order = self._orders.get(order_id)
        if order:
            order.shipment_priority = priority
            order.history.append(f"Shipment priority updated to {priority}")
        return order
