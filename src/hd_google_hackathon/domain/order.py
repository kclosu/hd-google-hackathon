from dataclasses import dataclass, field
from typing import List

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
    history: List[str] = field(default_factory=list)
