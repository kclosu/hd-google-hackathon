"""This module provides a data access layer for managing mock data.

It includes functions to retrieve, create, and update various data entities
such as products, components, plants, dealers, and orders. The data is
stored in-memory and is initialized from other modules within this package.
"""
from typing import List, Optional
import uuid

from .products import products, Product
from .components import components, Component
from .plants import plants, Plant
from .dealers import dealers, Dealer
from .orders import orders, Order, OrderItem
from .dealer_products import dealer_products, DealerProduct

def get_product_by_id(product_id: str) -> Optional[Product]:
    """Finds a product by its ID."""
    return next((product for product in products if product.id == product_id), None)

def get_component_by_id(component_id: str) -> Optional[Component]:
    """Finds a component by its ID."""
    return next((component for component in components if component.id == component_id), None)

def get_plant_by_id(plant_id: str) -> Optional[Plant]:
    """Finds a plant by its ID."""
    return next((plant for plant in plants if plant.id == plant_id), None)

def get_dealer_by_id(dealer_id: str) -> Optional[Dealer]:
    """Finds a dealer by its ID."""
    return next((dealer for dealer in dealers if dealer.id == dealer_id), None)

def get_dealer_product_by_id(dealer_product_id: str) -> Optional[DealerProduct]:
    """Finds a dealer product by its ID."""
    return next((dp for dp in dealer_products if dp.id == dealer_product_id), None)

def get_dealer_products_by_dealer(dealer_id: str) -> List[DealerProduct]:
    """Retrieves all products for a specific dealer."""
    return [dp for dp in dealer_products if dp.dealer_id == dealer_id]

def get_order_by_id(order_id: str) -> Optional[Order]:
    """Finds an order by its ID."""
    return next((order for order in orders if order.id == order_id), None)

def get_orders_by_dealer(dealer_id: str) -> List[Order]:
    """Retrieves all orders for a specific dealer."""
    return [order for order in orders if order.dealer_id == dealer_id]

def create_order(dealer_id: str, items: List[OrderItem]) -> Order:
    """Creates a new order."""
    new_order = Order(
        id=str(uuid.uuid4()),
        dealer_id=dealer_id,
        items=items,
        status="new"
    )
    orders.append(new_order)
    return new_order

def update_order_status(order_id: str, status: str) -> Optional[Order]:
    """Updates the status of an existing order."""
    order = get_order_by_id(order_id)
    if order:
        order.status = status
        return order
    return None
