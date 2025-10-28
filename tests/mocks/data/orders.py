
from hd_google_hackathon.domain.order import Order, OrderItem

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
