"""This module defines the data structures and mock data for products.

It includes the `Product` dataclass, which represents a product with its
attributes such as ID, name, description, and a list of component IDs.
The module also provides a predefined list of `Product` instances.
"""
from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    id: str
    name: str
    description: str
    components: List[str] = field(default_factory=list)

products = [
    Product(
        id="duette",
        name="Duette® Honeycomb Shades",
        description="The original cellular shades, specifically engineered to provide beauty and energy efficiency at the window in both cold and warm climates.",
        components=["fabric_1", "headrail_1", "bottom_rail_1", "chain_1"]
    ),
    Product(
        id="silhouette",
        name="Silhouette® Window Shadings",
        description="Features soft adjustable S-shaped vanes that appear to be floating between two sheer fabrics.",
        components=["fabric_2", "headrail_2", "bottom_rail_2"]
    ),
    Product(
        id="luminette",
        name="Luminette® Privacy Sheers",
        description="Perfect for large windows and sliding glass doors, these sheers combine a sheer fabric facing with vertical vanes attached to the back.",
        components=["fabric_3", "headrail_3", "bottom_rail_3", "chain_2"]
    )
]
