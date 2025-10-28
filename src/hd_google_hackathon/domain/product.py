from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    id: str
    name: str
    description: str
    components: List[str] = field(default_factory=list)

@dataclass
class DealerProduct:
    id: str
    product_id: str  # Foreign key to the generic Product
    dealer_id: str   # Foreign key to the Dealer
    brand_name: str
    dealer_sku: str
