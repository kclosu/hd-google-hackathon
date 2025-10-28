
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
    Order(
        id="order_3",
        dealer_id="dealer_1",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=2)],
        status="pending"
    ),
    Order(
        id="order_4",
        dealer_id="dealer_3",
        items=[
            OrderItem(dealer_product_id="ss_luminette", quantity=1),
            OrderItem(dealer_product_id="duette", quantity=0),
        ],
        status="cancelled"
    ),
    Order(
        id="order_5",
        dealer_id="dealer_2",
        items=[
            OrderItem(dealer_product_id="btg_duette", quantity=20)
            ],
        status="shipped"
    ),
    Order(
        id="order_6",
        dealer_id="dealer_1",
        items=[
            OrderItem(dealer_product_id="ss_duette", quantity=3),
            OrderItem(dealer_product_id="ss_luminette", quantity=2),
        ],
        status="in_progress"
    ),
    Order(
        id="order_7",
        dealer_id="dealer_3",
        items=[
            OrderItem(dealer_product_id="ss_luminette", quantity=10)
            ],
        status="in_progress"
    ),
    Order(
        id="order_8",
        dealer_id="dealer_2",
        items=[
            OrderItem(dealer_product_id="btg_duette", quantity=7),
            OrderItem(dealer_product_id="btg_duette", quantity=3),
        ],
        status="pending"
    ),
    Order(
        id="order_9",
        dealer_id="dealer_1",
        items=[OrderItem(dealer_product_id="ss_duette", quantity=1)],
        status="returned"
    ),
    Order(
        id="order_10",
        dealer_id="dealer_3",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=4)],
        status="shipped"
    ),
    Order(
        id="order_11",
        dealer_id="dealer_2",
        items=[OrderItem(dealer_product_id="btg_duette", quantity=12)],
        status="in_progress"
    ),
    Order(
        id="order_12",
        dealer_id="dealer_1",
        items=[
            OrderItem(dealer_product_id="ss_duette", quantity=6),
            OrderItem(dealer_product_id="ss_luminette", quantity=2),
        ],
        status="pending"
    ),
    Order(
        id="order_13",
        dealer_id="dealer_2",
        items=[OrderItem(dealer_product_id="btg_duette", quantity=9)],
        status="shipped"
    ),
    Order(
        id="order_14",
        dealer_id="dealer_1",
        items=[OrderItem(dealer_product_id="ss_duette", quantity=4)],
        status="in_progress"
    ),
    Order(
        id="order_15",
        dealer_id="dealer_3",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=6)],
        status="pending"
    ),
    Order(
        id="order_16",
        dealer_id="dealer_2",
        items=[
            OrderItem(dealer_product_id="btg_duette", quantity=2),
            OrderItem(dealer_product_id="btg_duette", quantity=1),
        ],
        status="in_progress"
    ),
    Order(
        id="order_17",
        dealer_id="dealer_1",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=3)],
        status="shipped"
    ),
    Order(
        id="order_18",
        dealer_id="dealer_3",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=8)],
        status="in_progress"
    ),
    Order(
        id="order_19",
        dealer_id="dealer_2",
        items=[OrderItem(dealer_product_id="btg_duette", quantity=15)],
        status="pending"
    ),
    Order(
        id="order_20",
        dealer_id="dealer_1",
        items=[
            OrderItem(dealer_product_id="ss_duette", quantity=2),
            OrderItem(dealer_product_id="ss_duette", quantity=2),
        ],
        status="shipped"
    ),
    Order(
        id="order_21",
        dealer_id="dealer_3",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=5)],
        status="returned"
    ),
    Order(
        id="order_22",
        dealer_id="dealer_2",
        items=[OrderItem(dealer_product_id="btg_duette", quantity=11)],
        status="in_progress"
    ),
    Order(
        id="order_23",
        dealer_id="dealer_1",
        items=[OrderItem(dealer_product_id="ss_duette", quantity=7)],
        status="pending"
    ),
    Order(
        id="order_24",
        dealer_id="dealer_2",
        items=[
            OrderItem(dealer_product_id="btg_duette", quantity=4),
            OrderItem(dealer_product_id="btg_duette", quantity=6),
        ],
        status="shipped"
    ),
    Order(
        id="order_25",
        dealer_id="dealer_3",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=9)],
        status="pending"
    ),
    Order(
        id="order_26",
        dealer_id="dealer_1",
        items=[OrderItem(dealer_product_id="ss_duette", quantity=14)],
        status="in_progress"
    ),
    Order(
        id="order_27",
        dealer_id="dealer_2",
        items=[OrderItem(dealer_product_id="btg_duette", quantity=1)],
        status="cancelled"
    ),
    Order(
        id="order_28",
        dealer_id="dealer_3",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=2)],
        status="shipped"
    ),
    Order(
        id="order_29",
        dealer_id="dealer_1",
        items=[
            OrderItem(dealer_product_id="ss_duette", quantity=5),
            OrderItem(dealer_product_id="ss_luminette", quantity=1),
        ],
        status="in_progress"
    ),
    Order(
        id="order_30",
        dealer_id="dealer_2",
        items=[OrderItem(dealer_product_id="btg_duette", quantity=18)],
        status="pending"
    ),
    Order(
        id="order_31",
        dealer_id="dealer_3",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=7)],
        status="in_progress"
    ),
    Order(
        id="order_32",
        dealer_id="dealer_1",
        items=[OrderItem(dealer_product_id="ss_duette", quantity=2)],
        status="shipped"
    ),
    Order(
        id="order_33",
        dealer_id="dealer_2",
        items=[OrderItem(dealer_product_id="btg_duette", quantity=3)],
        status="returned"
    ),
    Order(
        id="order_34",
        dealer_id="dealer_1",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=4)],
        status="pending"
    ),
    Order(
        id="order_35",
        dealer_id="dealer_3",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=12)],
        status="shipped"
    ),
    Order(
        id="order_36",
        dealer_id="dealer_2",
        items=[OrderItem(dealer_product_id="btg_duette", quantity=6)],
        status="in_progress"
    ),
    Order(
        id="order_37",
        dealer_id="dealer_1",
        items=[
            OrderItem(dealer_product_id="ss_duette", quantity=8),
            OrderItem(dealer_product_id="ss_luminette", quantity=3),
        ],
        status="pending"
    ),
    Order(
        id="order_38",
        dealer_id="dealer_2",
        items=[OrderItem(dealer_product_id="btg_duette", quantity=20)],
        status="shipped"
    ),
    Order(
        id="order_39",
        dealer_id="dealer_3",
        items=[OrderItem(dealer_product_id="ss_luminette", quantity=3)],
        status="in_progress"
    ),
    Order(
        id="order_40",
        dealer_id="dealer_1",
        items=[OrderItem(dealer_product_id="ss_duette", quantity=11)],
        status="shipped"
    ),
    Order(
        id="order_41",
        dealer_id="dealer_2",
        items=[OrderItem(dealer_product_id="btg_duette", quantity=2)],
        status="pending"
    ),
    Order(
        id="order_42",
        dealer_id="dealer_3",
        items=[
            OrderItem(dealer_product_id="ss_luminette", quantity=1),
            OrderItem(dealer_product_id="ss_luminette", quantity=2),
        ],
        status="in_progress"
    ),
]
