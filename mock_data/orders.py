
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class OrderItem:
    dealer_product_id: str
    quantity: int

@dataclass
class Order:
    id: str
    dealer_id: str
    items: List[OrderItem]
    status: str # e.g., 'new', 'in_progress', 'shipped', 'delivered'

orders = [
    Order(
        id="order_1",
        dealer_id="dealer_1",
        items=[OrderItem(dealer_product_id="ss_duette", quantity=10)],
        status="shipped"
    ),
    Order(
        id="order_2",
        dealer_id="dealer_2",
        items=[
            OrderItem(dealer_product_id="btg_duette", quantity=5),
        ],
        status="in_progress"
    ),
]
